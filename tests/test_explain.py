import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.explain import generate_explanation

text = generate_explanation(
    similarity_score=0.78,
    matched_skills=["Python", "SQL"],
    missing_skills=["Docker", "FastAPI"],
    bias_signals=["Gendered pronouns detected"],
)

print(text)
