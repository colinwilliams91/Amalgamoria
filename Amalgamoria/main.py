import sys
import os
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from Controllers.gemini import router as gemini_router
from Controllers.websockets_routes import router as websocket_router

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI()
templates = Jinja2Templates(directory="Views")

# Include the routers
app.include_router(gemini_router, prefix="/api")
app.include_router(websocket_router)  # Include the WebSocket router

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
