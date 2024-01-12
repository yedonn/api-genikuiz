import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routers.index import router as v1_router
from fastapi.staticfiles import StaticFiles

from sockets import sio_app

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title=os.environ.get("APP_NAME"))

# Montage du répertoire "media" pour servir les fichiers statiques
app.mount("/medias", StaticFiles(directory="medias"), name="medias")

app.include_router(v1_router)
app.mount('/', app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# origins = [
#    "http://192.168.211.:8000",
#    "http://localhost",
#    "http://localhost:3005",
#    "http://localhost:8080",
#    "http://localhost:8000",
#    "ws://localhost:8000",
# ]

# app.add_middleware(
#    CORSMiddleware,
#    allow_origins=origins,
#    allow_credentials=True,
#    # allow_origins=["*"],
#    allow_methods=["*"],
#    allow_headers=["*"],
# )


if __name__ == "__main__":
   uvicorn.run("main:app", reload=True, port=3000)