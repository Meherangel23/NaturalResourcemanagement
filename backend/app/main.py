from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .routers import design_tool, chatbot, contact
import os

app = FastAPI()

# CORS configuration
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(design_tool.router, prefix="/api")
app.include_router(chatbot.router, prefix="/api")
app.include_router(contact.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Natural Resource Management API"}

# This must be after all other routes
if os.path.exists("static"):
    app.mount("/", StaticFiles(directory="static", html=True), name="static")
