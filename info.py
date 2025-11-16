from pyrogram import Client
import re
from os import environ
from dotenv import load_dotenv
from Script import script
import time

# load_dotenv("./config.env")
load_dotenv("./dynamic.env", override=True)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Required API Credentials and Bot Settings
API_ID = "24135304"
API_HASH = "7bdcc6969ab723de66b02e64897b7184"
BOT_TOKEN = "6097583676:AAFIy9n4RALDt7US2xiyvjSby5NzuXh9HUQ"
BOT_USERNAME = "BF_SeriesBot"
#API_ID2 = environ['API_ID2']
#API_HASH2 = environ['API_HASH2']
#SESSION_STRING = environ['SESSION_STRING']

# Required Database and Channel Settings
DATABASE_URI = "mongodb+srv://SeriesDB1:SeriesDB1@cluster0.gqsvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "BF_Seri"
COLLECTION_NAME = "BF_si"
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6774015826 6773883939').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
AUTH_CHANNEL = "-1003455797823"
REQ_CHANNEL = -1003455797823
LOG_CHANNEL = "-1002437916009"
DB_CHANNEL = [-1002619733276, -1002179921548]
RAW_DB_CHANNEL = [2619733276, 2179921548]
IMGBB_API_KEY = "2901c1bc3e891134d8adb2a7deb19488"
TMDB_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YWJhNTM3NTkzMjI1ODBmZTg1NGMxN2MxZWQyYTUwMCIsIm5iZiI6MTc1MTk3NDUwOS42MjQsInN1YiI6IjY4NmQwMjZkZTBkMzY1OTA4MDEwNDAyYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zNIWGhxysTDK7dxS_4_qQV0les_XfMCRyrV-tHNrFD4"

# Optional settings with defaults
SESSION = environ.get('SESSION', 'series')
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Required Media settings with defaults
STICKER = environ.get('STICKER', 'False')
STICKER_ID = environ.get('STICKER_ID', "CAACAgUAAxkBAAJ0w2aZJMdpnEKbXtDVPJIvpL2XhIAhAAIrAAO8ljUq9-AkUFoHiMQeBA")
PIC = environ.get('PIC', 'False')
PICS = environ.get('PICS', "https://envs.sh/PSI.jpg").split()

# Optional Bot messages and settings
START_TXT = environ.get('START_TXT', "Bot Started..! And its Up and Running..!")
NO_POSTER_FOUND_IMG = environ.get('NO_POSTER_FOUND_IMG', "https://ibb.co/Zz2dPZht").split()
SPELL_CHECK_IMAGE = environ.get('SPELL_CHECK_IMAGE', 'https://ibb.co/DPRyQYZT').split()
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{previouscaption}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", '{previouscaption}')
AUTO_DELETE_TIME = int(environ.get('AUTO_DELETE_TIME', 0))
AUTO_DELETE_MSG = environ.get('AUTO_DELETE_MSG', """<blockquote>❗️❗️❗️<u>IMPORTANT</u>❗️️❗️❗️

ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ 10 mins 🫥 <i>(ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs)</i>.

<b>ᴘʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs ᴏʀ ᴀɴʏ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ.</b></blockquote>""")
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "False"), False)
PORT = environ.get('PORT', "8080")

LONG_IMDB_DESCRIPTION = "True"
MAX_LIST_ELM = "8"
USE_CAPTION_FILTER = "False"
#userbot = Client("my_userbot", api_id=API_ID2, api_hash=API_HASH2, session_string=SESSION_STRING)
#userbot.start()
