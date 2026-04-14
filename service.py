from fastapi import FastAPI
from pipeline import run_research_pipeline

app = FastAPI()

@app.post("/run")
def run(topic: str):
    response = run_research_pipeline(topic)
    return {
        "report": response['report'],
        "critique": response['feedback']
    }