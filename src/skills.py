COMMON_SKILLS = {
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "data analysis",
    "statistics",
    "pandas",
    "numpy",
    "scikit-learn",
    "nlp",
    "deep learning",
    "docker",
    "aws",
    "cloud",
    "fastapi",
    "rest api"
}


def extract_skills(text: str) -> set:
    text = text.lower()
    found_skills = set()

    for skill in COMMON_SKILLS:
        if skill in text:
            found_skills.add(skill)

    return found_skills


def skill_gap_analysis(resume_text: str, jd_text: str) -> dict:
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills

    return {
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
    }



