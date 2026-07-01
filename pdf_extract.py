from pypdf import PdfReader
from fastapi import FastAPI
from collections import defaultdict

app = FastAPI()


@app.get("/{pdffile}")
def home(pdffile: str):
    if pdffile == "favicon.ico":
        print(pdffile)
        return {"message": "Ignore"}
    reader = PdfReader(pdffile)
    text = defaultdict()
    j = 1
    print(len(reader.pages))
    for page in reader.pages:
        text[f'pages: {j}'] = page.extract_text() + '\n'
        j+=1
    
    return {'Message': text}