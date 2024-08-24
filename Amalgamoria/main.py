import sys
import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

from Controllers.gemini import model

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI()
templates = Jinja2Templates(directory="Views")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def handle_input(request: Request, user_input: str = Form(...)):
    response_data = model.generate_content(user_input)
    return templates.TemplateResponse("index.html", {"request": request, "response_data": response_data.text})