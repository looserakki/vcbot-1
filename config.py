from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCHcn6tT2UQMXWCbmofjPfItgokteMHDX2CQvXQocPe2ptqI8btRfsZABD_9tRLnJ1BhppSn4H4Hz5wuUbTx8Ia8n5OLmSQCm2crHVmAHs_yARdrs8UhvUlByMCGbiMTSO64XRfAC4xkSoeLsmuy9JVntg_iXc8A3Ktc-IoS2wyhTB0ZgwGRUe9Zob9x1D84r-gGr8ozMl9MvdasEeV9UKaI2N5nfFy3HzSpZdHwe3tNMzra37V1mbz14wciRaX7htMA-G52RmDP2LEQ0KxK_6gJhnWcfss5HXZfcd-RS9Q-PSwxHhDyArrwJV3kVWdNb6ZXceVqCJpUH-TzG5h5xw1b4g4gQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1795262909:AAEXNquVqPyXI8gtaBpUcElXE6WZJW8_eAU")
BOT_NAME = getenv("BOT_NAME", "AKKI-MUSIX")
admins = {}
API_ID = int(getenv("API_ID", "6285038"))
API_HASH = getenv("API_HASH", "cea8174655dfd00fb51f91f8493e55ee")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "800898218 1801516703 1832447570 936481432").split()))
