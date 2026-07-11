from fastapi import FastAPI

app = FastAPI(title="Risk Calculator API")


@app.get("/")
def home():
    return {"message": "Risk Calculator API", "status": "Running"}


@app.get("/health")
def health():
    return {"status": "Healthy"}


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
