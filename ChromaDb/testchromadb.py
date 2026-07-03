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

# embeddings = model.encode(document)
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

# collection.add(
#     id,embeddings,metadata,document
# )



ques = "Which Programming language must i use ?"
ques2 = "What is Amit's Hobby ?"

embedings = model.encode([ques,ques2])




result = collection.query(
    query_embeddings=embedings,
    n_results = 2
)

context1 = result['documents'][0]
context2 = result['documents'][1]

print(context1,'\n',context2)
print(result)