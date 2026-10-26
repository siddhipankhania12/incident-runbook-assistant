from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

RUNBOOK_DIR = Path(__file__).parent.parent / "runbooks"


class AskRequest(BaseModel):
    alert: str


def load_runbooks():
    runbooks = {}
    for file in RUNBOOK_DIR.glob("*.md"):
        runbooks[file.stem] = file.read_text(encoding="utf-8-sig")
    return runbooks


@app.get("/health")
def health():
    return {
        "status": "ok",
        "runbook_folder": str(RUNBOOK_DIR),
        "runbooks_found": list(load_runbooks().keys()),
    }


@app.post("/ask")
def ask(req: AskRequest):
    alert_words = req.alert.lower().split()
    best_name, best_score = None, 0

    for name, text in load_runbooks().items():
        score = sum(text.lower().count(word) for word in alert_words)
        if score > best_score:
            best_name, best_score = name, score

    if best_name is None:
        return {"answer": "No matching runbook. Escalate to on-call lead."}

    return {"runbook": best_name, "score": best_score, "answer": load_runbooks()[best_name]}
