import os
if os.environ.get("DEV"):
    print('Debug/Development mode')

### BOT CONFIGURATION ###
MODERATORS = [62056065, 918962, 7679610, 278941742, 127782573, 43740047, 353341197]
ADMINS = [62056065, 918962]
BOT_CONSIDERED_NEW = 14  # days
SELF_BOT_NAME = "josxasandboxbot" if bool(os.environ.get("DEV")) else "botlistbot"
SELF_BOT_ID = "182355371" if bool(os.environ.get("DEV")) else "265482650"
BOTLISTCHAT_ID = -1001118582923 if bool(os.environ.get("DEV")) else -1001067163791
SELF_CHANNEL_USERNAME = "botlist_testchannel" if bool(os.environ.get("DEV")) else "botlist"
REGEX_BOT_IN_TEXT = r'.*(@[a-zA-Z0-9_]{3,31}).*'
REGEX_BOT_ONLY = r'(@[a-zA-Z0-9_]{3,31})'
PAGE_SIZE_SUGGESTIONS_LIST = 5
PAGE_SIZE_BOT_APPROVAL = 5
MAX_SEARCH_RESULTS = 25
MAX_BOTS_PER_MESSAGE = 140
BOT_ACCEPTED_IDLE_TIME = 2  # minutes
SUGGESTION_LIMIT = 25
