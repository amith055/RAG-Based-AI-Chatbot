import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    'sentence-transformers/all-MiniLM-L6-v2'
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name='documents'
)

id = ['chunk_01','chunk_02','chunk03']
document = ['This is amit, my age is 21','Python is a programming language , i installed it yesterday','My hobbies are coding']

embeddings = model.encode(document)
metadata = [
    {
       'name': 'Data.pdf',
       'page': 1
    },
    {
        'name': 'Data.pdf',
        'page':2
    },
    {
        'name':'Data.pdf',
        'page':3
    }
]

collection.add(
    id,embeddings,metadata,document
)

print(embeddings,type(embeddings))


print("Collection Created")