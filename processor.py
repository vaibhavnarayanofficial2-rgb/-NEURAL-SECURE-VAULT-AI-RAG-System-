import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def create_vector_db():
    print("7 Scan PDF .")
    if not os.path.exists('docs'):
        os.makedirs('docs')
        print("docs' A folder has been created. Place your PDFs in it..")
        return

    loader = DirectoryLoader('docs/', glob="./*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    
    if not documents:
        print('docs')
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = FAISS.from_documents(texts, embeddings)
    vector_db.save_local("faiss_index")
    print(f"Database Ready! {len(documents)} documents index.")

def ask_vault_ai(query):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    if os.path.exists("faiss_index"):
        vector_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    else:
        return "Database not found. First, run 'python processor.py' in the terminal."

    docs = vector_db.similarity_search(query)
    context = "\n".join([doc.page_content for doc in docs])

    # --- LATEST GEMINI 2.5 FLASH ---
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(f"Context: {context}\n\nQuestion: {query}")
        return response.text
    except Exception as e:
        # Fallback latest model in problem
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(f"Context: {context}\n\nQuestion: {query}")
        return response.text

if __name__ == "__main__":
    create_vector_db()
