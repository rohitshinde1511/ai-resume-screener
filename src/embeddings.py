from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text: str) -> np.ndarray:
    return model.encode([text])


def compute_similarity(text_a: str, text_b: str) -> float:
    if not text_a.strip() or not text_b.strip():
        raise ValueError("Cannot compute similarity on empty text.")

    emb_a = embed_text(text_a)
    emb_b = embed_text(text_b)

    score = cosine_similarity(emb_a, emb_b)[0][0]
    return round(score * 100, 2)

