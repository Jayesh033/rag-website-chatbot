from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

def generate_embeddings(texts):
    return vectorizer.fit_transform(texts).toarray()

def embed_query(query):
    return vectorizer.transform([query]).toarray()[0]
