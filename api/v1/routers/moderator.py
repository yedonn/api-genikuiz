from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from sockets import sio_server

from api.db_manager import create_record, delete_record, list_records, list_filter_records, update_record

router = APIRouter()

@router.post("/create")
async def create_moderator(req: Request):
    try:
        request_body = await req.json() 
        create_record("moderator", request_body)
        return JSONResponse(request_body)
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.post("/login")
async def create_moderator(req: Request):
    try:
        request_body = await req.json()
        result = list_filter_records("moderator", {'login':request_body['login'],'password':request_body['password']})
        
        return JSONResponse(result[0])
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})
      