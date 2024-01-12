from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from sockets import sio_server

from api.db_manager import create_record, delete_record, list_records, list_filter_records, update_record

router = APIRouter()

@router.post("/create")
async def create_party(req: Request):
    try:
        request_body = await req.json()
        create_record("party", request_body)
        
        if request_body['update_action']:
            if request_body['update_action'] == 'update_return_menu':
                await sio_server.emit("update_return_menu")
            elif request_body['update_action'] == 'update_game_info':
                await sio_server.emit("update_game_info")
            elif request_body['update_action'] == 'update_restart_match':
                await sio_server.emit("update_restart_match")
            else:
                print('default')
        
        return JSONResponse(request_body)
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.post("/getAll")
async def get_all_parties(req: Request):
    try:
        request_body = await req.json()
        # Construire la requête en fonction des filtres reçus
        if request_body['start'] is None or request_body['done']is None:
            # Pas de filtres, récupérer toutes les parties
            result = list_records("party")
        else:
            # Utiliser des filtres start et done
            result = list_filter_records('party',{'start':request_body['start'], 'done':request_body['done']})

        # Traitement des résultats et renvoi de la réponse
        if result and len(result._responses) > 0:
            parties = result._responses[0].r
            return parties
        else:
            return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.get('/get')
async def get_party(req: Request):
    try:
        # Utiliser des filtres start et done
        result = list_filter_records('party',{'start':True, 'done':False})

        # Traitement des résultats et renvoi de la réponse
        if result and len(result._responses) > 0:
            parties = result._responses[0].r
            return parties
        else:
            return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})
    
@router.get('/getDone')
async def get_done_party(req: Request):
    try:
        # Utiliser des filtres start et done
        result = list_filter_records('party',{'start':True, 'done':True})

        # Traitement des résultats et renvoi de la réponse
        if result and len(result._responses) > 0:
            parties = result._responses[0].r
            return parties
        else:
            return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})
    
@router.get('/getInfo')
async def get_done_party(req: Request):
    try:
        request_body = await req.json()
        # Utiliser des filtres start et done
        result = list_filter_records('party',{'id':request_body['id']})

        # Traitement des résultats et renvoi de la réponse
        if result and len(result._responses) > 0:
            parties = result._responses[0].r
            return parties
        else:
            return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})
    
@router.post('/update')
async def update_party(req: Request):
    try:
        request_body = await req.json()
        update_action = request_body['update_action']
        request_body['update_action'] = None;
        
        # Utiliser des filtres start et done
        result = update_record('party',{'id':request_body['id']},request_body)

        # Traitement des résultats et renvoi de la réponse
        if result and len(result._responses) > 0:
            parties = result._responses[0].r
            return parties
        else:
            return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.post('/start_match')
async def start_match_party(req: Request):
    try:
        request_body = await req.json()
        sio_server.emit("START_MATCH", request_body)
        return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.post('/match_over')
async def match_over_party(req: Request):
    try:
        request_body = await req.json()
        sio_server.emit("MATCH_OVER", request_body)
        return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})
    
@router.post('/match_cancel')
async def match_cancel_party(req: Request):
    try:
        request_body = await req.json()
        sio_server.emit("MATCH_CANCEL", request_body)
        return []
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})
    