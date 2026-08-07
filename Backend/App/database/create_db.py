from app.database.connection import Base
from app.database.connection import engine
from app.models.state import State
from app.models.district import District
from app.models.commodity_group import CommodityGroup
from app.models.commodity import Commodity
from app.models.dashboard_data import DashboardData
from app.models.price_history import PriceHistory


from app.models.market import Market

Base.metadata.create_all(bind=engine)

print("Database Created")