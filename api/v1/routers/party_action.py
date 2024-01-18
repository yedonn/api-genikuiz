from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from sockets import sio_server

from api.db_manager import create_record, delete_record, list_records, list_filter_records, update_record

router = APIRouter()

@router.post("/create")
async def create_party_action(req: Request):
    try:
        request_body = await req.json()
        create_record("party_action", request_body)
        if request_body['party_action'] == 1:
            await sio_server.emit("action_change")
        else:
            await sio_server.emit("action_change_done")
        
        return JSONResponse(request_body)
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})
     
@router.post('/update')
async def update_party_action(req: Request):
    try:
        request_body = await req.json()
        result = update_record('party',{'id':request_body['id']},request_body)
        if request_body['party_action'] == 1:
            await sio_server.emit("action_change")
        else:
            await sio_server.emit("action_change_done")
        # Traitement des résultats et renvoi de la réponse
        if result and len(result) > 0:
            parties = result[0]
            return parties
        else:
            return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.get('/get')
async def get_party_action(req: Request):
    try:
        # Utiliser des filtres start et done
        result = list_records('party_action')

        # Traitement des résultats et renvoi de la réponse
        if result and len(result) > 0:
            parties = result[0]
            return parties
        else:
            return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})