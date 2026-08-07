from pydantic import BaseModel


class DashboardRequest(BaseModel):

    state_id: int
    district_id: int
    commodity_id: int

    variety_id: int = 100021
    grade_id: int = 4

    date: str