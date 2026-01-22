import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.embeddings import compute_similarity

resume = "Python developer with experience in SQL and data analysis"
jd = "Looking for a data analyst skilled in Python and SQL"

score = compute_similarity(resume, jd)
print("Similarity Score:", score)
