
from dotenv import load_dotenv
import chromadb
import os
import chromadb.utils.embedding_functions as embedding_functions

load_dotenv()

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key = os.environ.get("OPENAI_API_KEY"),
                model_name="text-embedding-ada-002"
            )


chroma_client = chromadb.HttpClient(host='localhost', port=8000)

collection = chroma_client.get_or_create_collection(name="datacamp", embedding_function=openai_ef)

print(collection.count())

print(chroma_client.list_collections())




