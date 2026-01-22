import re


def detect_bias_signals(text: str) -> list:
    text_lower = text.lower()
    signals = []

    # Graduation year / age proxy
    if re.search(r"\b(19|20)\d{2}\b", text_lower):
        signals.append("Graduation year or age-related information detected")

    # Gendered pronouns
    if re.search(r"\b(he|she|his|her)\b", text_lower):
        signals.append("Gendered pronouns detected")

    # Explicit gender terms
    if re.search(r"\b(male|female)\b", text_lower):
        signals.append("Explicit gender identifiers detected")

    # Personal details
    if re.search(r"\b(married|single|nationality|religion)\b", text_lower):
        signals.append("Personal demographic information detected")

    return signals
