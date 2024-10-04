from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("8143727"))
API_HASH = getenv("e2e9b22c6522465b62d8445840a526b1")
BOT_TOKEN = getenv("7838707055:AAFQGT34pjPbjqZzo9LyaleBNDD-QpFFZII")

MONGO_DB_URI = getenv("mongodb+srv://peacefulwolfdev:jR9mR92gQC1QhpdZ@cluster0.jbkwr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

INDEX_ID = int(getenv("-1002440194508"))
UPLOADS_ID = int(getenv("-1002448258068"))

STATUS_ID = int(getenv("2"))
SCHEDULE_ID = int(getenv("3"))

CHANNEL_TITLE = getenv("Anime Upload Main")
INDEX_USERNAME = getenv("AnimeUploadIndex")
UPLOADS_USERNAME = getenv("animeupmain")
