# FAST_API

A small FastAPI starter project intended for students learning how to build APIs (for example, AI/ML services or web backends). This README cleans up the original notes and gives clear, practical instructions to get started.

## Why FastAPI?

- Fast development: type hints + automatic request validation reduce boilerplate.
- High performance: based on Starlette and running on ASGI servers such as Uvicorn.
- Automatic interactive documentation (Swagger UI and ReDoc).
- Good integration with modern Python tools (Pydantic for data validation, dependency injection, async support).

FastAPI is built on Starlette (handles the ASGI request/response lifecycle) and Pydantic (data validation and parsing). Together they let you write succinct, type-safe endpoint code that performs well.

## Key concepts (brief)

- API / Endpoint: a function (route) exposed over HTTP (for example GET /items) that accepts input and returns JSON (or other) responses.
- WSGI vs ASGI: WSGI is the older synchronous interface used by frameworks like Flask. ASGI is asynchronous and supports WebSockets, long-lived connections, and high concurrency — FastAPI is ASGI-first.
- CRUD methods: typical HTTP verbs used for resources:
	- GET — read
	- POST — create
	- PUT/PATCH — update
	- DELETE — remove

## Project files

- `main.py` — the minimal FastAPI app with example endpoints (GET / and GET /about).
- `requirement.txt` — dependency list used by this project (note: consider renaming to `requirements.txt` and pinning versions for reproducibility).

## Setup (Windows PowerShell)

1. Open PowerShell in the project folder (where `main.py` is).
2. (Optional) Create a virtual environment:

```powershell
python -m venv myenv
```

3. Activate the environment (PowerShell):

```powershell
.\myenv\Scripts\Activate.ps1
```

4. Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirement.txt
```

If PowerShell blocks running scripts, you can allow local activation with:

```powershell
# Run as Administrator if needed
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Run the app (development)

Start the dev server using Uvicorn:

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Open a browser and view:

- http://127.0.0.1:8000/docs — interactive Swagger UI
- http://127.0.0.1:8000/redoc — ReDoc documentation

You can also call endpoints from PowerShell:

```powershell
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/about
```

## Example endpoints (from `main.py`)

- GET /

```json
{
	"message": "Hello, World!"
}
```

- GET /about

```json
{
	"message": "About Page"
}
```

## Notes for students

- Use type hints to declare request and response models — Pydantic will validate and coerce data for you.
- Prefer async endpoints for IO-bound work (database, network requests). FastAPI supports both sync and async handlers; ASGI servers like Uvicorn can run them efficiently.
- For production, run Uvicorn without `--reload`, and consider running behind a process manager or use Gunicorn with Uvicorn workers for multiple processes.

## Differences vs Flask (short)

- Flask is WSGI-based and synchronous by default; FastAPI is ASGI-first and designed for async and high concurrency.
- FastAPI provides automatic data validation and interactive docs out of the box; Flask requires more manual wiring or extensions.

## Next recommended steps (optional)

1. Rename and pin dependencies to `requirements.txt` with specific versions.
2. Add a small test suite using `pytest` to verify endpoints.
3. Add a `.gitignore`, `LICENSE`, and `README` enhancements (badges, usage examples) as needed.
4. Add environment config (dotenv) and a `Dockerfile` for containerized deployments.

If you'd like, I can:

- Add tests for the two sample endpoints with `pytest`.
- Create a pinned `requirements.txt` for reproducible installs.
- Add a small PowerShell setup script to create/activate the venv and install deps.

Tell me which of those you want next and I'll add it.



# FAST_API
Mainly for building api for ai
robust industrial level 

for the student ai or cs student fast api is very important to learn
api is connector use to connect vetween the software eg frontend and backend
api set of function special function or endpoint to fech the data



fastapi is baised on starlette and pydantic and is a web framework


starlate   manages resive and responseback of the api
pyndatic data validation 


objective of fast api
performance issue in older framework, and code redutancy and many boilerplate in older framework
in fast api it is fast to run and also to code

browser sand frature responce type and all to webserver
sgi change the http request data to python undestandable code
and api or ml function will do work and but the result is python undestavle form but browser doesnot understand so sgi change it to http or browser understandable format and resturn bask the responce

[basic diff betwell flask and fast api the wsi sg blocking nature sync async nature protacle gunicorn unicorn starlatte werkzeung performance time -- explain   wsgi asgi]

fast api is fast to code
automatic validation(typecheck can define type like type scropt)
airo frnrtayrd onteractibe documentation 
seamless integration weth morden echosystem(inc some example)


[explain statyc vs dynamic api post get put delete crud all]

