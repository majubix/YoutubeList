from googleapiclient.discovery import build
API_KEY = 'AIzaSyBNeKHZ1pCylcWDHSurWugdQGm5uiwWon8'

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