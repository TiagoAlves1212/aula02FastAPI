from fastapi import FastAPI
from models import Curso

# controllers

app = FastAPI()

@app.get('/')
async def root():
    return {"hello": "world"}


@app.get('/infinity')
async def infinity():
    return {"infinity": "school"}

@app.get('/meus-dados')
async def exibirDados():
    return     {
        "Nome": "Tiago",
        "idade": 17,
        "profissão": "developer"
    }


cursos = [
    {
        "codigo": 1,
        "nome": "python",
        "cargaHoraria": 100,
        "disponivel": True,
        "notaCorte": 7.5
    },
    
    {
        "codigo": 2,
        "nome": "javascript",
        "cargaHoraria": 50,
        "disponivel": False,
        "notaCorte": 6
    }
]

@app.get('/cursos')
async def getCursos():
    return cursos


# Trabalhando com path params
@app.get('/cursos/{curso_id}')
async def getCursoById(curso_id: int):
    for curso in cursos:
        if curso['codigo'] == curso_id:
            return curso

    return {"erro": "curso não encontrado"}


@app.get('/cursos-by-nota')
async def getCursoByNota(nota: float):
    resultado = []
    for curso in cursos:
        if curso['notaCorte'] >= nota:
            resultado.append(curso)


    return resultado

# post = enviar

@app.post('/cursos')
async def addCurso(curso: Curso):
    cursos.append(curso)
    return {"sucess": "ok"}

# put = alterar/editar
@app.put('/cursos/{curso_id}')
async def editCurso(curso_id: int, curso: Curso):
    for c in cursos:
        if c['codigo'] == curso_id:
            c['nome'] = curso.nome
            c['cargaHoraria'] = curso.cargaHoraria
            c['notaCorte'] = curso.notaCorte
            c['disponivel'] = curso.disponivel
            return c
    
    return {"Erro": "Curso não encontrado!"}

# delete = deletar


@app.delete('/cursos/{curso_id}')
async def deleteCurso(curso_id: int):
    for curso in cursos:
        if curso['codigo'] == curso_id:
            cursos.remove(curso)
            return {"success": "ok"}

    return {"erro": "true"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', reload=True, port=8000)