from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import helper as hp

import importlib
importlib.reload(hp)

app = FastAPI()

@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
def home():
    
    return "HOLAMUNDO"

@app.get(path = '/developer',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el nombre del desarrollador en el box abajo.<br>
                        3. Scrollear a "Resposes" para ver la cantidad de items y porcentaje de contenido Free por año de ese desarrollador.
                        </font>
                        """,
         tags=["Consultas Generales"])
def developer(desarrollador: str = Query(..., 
                            description="Desarrollador del videojuego", 
                            example='Valve')):
    return hp.developer_info(desarrollador)


# @app.get(path = '/userdata')
# def userdata(User_id:str):
#     return hp.userdata(User_id)


# @app.get(path = '/UserForGenre')
# def UserForGenre(genero:str):
#     return hp.UserForGenre(genero)


# @app.get(path = '/BestDeveloperYear')
# def best_developer_year(año:int):
#     return hp.best_developer_year(año)


# @app.get(path = '/DeveloperReviewsAnalysis')
# def developer_reviews_analysis(desarrolladora:str):
#     return hp.developer_reviews_analysis(desarrolladora)


# @app.get(path = '/RecomendacionJuego')
# def recomendacion_juego(id_producto):
#     return hp.recomendacion_juego(id_producto)


# @app.get(path = '/RecomendacionJuegoUsuario')
# def recomendacion_usuario(id_usuario):
#     return hp.recomendacion_usuario(id_usuario)