import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.embeddings import compute_similarity


def test_similarity_score_range():
    resume = "Python developer with experience in SQL and data analysis"
    jd = "Looking for a data analyst skilled in Python and SQL"

    score = compute_similarity(resume, jd)

    assert isinstance(score, float)
    assert 0 <= score <= 100


def test_similarity_empty_text():
    with pytest.raises(ValueError):
        compute_similarity("", "Some JD")
