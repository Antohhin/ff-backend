from enum import Enum
from src.storage.constants import Language


DEFAULT_USER_LANGUAGE = Language.EN


class UserType(str, Enum):    
    USER = "user"
    ACTIVE_USER = "active_user"
    SUPER_USER = "super_user"

    GHOSTED = "ghosted"  # ignoring the bot
    BLOCKED_BOT = "blocked_bot"

    MODERATOR = "moderator"


class Reaction(int, Enum):
    LIKE = 1
    DISLIKE = 2



MEME_BUTTON_CALLBACK_DATA_PATTERN = "r:{meme_id}:{reaction_id}"
MEME_BUTTON_CALLBACK_DATA_REGEXP = "^r:"

MEME_QUEUE_IS_EMPTY_ALERT_CALLBACK_DATA = "q:empty"

LOADING_EMOJIS = [
    "🕛", "🕧", "🕐", "🕜", "🕑", "🕝",
    "🕒", "🕞", "🕓", "🕟", "🕔", "🕠", 
    "🕕", "🕡", "🕖", "🕢", "🕗", "🕣", 
    "🕘", "🕤", "🕙", "🕥", "🕚", "🕦",
]