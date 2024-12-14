import os
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()

db = create_engine(os.getenv('DATABASE_URL'))
base = declarative_base()

Session = sessionmaker(db)
session = Session()


class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    password = Column(String(255), nullable=False)

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)
