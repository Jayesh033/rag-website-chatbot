
# 🌐 RAG-Based Website Chatbot

A **Retrieval-Augmented Generation (RAG) chatbot** that answers user questions using the content of **any public website URL**.
The system crawls a website, builds a knowledge base, and generates accurate, grounded answers.

---

## 🚀 Features

- 🔗 Accepts any public website URL
- 🕷️ Crawls and extracts website content
- 🧹 Cleans and chunks text data
- 🧠 Builds a searchable knowledge base
- 🔍 Retrieves relevant chunks using semantic search
- 💬 Generates answers using a free LLM
- 🎨 Modern, animated Streamlit UI
- ⚠️ Graceful error handling

---

## 🧠 System Architecture

```
User
 │
 ▼
Streamlit UI
 │
 ▼
URL Validation
 │
 ▼
Website Crawler
 │
 ▼
Text Cleaning & Chunking
 │
 ▼
Embedding Generator (TF-IDF)
 │
 ▼
Vector Store (Cosine Similarity)
 │
 ▼
Top-K Relevant Chunks
 │
 ▼
LLM Answer Generation
 │
 ▼
Final Answer
```

---

## 🛠️ Technology Stack

| Layer | Technology |
|------|-----------|
| Language | Python |
| UI | Streamlit |
| Crawling | Requests, BeautifulSoup |
| Embeddings | TF-IDF |
| Vector Search | Cosine Similarity |
| LLM | Google Gemini (Free Tier) |
| Deployment | Streamlit Community Cloud |

---

## ▶️ How to Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧪 Example Queries

- What is this website about?
- What services are offered?
- Who is the target audience?
- Summarize the website content.
- What does the company specialize in?

---

## ⚠️ Limitations

- JavaScript-heavy sites may not work
- Crawl depth is limited
- Login-protected sites are not supported
- Free LLM rate limits
- In-memory vector storage only

---

## 🚀 Future Enhancements

- PDF and document ingestion
- Persistent vector database (FAISS/Chroma)
- Multi-language support
- Hybrid retrieval
- Chat history export

---

## 📌 Conclusion

This project demonstrates a complete RAG pipeline with a professional UI and free deployment capability.

✅ **Submission Ready**
