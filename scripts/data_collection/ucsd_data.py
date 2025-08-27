import os
import requests
from pathlib import Path

UCSD_URL = "https://mcauleylab.ucsd.edu/public_datasets/gdrive/googlelocal/"
DEST_DIR = Path(__file__).parent.parent.parent / "data" / "raw" / "ucsd"

def download_file(url, dest_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def main():
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    files = [
        "review-Alabama_10.json.gz",
        "review-Washington_10.json.gz"
    ]
    for filename in files:
        file_url = UCSD_URL + filename
        dest_path = DEST_DIR / filename
        print(f"Downloading {filename} ...")
        download_file(file_url, dest_path)
        print(f"Saved to {dest_path}")

if __name__ == "__main__":
    main()