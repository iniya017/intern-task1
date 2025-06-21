import chromadb
from chromadb.utils import embedding_functions
import uuid
import os

client = chromadb.PersistentClient(path="data/chromadb")
embedding_fn = embedding_functions.DefaultEmbeddingFunction()
collection = client.get_or_create_collection(name="chapter_versions", embedding_function=embedding_fn)

def save_version(text):
    version_id = str(uuid.uuid4())
    collection.add(documents=[text], ids=[version_id])
    print(f"✅ Saved version with ID: {version_id}")

def search_version(query):
    try:
        from rl_search import search_versions
        search_versions(query)
    except ImportError:
        print("❌ Error: 'rl_search.py' not found in the project directory.")
