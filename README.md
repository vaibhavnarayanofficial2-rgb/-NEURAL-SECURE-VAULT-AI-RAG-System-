#NEURAL SECURE VAULT (AI-RAG System)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-orange.svg)](https://aistudio.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Neural Secure Vault is an advanced Retrieval-Augmented Generation (RAG) system that transforms your personal documents (PDFs) into a secure digital vault, enabling safe storage, intelligent retrieval, and AI-powered interaction with your information.

---

Key Features
Face-ID Authentication: Only authorized users can unlock the vault.
Intelligent RAG: Uses the FAISS Vector Database to retrieve accurate context from documents.
Gemini 2.0 Integration: Leverages the latest AI model to provide fast and intelligent responses.
Privacy-Focused: With .env integration, your API keys and personal files remain secure at all times.

---

## Project Structure
```text
AI_Secure_Vault/
├── docs/              # Your secret PDF files will be here.
├── faiss_index/        # AI brain (Vector Database)
├── app.py              # Main Entry Point (Face-ID + Chat)
├── processor.py        # AI Processing & RAG Logic
├── auth.py             # Face-ID Security System
├── .env                # (Hidden) API Keys 🤫
└── .gitignore          # Prevents keys from being uploaded to GitHub.
