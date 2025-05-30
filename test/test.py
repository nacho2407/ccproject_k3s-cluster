from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import os
import subprocess

app = FastAPI()
count = 0
hostname = os.getenv("NODE_NAME", "unknown")

@app.get("/", response_class = HTMLResponse)
async def hello(request: Request):
    global count
    count += 1

    html = f"""
    <html>
        <head>
            <title>Hello from {hostname}</title>
        </head>
        
        <body style="font-family: sans-serif; text-align: center; padding-top: 3em">
            <h1>👋 Hello, world!</h1>

            <p>🐳 Served from node: <strong>{hostname}</strong></p>
            
            <p>📊 Visitor number: <strong>{count}</strong></p>

            <form action="/load" method="post">
                <label>⏱️ 몇 초간 CPU 로드를 줄까요? </label>

                <input type="number" name="duration" min="1" max="300" value="180">
                
                <input type="submit" value="Load 시작">
            </form>
        </body>
    </html>
    """

    return HTMLResponse(content=html)

@app.post("/load")
async def load(duration: int = Form(...)):
    cpus = (os.cpu_count() - 1) or 1

    try:
        subprocess.Popen(
            ["stress", "--cpu", str(cpus), "--timeout", str(duration)],
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL
        )
        result = f"✅ Started stress with {cpus} CPUs for {duration} seconds"
    except Exception as e:
        result = f"❌ Failed to start stress: {e}"
