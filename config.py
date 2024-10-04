from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = 8143727
API_HASH = "e2e9b22c6522465b62d8445840a526b1"
BOT_TOKEN = "7838707055:AAFQGT34pjPbjqZzo9LyaleBNDD-QpFFZII"

MONGO_DB_URI = "mongodb+srv://friendakouseimanu:nGm1RUSjMwKPC96G@cluster0.1trpq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

INDEX_ID = int(getenv("-1002440194508"))
UPLOADS_ID = int(getenv("-1002448258068"))

STATUS_ID = 2
SCHEDULE_ID = 3

CHANNEL_TITLE = getenv("Anime Upload Main")
INDEX_USERNAME = getenv("AnimeUploadIndex")
UPLOADS_USERNAME = getenv("animeupmain")
