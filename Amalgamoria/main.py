import sys
import os
import redis

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from Controllers.gemini import router as gemini_router
from Controllers.websockets_routes import router as websocket_router

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
app.mount("/static", StaticFiles(directory="Views"), name="static")

# Include the routers
app.include_router(gemini_router, prefix="/api")
app.include_router(websocket_router)  # Include the WebSocket router

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Serve the index.html file from the static directory
    with open("Views/index.html") as f:
         # Read the content of the file and return it as an HTML response
        return HTMLResponse(content=f.read())

@app.post("/test")
def test():
    return