# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "17995671"))
API_HASH = getenv("API_HASH", "37adac03f1c113a3126b1f9eea32aff4")
BOT_TOKEN = getenv("BOT_TOKEN", "7732713943:AAEDN8svoL-aZbZQ-egF1wctQ1JYfnJHJX4")
OWNER_ID = int(getenv("OWNER_ID", "7464865613"))
MONGODB_CONNECTION_STRING = getenv("mongodb+srv://smallcapitaltrader1:XVsdQj8vu38ZIFoy@cluster0.9g3ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002499315195"))
FORCESUB = getenv("FORCESUB", "https://t.me/+kkYNlMJCEP9hNjNl")
