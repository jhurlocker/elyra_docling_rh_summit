from huggingface_hub import snapshot_download

# Specify the Hugging Face repository containing the model
model_repo = "ibm-granite/granite-3.3-2b-instruct"
snapshot_download(
    repo_id=model_repo,
    local_dir="model",
    allow_patterns=["*.safetensors", "*.json", "*.txt"],
)