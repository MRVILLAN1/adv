# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "10000844"))
API_HASH = getenv("API_HASH", "776f257fc1d1f8aa4aea9dd35d10a45b")
BOT_TOKEN = getenv("BOT_TOKEN", "6743648885:AAFGGf9BjIiXf-dTKWss2ocn-UgkUIZOGJY")
OWNER_ID = int(getenv("OWNER_ID", "6750546542"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://fiona171593:tbGMvepmKQ8YNfJy@cluster0.5ccbrkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1004530635818"))
FORCESUB = getenv("FORCESUB", "funnyzilla")
