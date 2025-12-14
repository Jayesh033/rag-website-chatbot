import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:
    def __init__(self, dimension):
        self.embeddings = []
        self.texts = []

    def add(self, embeddings, texts):
        self.embeddings = embeddings
        self.texts = texts

    def search(self, query_embedding, k=5):
        similarities = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]

        top_indices = np.argsort(similarities)[::-1][:k]
        return [self.texts[i] for i in top_indices]
