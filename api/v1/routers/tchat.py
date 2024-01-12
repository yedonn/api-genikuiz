import uuid
from fastapi import APIRouter,Request, WebSocket

from fastapi.responses import JSONResponse

from api.db_manager import create_record, delete_record, list_records

router = APIRouter()

# Route pour se connecter au chat
@router.post("/chat")
async def connect_to_chat(request: Request, user_id: str):
    # Obtenez l'identifiant de l'utilisateur
    # user_id = request.headers["user-id"]

    # Créez une nouvelle connexion WebSocket
    connection = WebSocket(request)

    # Ajoutez la connexion à la liste des connexions actives
    create_record('chat', {"user_id": user_id, "connection": connection.id})

    # Envoyez un message de bienvenue à l'utilisateur
    await connection.send_text("Bienvenue dans le chat !")

    # Renvoyez un message de confirmation à l'utilisateur
    return JSONResponse({"status": "ok"})


# Route pour envoyer un message
@router.post("/chat/message")
async def send_message(request: Request, user_id: str):
    # Obtenez l'identifiant de l'utilisateur
    # user_id = request.headers["user-id"]

    # Obtenez le message
    message = request.json["message"]

    # Enregistrez le message dans la base de données
    connection_id = str(uuid.uuid4())
    create_record('chat', {"user_id": user_id, "message": message})

    # Envoyez le message à tous les utilisateurs connectés
    for connection in list_records('chat', {"user_id": {"$ne": user_id}}):
        await connection["connection"].send_text(message)

    return JSONResponse({"status": "ok"})


# Route pour se déconnecter du chat
@router.post("/chat/disconnect")
async def disconnect_from_chat(request: Request, user_id: str):
    # Obtenez l'identifiant de l'utilisateur
    # user_id = request.headers["user-id"]

    # Supprimez la connexion de la base de données
    delete_record('chat', {"user_id": user_id})

    return JSONResponse({"status": "ok"})


# Gestion des événements WebSocket
@router.websocket("/chat/ws")
async def chat_ws(websocket: WebSocket, user_id: str):
    # Obtenez l'identifiant de l'utilisateur
    # user_id = websocket.headers["user-id"]

    # Ajoutez la connexion à la base de données
    connection_id = str(uuid.uuid4())
    create_record("chat", {"user_id": user_id, "connection": connection_id})

    # Attendez que le client se connecte
    await websocket.accept()

    # Boucle infinie pour recevoir des messages
    while True:
        # Attendez un message
        message = await websocket.receive()

        # Si le message est une demande de déconnexion
        if message == "close":
            # Supprimez la connexion de la base de données
            delete_record('chat', {"user_id": user_id})

            # Fermez la connexion
            await websocket.close()
            break

        # Sinon, enregistrez le message dans la base de données
        create_record('chat', {"user_id": user_id, "message": message})

        # Envoyez le message à tous les utilisateurs connectés
        for connection in list_records('chat', {"user_id": {"$ne": user_id}}):
            await connection["connection"].send_text(message)