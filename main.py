from fastapi import FastAPI
from browser_use import Agent
import asyncio

app = FastAPI()

@app.get("/run")
async def run_task(task: str):
    agent = Agent()
    result = await agent.run(task)
    return {"result": result}

@app.get("/health")
async def health():
    return {"status": "ok"}