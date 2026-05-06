from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import notes

app = FastAPI(title="Note App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes.router)

@app.get("/")
def read_root():
    return {"message": "Chào mừng đến với Note App"}

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend API hoạt động bình thường!"}