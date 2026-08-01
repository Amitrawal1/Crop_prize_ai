from fastapi import FastAPI

from app.api.routes.state import router as state_router

app = FastAPI(
    title="Crop Price AI API",
)

app.include_router(state_router)


@app.get("/")
def root():

    return {
        "message": "Crop Price AI Backend Running"
    }