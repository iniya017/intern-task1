# versioning.py
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("chapters")

def save_version(title, content):
    collection.add(documents=[content], ids=[title])
    print(f"✅ Version '{title}' saved.")

def search_version(query):
    result = collection.query(query_texts=[query], n_results=1)
    return result["documents"][0][0] if result["documents"] else "No match found."
