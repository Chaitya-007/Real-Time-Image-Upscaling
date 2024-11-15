import gdown

# Google Drive file ID
file_id = "1TPrz5QKd8DHHt1k8SRtm6tMiPjz_Qene"
gdown.download(f"https://drive.google.com/uc?id={file_id}", quiet=False)
