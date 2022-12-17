import os


class Config(object):
    API_HASH = "6136c4d25def575624a2baa83d022826"
    BOT_TOKEN = "5665068184:AAHVy9pPeIsMnd7cSXcaq4X3OuKYggY2ydQ"
    TELEGRAM_API = "27168211"
    OWNER = "5674750841"
    OWNER_USERNAME = "@Ayankojiko"
    PASSWORD = "12345"
    DATABASE_URL = os.environ.get("DATABASE_URL")
    LOGCHANNEL = "-1001871188394"
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
