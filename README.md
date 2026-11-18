# InsightForge

**An AI-powered document intelligence and workflow platform.**

InsightForge is being built as a practical AI engineering project. Its first module, **Academic Assignment Intelligence**, will help turn user-provided assignment instructions, rubrics, and supporting materials into structured, evidence-grounded work.

The goal is not simply to build a chatbot. The goal is to engineer a reliable application with document ingestion, text extraction, retrieval, model integration, validation, APIs, testing, and deployment.

## First module: Academic Assignment Intelligence

Planned capabilities (introduced incrementally):

- Accept assignment instructions, rubrics, and supporting documents.
- Extract and organize their contents.
- Identify requirements and map them to evidence in the supplied materials.
- Help draft and review an assignment against its rubric.
- Flag missing evidence, unsupported statements, and citation gaps instead of inventing information.

These are roadmap goals, not features that are already implemented.

## Engineering principles

- Ground outputs in the materials supplied by the user.
- Do not fabricate citations, sources, or evidence.
- Clearly flag uncertainty and missing information.
- Validate files and inputs before processing them.
- Test each milestone before adding complexity.
- Keep the application modular so future modules can reuse the platform.

## Current milestone

**Milestone 1 — Backend foundation**

The initial backend uses Python and FastAPI and exposes:
- `GET /` — basic application information.
- `GET /api/v1/health` — a health-check response.

## Run locally

Requirements: Python 3.11 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:
- API: http://127.0.0.1:8000
- Interactive API documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/api/v1/health

## Planned roadmap

1. Backend foundation and API conventions.
2. Secure document upload and PDF/DOCX text extraction.
3. LLM integration and core concepts such as tokens and context windows.
4. Chunking, embeddings, vector search, and retrieval-augmented generation (RAG).
5. Rubric-aware drafting and evidence validation.
6. Tool calling and multi-step workflow orchestration.
7. Persistence, automated evaluation, security hardening, monitoring, and deployment.

Each stage will be implemented and tested before moving to the next.
