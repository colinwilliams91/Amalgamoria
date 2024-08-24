from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

gemini_api = os.getenv("GEMINI_API")
genai.configure(api_key=gemini_api)
model = genai.GenerativeModel('gemini-1.5-flash')

router = APIRouter()
templates = Jinja2Templates(directory="Views")

@router.get("/gemini")
async def get_gemini(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/gemini")
async def post_gemini(request: Request, user_input: str = Form(...)):
    response_data = model.generate_content(user_input)
    return templates.TemplateResponse("index.html", {"request": request, "response_data": response_data.text})
