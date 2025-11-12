from client.server_client import client
import asyncio
from fastapi import FastAPI
import uvicorn
from route import router as api_router

app = FastAPI(
    title="Meducate _Client/Backend",
    description="This is the backend that handles the requests and logic for"
    "meducate backend",
)

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Meducate it"}


async def main():
    print("Hello from meducate_client!")
    async with client:
        await client.ping()
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


if __name__ == "__main__":
    asyncio.run(main())
