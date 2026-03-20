# 📘 Assignment: FastAPI APIs

## 🎯 Objective

Build a small REST API using FastAPI to learn endpoint creation, request handling, and response modeling. Students will practice designing JSON APIs, input validation, and using path/query parameters.

## 📝 Tasks

### 🛠️ Create a basic FastAPI service

#### Description

Set up a new FastAPI app with a root endpoint and a simple data endpoint.

#### Requirements

Completed program should:
- Create an app in `main.py` using `FastAPI()`.
- Add `GET /` endpoint that returns `{ "message": "Welcome to FastAPI" }`.
- Add `GET /items/{item_id}` endpoint returning JSON with `item_id` and `name` or a placeholder.
- Launch the app with `uvicorn main:app --reload`.

### 🛠️ Add query parameters and validation

#### Description

Enhance the API with query parameters and request body model validation.

#### Requirements

Completed program should:
- Add `GET /search` accepting `q: str` and optional `limit: int = 10` returns sample results.
- Add `POST /items` that accepts a Pydantic model `Item` with fields `name: str`, `description: str | None`, `price: float`, `tax: float | None`.
- Return created item with calculated `price_with_tax`.
- Handle invalid input with meaningful HTTP 422 responses (FastAPI default behavior).

### 🛠️ Include docs and tests (optional but recommended)

#### Description

Wrap up with self-review and optional verification using automatic docs and basic endpoints.

#### Requirements

Completed program should:
- Confirm the app works at `/docs` and `/redoc`.
- Optionally include a file `test_main.py` with one simple test using `TestClient`.
