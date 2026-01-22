import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.extract import clean_text


sample = """
Python Developer

Experience with Python, SQL

"""

print(clean_text(sample))
