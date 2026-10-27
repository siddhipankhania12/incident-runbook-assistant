import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
    assert len(r.json()["runbooks_found"]) == 5


@pytest.mark.parametrize("alert, expected", [
    ("pod crashloopbackoff liveness probe", "crashloopbackoff"),
    ("pod payments-api OOMKilled exit code 137 memory limit", "oomkilled"),
    ("node DiskPressure disk full logs pvc", "disk-full"),
    ("RDS too many connections max_connections database", "rds-connections"),
    ("deployment rollout failed ImagePullBackOff readiness probe", "failed-deploy"),
])
def test_ask_picks_right_runbook(alert, expected):
    r = client.post("/ask", json={"alert": alert})
    assert r.status_code == 200
    assert r.json()["runbook"] == expected
    assert r.json()["answer"].startswith("#")
