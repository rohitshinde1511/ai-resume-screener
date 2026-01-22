import pdfplumber


def extract_text_from_pdf(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()


def clean_text(text: str) -> str:
    """
    Basic cleanup: remove extra spaces and empty lines.
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return " ".join(lines)
