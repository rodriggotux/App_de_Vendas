from sqlalchemy import Boolean, Column, Foreignkey, Integer, String
from src.infra.banco.config.database import Base
#from sqlalchemy.orm import relationship


class Product(Base):
    
    __tablename__ = 'produtos'
    
    id = Column(Interger, primary_key=True, index=True)
    user = Column(String)
    detail = Column(String)
    price = Column(Float)
    availabel = Column(Boolean, default=Flase)
