from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from sockets import sio_server

from api.db_manager import create_record, delete_record, list_records, list_filter_records, update_record

router = APIRouter()

@router.post("/create")
async def create_player(req: Request):
    try:
        request_body = await req.json()
        create_record("player", request_body)
        
        return JSONResponse(request_body)
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.post("/login")
async def create_player(req: Request):
    try:
        request_body = await req.json()
        result = list_filter_records("player", {'login':request_body['login'],'password':request_body['password']})
        
        return JSONResponse(result[0])
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.get('/get')
async def get_player(req: Request):
    try:
        request_body = await req.json()
        # Utiliser des filtres start et done
        result = list_filter_records('player',{'login':request_body['login']})

        # Traitement des résultats et renvoi de la réponse
        if result and len(result._responses) > 0:
            parties = result._responses[0].r
            return parties
        else:
            return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.post('/team_entrance')
async def player_team_entrance(req: Request):
    try:
        request_body = await req.json()
        sio_server.emit("TEAM_ENTRANCE", request_body)
        return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})
    