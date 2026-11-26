from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL ="postgresql+psycopg2://fruitinventory_user:ECZr3nkIg8yL8vP1CYUyOq1cVIcVGP61@dpg-dc3qgj6i0phs7388io5g-a.oregon-postgres.render.com/fruitinventory"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
