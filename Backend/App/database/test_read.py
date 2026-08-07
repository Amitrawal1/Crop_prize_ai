from app.database.connection import SessionLocal
from app.models.market import Market

db = SessionLocal()

markets = db.query(Market).all()

for market in markets:
    print(
        market.id,
        market.market_name,
        market.state,
        market.district,
    )

db.close()