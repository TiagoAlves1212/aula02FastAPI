from pydantic import BaseModel

class Curso(BaseModel):
    codigo: int
    nome: str
    cargaHoraria: int
    disponivel: bool
    notaCorte: float