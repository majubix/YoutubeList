import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY não encontrada. Verifique o arquivo .env.")


youtube = build('youtube','v3', developerKey=API_KEY)

CANAL_ID = 'UC__dSYOfZ8QnGLiYes82D_A'

def get_youtube_client():
    return build('youtube', 'v3', developerKey=API_KEY)

def listar_subscript():
    youtube = get_youtube_client()
    request = youtube.subscriptions().list(
        part='snippet',
        channelId=CANAL_ID,
        maxResults=20,
        order='relevance'
    )
    response = request.execute()

    for item in response.get('items',[]):
        nome = item['snippet']['title']
        canal = item['snippet']['resourceId']['channelId']
        print(f'{nome} - Canal ID: {canal}')

listar_subscript()