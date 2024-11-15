# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "17995671"))
API_HASH = getenv("API_HASH", "37adac03f1c113a3126b1f9eea32aff4")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "7464865613"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://fiona171593:tbGMvepmKQ8YNfJy@cluster0.5ccbrkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002499315195"))
FORCESUB = getenv("FORCESUB", "")
