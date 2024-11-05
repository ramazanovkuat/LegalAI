import pickle
import os
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker

name_db = f"FAISS_CPU_USER-bge-m3_RecursiveCharacter_CHUNK_SIZE_512"
load_path_db = f"data/vector_dbs/{name_db}"
load_path_db = os.path.join(os.path.dirname(__file__), load_path_db)

with open(load_path_db, 'rb') as f:
    db = pickle.load(f)

name_chunked_documents_with_page_content = f"chunked_documents_with_page_content_RecursiveCharacter_CHUNK_SIZE_512"
load_path_chunked_documents_with_page_content = f"data/chunked_documents/{name_chunked_documents_with_page_content}"
load_path_chunked_documents_with_page_content = os.path.join(os.path.dirname(__file__), load_path_chunked_documents_with_page_content)

with open(f'{load_path_chunked_documents_with_page_content}.pkl', 'rb') as f:
    chunked_documents_with_page_content = pickle.load(f)

bm25_retriever = BM25Retriever.from_documents(
    chunked_documents_with_page_content)


num_docs = 3 # как аргумент фунции
retriever = db.as_retriever(search_kwargs={"k": num_docs})
bm25_retriever.k = num_docs

reranker_model_name = "BAAI/bge-reranker-v2-m3"
num_docs_rerank = 1 # как аргумент фунции
model = HuggingFaceCrossEncoder(model_name=reranker_model_name)
compressor = CrossEncoderReranker(model=model, top_n=num_docs_rerank)

def bm25_faiss_rerank(question):

    print("---Сообщение---")
    print(question)
    print("---------------")

    # initialize the ensemble retriever
    vector_database = EnsembleRetriever(
        retrievers=[bm25_retriever, retriever], weights=[0.5, 0.5] # You can adjust the weight of each retriever in the EnsembleRetriever
    )

    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=vector_database
    )
    docs = compression_retriever.invoke(question)
    
    print('---Документы---')
    print(docs)
    print('--------------')

    return docs 
