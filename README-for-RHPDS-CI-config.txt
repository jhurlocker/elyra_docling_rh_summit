Run to setup RHPDS CI

### OPTIONAL - RUN ONCE ###
OpenShift AI
oc apply -k ./components/openshift-ai/operator/overlays/fast
oc apply -k ./components/openshift-ai/instance/overlays/fast

### RUN ONCE ###
OpenShift AI Single Serving runtime
oc apply -k components/openshift-servicemesh/operator/overlays/stable
oc apply -k components/openshift-serverless/operator/overlays/stable
oc apply -k components/model-server/components-serving

OpenShift Pipelines
oc apply -k components/openshift-pipelines/operator/overlays/latest/

### BEGIN LOOP - I NEED ENV VAR HERE ###
#THIS IS JUST FOR TESTING
oc new-project summit-project-user10

Minio
export SUMMIT_PROJECT=summit-project-user10
oc apply -k ./components/minio/base
envsubst < components/create-bucket-job/base/create-bucket-job-template.yaml > components/create-bucket-job/base/create-bucket-job.yaml
oc create configmap -n ${SUMMIT_PROJECT} model-config-file
oc apply -k ./components/create-bucket-job/base

RoleBinding
oc apply -f components/workbenches/base/role-binding.yaml

OpenShift Pipeline triggers
export OCP_APPS_URL=$(oc get ingresses.config.openshift.io cluster -o jsonpath='{.spec.domain}')
envsubst < components/ocp-pipeline-triggers/el-route-template.yaml > components/ocp-pipeline-triggers/el-route.yaml
oc apply -k components/ocp-pipeline-triggers/

### END LOOP ###

### SETTING UP THE MODEL PROJECT ###
oc new-project granite-model-project
export SUMMIT_PROJECT=granite-model-project
oc apply -k ./components/minio/base
export MINIO_API_URL=$(oc get routes -n $SUMMIT_PROJECT -o custom-columns=":spec.host" | grep minio-api)
envsubst < components/create-bucket-job/base/create-bucket-job-template.yaml > components/create-bucket-job/base/create-bucket-job.yaml
oc create configmap -n ${SUMMIT_PROJECT} model-config-file 
oc apply -k ./components/create-bucket-job/base

### DOWNLOAD MODEL files
pip install huggingface_hub
python components/model-server/download-model.py

### UPLOAD MODEL FILES
python components/model-server/model-folder-upload.py

oc apply -f components/model-server/sa-secret-token.yaml
oc apply -f components/model-server/granite2b-conn.yaml
oc apply -f components/model-server/model-namespace.yaml
oc apply -f components/model-server/servingruntimes.yaml
oc apply -f components/model-server/inferenceservice.yaml
### END SETTING UP THE MODEL PROJECT ###
