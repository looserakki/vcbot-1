from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCt3YwFqx71ynNNHviUmQ2BeriDRLvH8Qvt6cXe8dtrfb-rD_8-5l1GXy0zZNdZ3wEjH_OxSKaxTCo8N3y0gSCiZPhHxIr8PEhBxbkXlB-LoMe1ruJCPdZc45BsRwSPKya0ojNNt_PGsI5-ETLKh_L6DIeXnKpp1Fh1mCBnKjfTZ7SCONfR9DLWSMk0AnmPJ7EARDEqstBjwCjFrs_6vrOEATC_6n16xqVVH8KIZZMEY4xwvfcqppX5jEiuSo6H1bdgyIxmC1J-LvRV-cUHtene0GKFTyeBkyedsdzmP23w6eIPiWyYyus0ETV1Q6_8x1D_0dZdvj0jSQS0RCkON1Jnb4g4gQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1795262909:AAEXNquVqPyXI8gtaBpUcElXE6WZJW8_eAU")
BOT_NAME = getenv("BOT_NAME", "AKKI-MUSIX")
admins = {}
API_ID = int(getenv("API_ID", "6285038"))
API_HASH = getenv("API_HASH", "cea8174655dfd00fb51f91f8493e55ee")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "800898218 1801516703 1832447570 936481432").split()))
