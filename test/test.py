from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os

app = FastAPI()
count = 0
hostname = os.getenv("NODE_NAME", "unknown")

@app.get("/", response_class = HTMLResponse)
async def hello(request: Request):
    global count
    count += 1

    html = f"""
    <html>
        <head><title>Hello from {hostname}</title></head>

        <body style="font-family:sans-serif; text-align:center; padding-top:3em;">
            <h1>👋 Hello, world!</h1>

            <p>🐳 Served from pod: <strong>{hostname}</strong></p>

            <p>📊 Visitor number: <strong>{count}</strong></p>
            
            <p>🌐 Your IP: <strong>{request.client.host}</strong></p>
        </body>
    </html>
    """
    
    return HTMLResponse(content = html)
