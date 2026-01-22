import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.explain import generate_explanation


def test_generate_explanation_basic():
    explanation = generate_explanation(
        similarity_score=78.0,
        matched_skills=["python", "sql"],
        missing_skills=["docker", "fastapi"],
        bias_signals=["gendered pronouns detected"]
    )

    assert isinstance(explanation, str)
    assert "similarity score" in explanation.lower()
    assert "python" in explanation.lower()
    assert "sql" in explanation.lower()
    assert "docker" in explanation.lower()
