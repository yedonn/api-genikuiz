from datetime import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import re
import smtplib
import aiofiles
from typing import List
from fastapi import BackgroundTasks, File, UploadFile
from api.settings import Envs

# Chemin du dossier de stockage des fichiers
media_folder = "medias"
os.makedirs(media_folder, exist_ok=True)

def is_email(texte):
    # Modèle d'expression régulière pour la validation d'une adresse e-mail
    modele_email = r'^[\w\.-]+@[\w\.-]+(\.\w+)+$'

    # Utilisation de re.match() pour vérifier si la chaîne correspond au modèle d'adresse e-mail
    if re.match(modele_email, texte):
        return True
    else:
        return False

async def upload_file(dossier: str = "", file: UploadFile = File(...)):
    upload_folder = os.path.join(media_folder, dossier)
    os.makedirs(upload_folder, exist_ok=True)  # Crée le dossier s'il n'existe pas

    file_path = os.path.join(upload_folder, file.filename)
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(await file.read())
    return dict(filename=file.filename, filepath=file_path)    

def test_connection():
    try:
        # return Envs.MAIL_PORT
        server = smtplib.SMTP(Envs.MAIL_SERVER, Envs.MAIL_PORT)
        server.starttls()
        server.login(Envs.MAIL_USERNAME, Envs.MAIL_PASSWORD)
        server.quit()
        return True
    except smtplib.SMTPConnectError as e:
        print(f"SMTP Connection Error: {e}")
        return False
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
        return False
    except smtplib.SMTPException as e:
        print(f"SMTP Exception: {e}")
        return False