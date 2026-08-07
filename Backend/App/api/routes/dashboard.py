from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.response import DashboardResponse

from app.api.dependencies import get_db
from app.schemas.dashboard import DashboardRequest
from app.services.dashboard.service import DashboardService
from app.services.dashboard.formatter import format_dashboard_response

router = APIRouter()


@router.post(
    "/dashboard",
    response_model=DashboardResponse,
    )

def get_dashboard(
    request: DashboardRequest,
    db: Session = Depends(get_db),
):

    service = DashboardService(db)

    data = service.get_dashboard(
        state_id=request.state_id,
        district_id=request.district_id,
        commodity_id=request.commodity_id,
        variety_id=request.variety_id,
        grade_id=request.grade_id,
        request_date=request.date,
    )
    return format_dashboard_response(data)