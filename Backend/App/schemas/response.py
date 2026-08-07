from pydantic import BaseModel


class DashboardRecord(BaseModel):

    trend: str

    cmdt_name: str

    cmdt_grp_name: str

    msp_price: str

    as_on_price: str

    as_on_arrival: str

    reported_date: str

    one_day_ago_price: str

    two_day_ago_price: str

    one_day_ago_arrival: str

    two_day_ago_arrival: str


class DashboardResponse(BaseModel):

    status: bool

    message: str

    records: list[DashboardRecord]