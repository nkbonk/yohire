from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Yohire!"}

app = FastAPI()

app.add_middleware(
    # CORS middleware нужен для того, чтобы фронтенд на другом порту (5173) мог обращаться к API
    # Без этого браузер будет блокировать запросы из-за политики безопасности
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # фронт
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)