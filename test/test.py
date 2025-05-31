from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import os
import subprocess

app = FastAPI()
count = 0
hostname = os.getenv("NODE_NAME", "unknown")


@app.get("/", response_class = HTMLResponse)
async def hello():
    global count
    count += 1

    html = f"""
        <html>
            <head>
                <title>Hello from {hostname}</title>
            </head>
            
            <body style="font-family:sans-serif; text-align:center; padding-top:3em">
                <h1>👋 Hello, world!</h1>

                <p>🐳 Served from node: <strong>{hostname}</strong></p>
                
                <p>📊 Visitor number: <strong>{count}</strong></p>

                <form onsubmit="sendLoadRequest(event)">
                    <label>⏱️ CPU Load</label>

                    <input type="number" id="duration" name="duration" min="1" max="300" value="60">

                    <input type="submit" value="Commit">
                </form>
            </body>
        </html>
        """

    return HTMLResponse(content = html)


@app.post("/load", response_class = HTMLResponse)
async def load(duration: int = Form(...)):
    cpus = os.cpu_count() or 1

    try:
        subprocess.Popen(
            ["stress", "--cpu", str(cpus), "--timeout", str(duration)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        result = f"✅ Started stress with {cpus} CPUs for {duration} seconds"
    except Exception as e:
        result = f"❌ Failed to start stress: {e}"

    html = f"""
        <html>
            <body style="font-family:sans-serif; text-align:center; padding-top:3em">
                <p>{result}</p>

                <p><a href="/">Back</a></p>
            </body>
        </html>
        """

    return HTMLResponse(content = html)
