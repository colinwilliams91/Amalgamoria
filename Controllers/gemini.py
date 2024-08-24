import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

gemini_api = os.getenv("GEMINI_API")
genai.configure(api_key=gemini_api)
model = genai.GenerativeModel('gemini-1.5-flash')