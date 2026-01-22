import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.skills import skill_gap_analysis


def test_skill_gap_basic():
    resume = "Experienced Python developer with SQL and Pandas"
    jd = "Looking for a data analyst with Python, SQL, Docker, and AWS"

    result = skill_gap_analysis(resume, jd)

    assert "python" in result["matched_skills"]
    assert "sql" in result["matched_skills"]
    assert "docker" in result["missing_skills"]
    assert "aws" in result["missing_skills"]
