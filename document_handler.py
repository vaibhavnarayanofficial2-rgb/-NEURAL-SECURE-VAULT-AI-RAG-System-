import os
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings # Naya import

def process_vault_pdfs():
    pdf_folder = "docs" 
    
    # Agar index pehle se bana hai, toh dubara mehnat nahi karni
    if os.path.exists("faiss_index"):
        print("✅ Vault index already exists. Ready to use!")
        return "Success"

    raw_text = ""
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
        print(f"📁 '{pdf_folder}' folder bana diya gaya hai. PDF daalein.")
        return "No Folder"

    # PDFs se text nikalna
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            print(f"📖 Reading: {file}...")
            reader = PdfReader(os.path.join(pdf_folder, file))
            for page in reader.pages:
                raw_text += page.extract_text() or ""

    if not raw_text:
        print("⚠️ No text found in PDFs!")
        return "Empty"

    # Text ko chunks mein todna
    splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=70)
    chunks = splitter.split_text(raw_text)

    # LOCAL EMBEDDINGS (HuggingFace)
    # Pehli baar run hone par ye chhota sa model download karega (~80MB)
    print("⏳ Generating Local Embeddings (No API limits)...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    print("✅ Vault Index Created Successfully (Locally)!")
    return "Success"