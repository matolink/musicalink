from fastapi import FastAPI
from backend.infrastructure.router import router as backend_router
from frontend.router import router as frontend_router

app = FastAPI()
app.include_router(backend_router)
app.include_router(frontend_router)

