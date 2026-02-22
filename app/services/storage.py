import os
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

def save_file(file: UploadFile) -> str:
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file.filename
