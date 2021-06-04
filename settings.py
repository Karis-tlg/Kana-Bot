import os
from dotenv import load_dotenv

# For non-replit env
load_dotenv()


# Any extension here can be loaded by the bot owner using
# the admin ext
ALL_EXTENSIONS = {
    # "extension path": enabled?
    'extensions.admin': True,

    'extensions.encouragements': True,
    'extensions.economy': True,

    'extensions.greetings': True,
}

# Only enabled extensions are loaded in main.py
EXTENSIONS = [extension for extension, enabled in ALL_EXTENSIONS.items() if enabled]

TOKEN = os.getenv('TOKEN')

COMMAND_PREFIX = '$'

BOT_OWNER_ID = os.getenv('BOT_OWNER_ID')
