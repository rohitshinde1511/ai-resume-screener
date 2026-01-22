def generate_explanation(
    similarity_score: float,
    matched_skills: list,
    missing_skills: list,
    bias_signals: list,
) -> str:
    explanation = []

    explanation.append(
        f"The resume shows a similarity score of {similarity_score:.2f} with the job description."
    )

    if matched_skills:
        explanation.append(
            f"Matched skills include: {', '.join(matched_skills)}."
        )
    else:
        explanation.append("No direct skill matches were identified.")

    if missing_skills:
        explanation.append(
            f"Skills not found in the resume but mentioned in the job description include: {', '.join(missing_skills)}."
        )

    if bias_signals:
        explanation.append(
            "The resume contains certain demographic or contextual signals that may require careful human review."
        )

    return " ".join(explanation)
