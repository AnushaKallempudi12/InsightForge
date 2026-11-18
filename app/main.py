from fastapi import FastAPI

app = FastAPI(
    title="InsightForge API",
    description=(
        "Backend for an AI-powered document intelligence "
        "and workflow platform."
    ),
    version="0.1.0",
)


@app.get("/", tags=["System"])
async def root() -> dict[str, str]:
    """Return basic information about the running application."""
    return {
        "name": "InsightForge",
        "message": "Document intelligence starts here.",
        "status": "running",
    }


@app.get("/api/v1/health", tags=["System"])
async def health_check() -> dict[str, str]:
    """Report whether the API process is responding."""
    return {"status": "healthy"}
