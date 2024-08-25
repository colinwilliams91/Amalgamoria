from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

gemini_api = os.getenv("GEMINI_API")
genai.configure(api_key=gemini_api)
model = genai.GenerativeModel('gemini-1.5-flash')

router = APIRouter()

# Takes form data (user_input) as input.
# The Form(...) part indicates that user_input is expected to come from a form submission and is required.
@router.post("/gemini")
async def post_gemini(user_input: str = Form(...)):
    response_data = model.generate_content(user_input)
    # Return the generated content as a JSON response
    return JSONResponse(content={"response": response_data.text})
