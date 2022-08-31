from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produtos
from src.infra.banco.config.database import get_db
from src.infra.banco.repositorios import RepositorioPordutos


app = FastAPI()

@app.get('/')
def home():
    return f'Deu certo'

@app.post('/produtos')
def criar_produtos(product:Product,db: Session = Depends(get_db)):
    product_create = RepositorioProdutos().criar(product)
    return product_create

@app.get('/produtos')
def listar_produtos():
    return f'Lista de Produtos'

