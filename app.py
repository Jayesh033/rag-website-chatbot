import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="RAG Website Chatbot",
    layout="wide"
)

st.title("🌐 RAG-Based Website Chatbot")
st.write("Enter a website URL, build a knowledge base, and ask questions about the site.")

# ---------------- SESSION STATE ----------------
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# ---------------- URL INPUT ----------------
url = st.text_input("Enter Website URL", placeholder="https://example.com")

# ---------------- BUILD KNOWLEDGE BASE ----------------
if st.button("Crawl & Build Knowledge Base"):
    if not url:
        st.warning("Please enter a valid URL")
    else:
        with st.spinner("🔍 Crawling website..."):
            try:
                from crawler import crawl_website
                pages = crawl_website(url)
            except Exception as e:
                st.error(f"Crawling failed: {e}")
                pages = []

        if not pages:
            st.error("No content could be extracted from this website.")
        else:
            with st.spinner("🧹 Processing & chunking content..."):
                from preprocess import prepare_chunks
                chunks = prepare_chunks(pages)

            with st.spinner("🧠 Generating embeddings & building vector store..."):
                from embeddings import generate_embeddings
                from vector_store import VectorStore

                texts = [c["text"] for c in chunks]
                embeddings = generate_embeddings(texts)

                vector_store = VectorStore(dimension=len(embeddings[0]))
                vector_store.add(embeddings, chunks)

                st.session_state.vector_store = vector_store

            st.success("✅ Knowledge Base is ready!")

# ---------------- DIVIDER ----------------
st.divider()

# ---------------- QUESTION INPUT ----------------
question = st.text_input(
    "Ask a question about the website",
    placeholder="What is this website about?"
)

# ---------------- ANSWER GENERATION ----------------
if st.button("Ask"):
    if not st.session_state.vector_store:
        st.warning("Please crawl a website first.")
    elif not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("🔎 Retrieving relevant information..."):
            from embeddings import embed_query
            query_embedding = embed_query(question)

            top_chunks = st.session_state.vector_store.search(
                query_embedding,
                k=5
            )

        with st.spinner("✍️ Generating answer..."):
            from rag import generate_answer
            answer = generate_answer(question, top_chunks)

        st.subheader("📌 Answer")
        st.write(answer)

        with st.expander("🔍 Source Chunks Used"):
            for i, chunk in enumerate(top_chunks, 1):
                st.markdown(f"**Chunk {i} (Source):** {chunk['source']}")
                st.write(chunk["text"][:500] + "...")
