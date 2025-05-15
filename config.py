"""
from os import getenv


API_ID = int(getenv("API_ID", "18116358"))
API_HASH = getenv("API_HASH", "80e7597f27a57df271dfc500120d4ea9")
BOT_TOKEN = getenv("BOT_TOKEN", "7594405866:AAF527H4zrRubxeLfS_mAfOIgu_idqG9MsM")
OWNER_ID = int(getenv("OWNER_ID", "7836088695"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5637668210").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002385747075"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002385747075"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "18116358"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "80e7597f27a57df271dfc500120d4ea9")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7594405866:AAF527H4zrRubxeLfS_mAfOIgu_idqG9MsM")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7836088695"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5637668210").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002385747075"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://mrnobody:modernhackers@mrnobody.q8e87ij.mongodb.net/?retryWrites=true&w=majority&appName=MrNobody")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002385747075"))

