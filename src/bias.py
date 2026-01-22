import re

GENDERED_PRONOUNS = {
    "he", "she", "him", "her", "his", "hers"
}

EDUCATION_PRESTIGE = {
    "iit", "nit", "ivy league", "oxford", "cambridge", "mit", "stanford"
}

AGE_PATTERNS = [
    r"\b\d{2}\s*years\s*old\b",
    r"\bage\b\s*\d{2}\b",
    r"\bborn\s+\d{4}\b"
]


def detect_bias_signals(text: str) -> list[str]:
    text_lower = text.lower()
    signals = []

    # Gendered language
    if any(p in text_lower.split() for p in GENDERED_PRONOUNS):
        signals.append("Gendered pronouns detected")

    # Education prestige
    if any(school in text_lower for school in EDUCATION_PRESTIGE):
        signals.append("Prestigious institution mentioned")

    # Age indicators
    for pattern in AGE_PATTERNS:
        if re.search(pattern, text_lower):
            signals.append("Age-related information detected")
            break

    return signals
