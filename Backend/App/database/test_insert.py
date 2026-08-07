from app.database.connection import SessionLocal
from app.repositories.market_repository import MarketRepository

db = SessionLocal()

repo = MarketRepository(db)

market = repo.create_market(
    market_name="Agra",
    state="Uttar Pradesh",
    district="Agra",
)

print(market.id, market.market_name)

db.close()