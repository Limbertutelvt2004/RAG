## 🧠 RAG Chatbot (LangChain + Streamlit + FAISS)

- A Retrieval-Augmented Generation (RAG) chatbot built with LangChain, Streamlit, and FAISS, designed to answer questions accurately from custom documents (PDFs).
- The system adapts responses based on the user’s experience level and runs fully offline using local LLMs via Ollama.

---

## ✨ Features

- 📄 PDF Knowledge Ingestion
  - Load and process custom PDF documents

- ✂️ Smart Text Chunking
  - Recursive splitting for optimal retrieval

- 🧠 Semantic Search with FAISS
  - Fast vector similarity search using embeddings

- 🎯 Experience-Aware Answers
  - Adapts explanation depth (Beginner / Intermediate / Advanced)

- 💬 Interactive Chat UI
  - Built with Streamlit for a clean, responsive interface

- 🔒 Offline & Private
  - Uses local LLMs (no data sent to cloud APIs)

---

## 🏗️ Tech Stack

| Component       | Technology                  |
| --------------- | --------------------------- |
| Language        | Python                      |
| UI              | Streamlit                   |
| RAG Framework   | LangChain                   |
| Vector Database | FAISS                       |
| Embeddings      | Sentence Transformers       |
| LLM Backend     | Ollama (LLaMA / Phi / etc.) |

---

## 📂 Project Structure

```powershell
RAG/
├── app.py               # Streamlit UI
├── ingest.py            # PDF ingestion & vectorization
├── rag_pipeline.py      # RAG retrieval + generation logic
├── user_profile.py      # User experience handling
├── requirements.txt     # Python dependencies
├── data/
│   └── docs/            # Input PDFs
└── vectorstore/         # FAISS index (generated, ignored in git)
```

---

## 🚀 Getting Started

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd RAG
```

#### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Add Your PDFs

Place your documents inside:
```bash
data/docs/
```

#### 5️⃣ Ingest Documents
```bash
python ingest.py
```

This generates vector embeddings and stores them in FAISS.

#### 6️⃣ Run the Chatbot
```bash
streamlit run app.py
```

#### Access the app at:
```arduino
http://localhost:8501
```

#### 🧠 Supported LLMs (via Ollama)

- `llama3`
- `phi3`

- Any locally supported Ollama model

> Make sure Ollama is running:
```bash
ollama serve
```

---

### ⚠️ Notes

- The vectorstore/ directory is not committed (generated data)
- Virtual environments are ignored using .gitignore
- Designed for learning, experimentation, and portfolio projects

---

### 🎯 Use Cases

- 📚 Study assistants
- 🧪 Research paper Q&A
- 🏢 Internal documentation bots

---

### 👨‍💻 Developer knowledge bases

- 📌 Future Enhancements
- Chat history memory
- Multi-document support
- Web-based deployment (API-based LLMs)
- User authentication
- RAG evaluation metrics

---

### 🤝 Contributing

Pull requests and suggestions are welcome.
Feel free to fork and experiment.

---

## 👨‍💻 Author

### Vinaal R

Passionate Learner | Aspiring Developer | Python Enthusiast

### Contact me through 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vinaal/) [![GitHub](https://img.shields.io/badge/GitHub-%23181717.svg?logo=github&logoColor=white)](https://github.com/Dark-Vinaal) 

<a href="https://vinaalr.netlify.app/">
  <img src="https://img.shields.io/badge/VR%20-%20Portfolio-d5d5d5?style=for-the-badge&labelColor=0A0209&color=d5d5d5&logoColor=0A0209" />
</a>

---

### ⭐ If you like this project

> Give it a ⭐ on GitHub — it helps a lot!

---