Run to setup RHPDS CI

OpenShift AI
oc apply -k ./components/openshift-ai/operator/overlays/fast
oc apply -k ./components/openshift-ai/instance/overlays/fast
oc new-project summit-project

Mino
oc apply -k ./components/minio/base
export MINIO_API_URL=$(oc get routes -n summit-project -o custom-columns=":spec.host" | grep minio-api)
envsubst < components/create-bucket-job/base/create-bucket-job-template.yaml > components/create-bucket-job/base/create-bucket-job.yaml
oc create configmap -n summit-project model-config-file --from-file=IntroToML_Cert.pdf
oc apply -k ./components/create-bucket-job/base

OpenShift AI workbench
oc apply -k ./components/workbenches/base/
oc apply -f components/datascience-pipelines/secret-dashboard-dspa-secret.yaml
oc apply -f components/datascience-pipelines/dspa-jh.yaml

OpenShift Pipelines
oc apply -k components/openshift-pipelines/operator/overlays/latest/

OpenShift Pipeline instance and triggers
oc apply -f components/ocp-pipeline-triggers/
oc apply -f components/ocp-pipeline-triggers/el-route.yaml

OpenShift AI Single Serving runtime
oc apply -k components/openshift-servicemesh/operator/overlays/stable
oc apply -k components/openshift-serverless/operator/overlays/stable
oc apply -k components/model-server/components-serving
oc apply -f components/serving-runtime/vllm-cpu-runtime-template.yaml

