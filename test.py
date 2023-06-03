import requests
from typing import List

API_BASE_URL = "http://127.0.0.1:8000"  # Replace with your actual API base URL


def embed_documents(files: List[str], collection_name: str):
    endpoint = f"{API_BASE_URL}/embed"
    files_data = [("files", open(file, "rb")) for file in files]
    data = {"collection_name": collection_name}

    response = requests.post(endpoint, files=files_data, data=data)
    if response.status_code == 200:
        print("Documents embedded successfully!")
    else:
        print("Document embedding failed.")
        print(response.text)


def retrieve_documents(query: str, collection_name: str):
    endpoint = f"{API_BASE_URL}/retrieve"
    data = {"query": query, "collection_name": collection_name}

    response = requests.post(endpoint, params=data)
    if response.status_code == 200:
        result = response.json()
        print("Results:")
        print(result["results"])

        print("\nDocuments:")
        for doc in result["docs"]:
            print(doc)
    else:
        print("Failed to retrieve documents.")
        print(response.text)


# Test the backend without Streamlit
def test_backend():
    # Test embedding documents
    files_to_upload = [".dev-data/sources/document1.txt", ".dev-data/sources/document2.txt"]
    collection_name = "coding"
    embed_documents(files_to_upload, collection_name)

    # Test retrieving documents
    query = "what is the project about ?"
    collection_name = "coding"
    retrieve_documents(query, collection_name)


if __name__ == "__main__":
    test_backend()
