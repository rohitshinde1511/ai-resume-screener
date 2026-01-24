from fastapi import FastAPI
from pydantic import BaseModel

from src.embeddings import compute_similarity
from src.skills import skill_gap_analysis
from src.bias import detect_bias_signals
from src.explain import generate_explanation

app = FastAPI(title="AI Resume Screener API")


class ScreenRequest(BaseModel):
    resume_text: str
    jd_text: str


class ScreenResponse(BaseModel):
    similarity_score: float
    matched_skills: list[str]
    missing_skills: list[str]
    bias_signals: list[str]
    explanation: str

@app.post("/screen", response_model=ScreenResponse)
def screen_resume(payload: ScreenRequest):
    similarity = compute_similarity(payload.resume_text, payload.jd_text)

    skill_result = skill_gap_analysis(
        resume_text=payload.resume_text,
        jd_text=payload.jd_text
    )

    bias_signals = detect_bias_signals(payload.resume_text)

    explanation = generate_explanation(
        similarity_score=similarity,
        matched_skills=skill_result["matched_skills"],
        missing_skills=skill_result["missing_skills"],
        bias_signals=bias_signals
    )

    return ScreenResponse(
        similarity_score=similarity,
        matched_skills=skill_result["matched_skills"],
        missing_skills=skill_result["missing_skills"],
        bias_signals=bias_signals,
        explanation=explanation
    )
