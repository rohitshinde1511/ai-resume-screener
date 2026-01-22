def validate_job_description(text: str, min_length: int = 200):
    if not text or len(text.strip()) < min_length:
        raise ValueError("Job description is too short or empty.")
