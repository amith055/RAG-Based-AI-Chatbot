from fastapi import FastAPI,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from services.pdf_service import extract_text



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.get('/')
def home():
    return {'msg': 'API is working'}


@app.post("/upload")
async def upload_pdf(files: UploadFile = File(...)):
    try:
        contents = await files.read()
        with open(f"uploads/{files.filename}", "wb") as f:
            f.write(contents)

        text = extract_text(f"uploads/{files.filename}")
        print(text)
        return {
            "message": "PDF uploaded successfully",
            "filename": files.filename
        }
    except Exception as e:
        print("Backend",e)



