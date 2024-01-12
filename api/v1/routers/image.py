from fastapi import File, Request, APIRouter, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from api.util import upload_file
from sockets import sio_server

from api.db_manager import create_record, delete_record, list_records, list_filter_records, update_record

router = APIRouter()

@router.post("/upload")
async def image_upload(fichier: UploadFile = File(...)):
    try:
        upload_file("genikuiz", fichier)
        
        return JSONResponse({'status':200, 'item':{'imageurl':fichier.filename}})
    except Exception as e:
        return JSONResponse({'detail':f'Une erreur s\'est produite: {str(e)}'})

@router.get('/{upload}')
async def get_image(upload: str):
    file_path = f'./images/{upload}'
    return FileResponse(file_path, media_type='image/png')