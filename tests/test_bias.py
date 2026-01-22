import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bias import detect_bias_signals


def test_bias_detection_basic():
    resume = """
    John Doe
    He is a data analyst with 5 years of experience.
    Graduated from IIT Bombay.
    """

    signals = detect_bias_signals(resume)

    assert "Gendered pronouns detected" in signals
    assert "Prestigious institution mentioned" in signals
