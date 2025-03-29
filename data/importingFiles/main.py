import kagglehub

# Download latest version
path = kagglehub.dataset_download("xainano/handwrittenmathsymbols")

print("Path to dataset files:", path)