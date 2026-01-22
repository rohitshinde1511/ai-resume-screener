import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.skills import skill_gap_analysis

resume = "Experienced Python developer with SQL and Pandas"
jd = "Looking for a data analyst with Python, SQL, Docker, and AWS"

result = skill_gap_analysis(resume, jd)
print(result)
