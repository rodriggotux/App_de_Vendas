from fastapi import FastAPI
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.banco.repositorios import RepositorioPordutos


app = FastAPI()

@app.get('/')
def home():
    return f'Deu certo'

@app.post('/produtos')
def criar_produtos(product:Product,db: Session):
    product_create = RepositorioProdutos().criar(produtos)
    return product_create

@app.get('/produtos')
def listar_produtos():
    return f'Lista de Produtos'

