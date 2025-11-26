# Delta-Demo (JavaScript / Node.js conversion)

This repository was converted from a simple Python FastAPI template to a minimal JavaScript (Node.js + Express) demo.
All leftover Python source files have been removed from the project and the JavaScript implementation under `src/` (Express) is the canonical version.

Quick start:

1. Install dependencies:

```powershell
npm install
```

2. Run in development (with nodemon):

```powershell
npm run dev
```

3. Run tests (Jest + supertest):

```powershell
npm test
```

The project exposes a single route: `GET /health/` which returns JSON `{status: 'ok', message: 'Service is healthy'}`.

Notes:
- The original Python files (FastAPI app and tests) were intentionally removed to keep this repository focused on the Node.js implementation.
