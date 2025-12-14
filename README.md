
# 🌐 RAG-Based Website Chatbot (Free Model, Submission-Ready)

## 📌 Project Overview
This project implements a **Retrieval-Augmented Generation (RAG) based chatbot** that answers user questions using the content of **any website URL** provided by the user.

The application:
- Crawls a website
- Builds a knowledge base from extracted content
- Retrieves relevant information using semantic search
- Generates answers grounded strictly in website data
- Uses a **free AI model**
- Can be deployed **completely free**

This project is suitable for **college assignments, company assessments, and interviews**.

---

## 🎯 Problem Statement
**Input:** Website URL  
**Process:** Crawl → Clean → Chunk → Embed → Retrieve → Answer  
**Output:** Chatbot answers questions about the website

---

## 🧠 System Architecture

```
User
 │
 │  (Website URL / Question)
 ▼
Streamlit UI
 │
 ▼
Website Crawler
 │  - Fetch HTML pages
 │  - Extract visible text
 ▼
Text Cleaning & Chunking
 │
 ▼
Embedding Generator (TF-IDF)
 │
 ▼
Vector Store (Cosine Similarity Search)
 │
 ▼
Top-K Relevant Chunks
 │
 ▼
Answer Generator (Free AI Model)
 │
 ▼
Final Answer to User
```

---

## 🛠️ Technology Stack

| Layer | Technology |
|------|-----------|
| Language | Python |
| UI | Streamlit |
| Crawling | Requests, BeautifulSoup |
| Text Processing | Custom chunking |
| Embeddings | TF-IDF (scikit-learn) |
| Vector Search | Cosine Similarity |
| LLM (Free) | Google Gemini Flash Lite |
| Deployment | Streamlit Community Cloud |

---

## 🤖 Free AI Model Used

**Model Name:** `models/gemini-flash-lite-latest`

### Why this model?
- Free-tier supported
- Fast and lightweight
- Suitable for text-based Q&A
- No billing or credit card required

---

## ⚙️ Features

### ✅ Website Crawling
- Crawls internal pages (depth ≤ 2)
- Extracts titles, headings, and visible text
- Ignores images, scripts, and ads

### ✅ Knowledge Base Creation
- Cleans and normalizes text
- Splits text into overlapping chunks
- Generates TF-IDF embeddings

### ✅ RAG-Based Question Answering
- Converts user query into vector
- Retrieves top-k relevant chunks
- Generates grounded answers

### ✅ User Interface
- Simple Streamlit UI
- URL input
- Crawl & build button
- Chat-style Q&A

---

## ▶️ How to Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open browser at:
```
http://localhost:8501
```

---

## 🌍 Free Deployment

This application can be deployed for free using **Streamlit Community Cloud**.

**Steps:**
1. Push code to GitHub
2. Deploy via Streamlit Cloud
3. Add API key in Secrets
4. Get a public URL

---

## 🧪 Example Usage

**Website URL:**
```
https://example.com
```

**Questions:**
- What is this website about?
- What services are mentioned?
- Summarize the purpose of the website

---

## ⚠️ Limitations
- JavaScript-rendered websites are not supported
- Crawl depth and pages are limited
- Free model has rate limits

---

## 🚀 Future Enhancements
- Sitemap crawling
- PDF ingestion
- Persistent vector databases
- Multi-language support
- Model switching (Offline / Gemini / Llama)

---

## 🔐 Security
- API keys stored using environment variables
- No user data stored permanently

---

## 📌 Conclusion
This project demonstrates a **complete, cost-free RAG pipeline** with a clean architecture and free deployment options.  
It satisfies all task requirements and is **submission-ready**.

---

✅ **Project Status: COMPLETE**
