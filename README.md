# fastapi-healthcheck

A minimal FastAPI backend with health check and echo endpoints. No frontend.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Root — confirms API is running |
| GET | `/health` | Status, timestamp, uptime |
| GET | `/ping` | Simple ping → pong |
| POST | `/echo` | Returns whatever JSON body you send |
| GET | `/info` | Python version, platform, hostname |
| GET | `/docs` | Auto-generated Swagger UI |

## Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Docker

```bash
docker build -t fastapi-healthcheck .
docker run -p 8000:8000 fastapi-healthcheck
```
