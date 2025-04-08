Run to setup RHPDS CI

### OPTIONAL - RUN ONCE ###
OpenShift AI
oc apply -k ./components/openshift-ai/operator/overlays/fast
oc apply -k ./components/openshift-ai/instance/overlays/fast
oc new-project summit-project

### RUN ONCE ###
OpenShift AI Single Serving runtime
oc apply -k components/openshift-servicemesh/operator/overlays/stable
oc apply -k components/openshift-serverless/operator/overlays/stable
oc apply -k components/model-server/components-serving
oc apply -f components/serving-runtime/vllm-cpu-runtime-template.yaml

OpenShift Pipelines
oc apply -k components/openshift-pipelines/operator/overlays/latest/

### BEGIN LOOP - I NEED ENV VAR HERE ###
Minio
oc apply -k ./components/minio/base
export MINIO_API_URL=$(oc get routes -n summit-project -o custom-columns=":spec.host" | grep minio-api)
envsubst < components/create-bucket-job/base/create-bucket-job-template.yaml > components/create-bucket-job/base/create-bucket-job.yaml
oc create configmap -n summit-project model-config-file --from-file=IntroToML_Cert.pdf
oc apply -k ./components/create-bucket-job/base

OpenShift AI workbench
oc apply -f components/datascience-pipelines/secret-dashboard-dspa-secret.yaml
oc apply -f components/datascience-pipelines/dspa.yaml
oc apply -k ./components/workbenches/base/

OpenShift Pipeline triggers
oc apply -f components/ocp-pipeline-triggers/
oc apply -f components/ocp-pipeline-triggers/el-route.yaml
### END LOOP ###


