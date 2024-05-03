from fastapi import FastAPI

import models
from database import engine
models.Base.metadata.create_all(bind=engine)

from board import board_router

app = FastAPI()

app.include_router(board_router.app, tags=["board"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)