import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bias import detect_bias_signals

resume = """
John Doe
Graduated in 2019.
He has experience in Python.
Nationality: Indian
"""

signals = detect_bias_signals(resume)
print(signals)
