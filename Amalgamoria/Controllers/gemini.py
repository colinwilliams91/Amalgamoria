from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
import google.generativeai as genai
from Controllers.prompt import Prompt

load_dotenv()

gemini_api = os.getenv("GEMINI_API")
genai.configure(api_key=gemini_api)
model = genai.GenerativeModel('gemini-1.5-flash')


router = APIRouter()
prompt_generator = Prompt()

# Takes form data (user_input) as input.
# The Form(...) part indicates that user_input is expected to come from a form submission and is required.
# user_input is not used for not, but keeping it in incase its helpful later
@router.post("/gemini")
async def post_gemini(user_input: str = Form(...)):
    prompt = prompt_generator.create_prompt()
    response_data = model.generate_content(prompt)
    # Return the generated content as a JSON response
    return JSONResponse(content={"response": response_data.text})
