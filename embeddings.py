from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    'sentence-transformers/all-MiniLM-L6-v2'
)

chunks = [
    "Python is Used in AI",
    "Java is used in enterprise system",
    "Machine Learning uses data"
]

embeddings = model.encode(chunks)
print(" This is embeding " ,embeddings)