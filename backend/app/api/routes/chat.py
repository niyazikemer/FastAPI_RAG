# backend/app/api/routes/chat.py
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Get template path similar to email templates approach
# Get template path relative to Docker container structure
TEMPLATE_DIR = Path(__file__).parent.parent.parent / "templates"
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))

router = APIRouter(prefix="/chat", tags=["chat"])

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@router.post("/send")
async def send_message(message: str = Form(...)):
    return HTMLResponse(f"<p class='bg-gray-100 rounded-lg p-3'>{message}</p>")