from fastapi import FastAPI
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer


app = FastAPI()

@app.get('/')
def home():
    return {'msg': " thsi is api"}

@app.get('/{pdf_file}')
def read_pdf(pdf_file: str):
    if pdf_file == 'favicon.ico':
        return {'msg': pdf_file}
    reader = PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100
    )

    text_chunks = splitter.split_text(text)
    embeddings = get_embeddings(text_chunks)
    print(embeddings.shape)
    return text_chunks

def get_embeddings(chunks: list[str]):
    transformer_model = SentenceTransformer(
    'sentence-transformers/all-MiniLM-L6-v2'
    )
    return transformer_model.encode(chunks)