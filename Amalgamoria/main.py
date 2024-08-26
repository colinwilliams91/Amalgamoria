import sys
import os
import redis


from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from Amalgamoria.Controllers.gemini import router as gemini_router
from Amalgamoria.Controllers.websockets_routes import router as websocket_router

from Amalgamoria.store import store

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI()

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Check Redis connection
try:
    response = redis_client.ping()
    if response:
        print("Redis is connected and responding.")
    else:
        print("Redis is not responding.")
except redis.ConnectionError:
    print("Could not connect to Redis. Check your connection settings.")

# Serve static file from the 'Views' directory
app.mount("/static", StaticFiles(directory="Amalgamoria/Views"), name="static")

# Include the routers
app.include_router(gemini_router, prefix="/api")
app.include_router(websocket_router)  # Include the WebSocket router

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Serve the index.html file from the static directory
    with open("Amalgamoria/Views/index.html") as f:
         # Read the content of the file and return it as an HTML response
        return HTMLResponse(content=f.read())

@app.post("/username")
async def submit_username(username: str = Form(...), user_id: int = Form(...)):
    # Store the submitted username
    obj = { user_id: user_id, username: username }
    store["users"].append(obj)

    # TODO: look up common design patterns for building up HTML in server response
    # response = FileResponse("Amalgamoria/Views/Templates/username.html")
    with open("Amalgamoria/Views/Templates/username.html", "r+") as f:
        html = f.read()
        html = html.replace("{{dingus}}", username)
        return HTMLResponse(html)

@app.get("/lobby")
async def index():
    with open("Amalgamoria/Views/Templates/lobbies.html") as f:
        html = f.read()
        return HTMLResponse(html)
