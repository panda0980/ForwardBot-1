from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "11671320")
    API_HASH = environ.get("API_HASH", "8e409e260f1d80f0ead65da912ee07bb")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5813212548:AAG1503Ilf2se-uiHkWwNSxPSr20v0yL6Oo")
    STRING_SESSION = environ.get("STRING", "BQBtDYfn0sUsI76Bhk6Ez-9Jx-Px-_TP50c4ZdXifWRdwVRcCXSvGSdXQ53X4aqdq0Wp5ptiSA-ql0waGMHDCQ_-NZmGvU4HkAGaMJvbg8FTgB6d9J3iBxFyeWmZ8t8CRe2jSyF7vvQ568FEGJ8cnoa8yreNhVJNxK_C8g3n1MHpt2jX0iwoPnwYByCl6o7zKIUyW3CFd0LP-o3h5tFrq3IDBgpnpUiVyfNdXSJ-q0jdeegbrEq-6ApotTWxS580NpbW1iq3fw21sBYrDvcFFxmhcx3uK5EIkvEJ4MLNoClQt9JSYtmgHNiKDBpIvSgwbIFX9dgBIBtSSbBxNb_e64X5djpEVgA")
    SUDO_USERS = environ.get("SUDO_USERS", "1983530070")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
