from pypdf import PdfReader
from fastapi import UploadFile,HTTPException,status


def extract_text(filename):
    reader = PdfReader(filename)
    text = ""
    for page in reader.pages:
        text+= page.extract_text() + "\n"
    return text

def validate_pdf(file: UploadFile)-> bool:
    if file is None:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="No file was uploaded"
        )
    if not file.filename:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            details="File name is missing"
        )
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            details="Only PDF file are allowed"
        )
    if file.content_type!= "application/pdf":
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            details = "Invalid MIME type . Expected application/pdf"
        )
    return True
    