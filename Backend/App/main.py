from fastapi import FastAPI

from app.api.routes.state import router as state_router
from app.api.routes.district import router as district_router
from app.api.routes.market import router as market_router
from app.api.routes.commodity import router as commodity_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.routes.filters import router as filters_router

app = FastAPI(
    title="Crop Price AI API",
)

app.include_router(state_router)
app.include_router(district_router)
app.include_router(market_router)
app.include_router(commodity_router)
app.include_router(dashboard_router)
app.include_router(filters_router)


@app.get("/")
def root():

    return {
        "message": "Crop Price AI Backend Running"
    }