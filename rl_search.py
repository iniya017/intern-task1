import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="data/chromadb")
embedding_fn = embedding_functions.DefaultEmbeddingFunction()
collection = client.get_or_create_collection(name="chapter_versions", embedding_function=embedding_fn)

def search_versions(query, top_k=1):
    print(f"🔍 Searching for: {query}")
    results = collection.query(query_texts=[query], n_results=top_k)
    
    for i in range(top_k):
        print(f"\n⭐ Match {i+1}:")
        print("ID:", results['ids'][0][i])
        print("Text:\n", results['documents'][0][i])
