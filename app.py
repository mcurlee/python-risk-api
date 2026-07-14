from fastapi import FastAPI
import os

app = FastAPI(title="Risk Calculator API")


@app.get("/")
def home():
    return {"message": "Risk Calculator API", "status": "Running", "version": "1.1"}


@app.get("/health")
def health():
    return {
        "health": "Healthy",
    }


@app.get("/version")
def version():
    return {
        "application": "Risk Calculator API",
        "version": "1.1",
    }


@app.post("/risk")
def calculate_risk(impact: int, likelihood: int):

    score = impact * likelihood

    if score >= 40:
        level = "High"
    elif score >= 20:
        level = "Medium"
    else:
        level = "Low"

    return {"impact": impact, "likelihood": likelihood, "score": score, "level": level}
