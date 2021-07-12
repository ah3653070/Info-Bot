# Made with Python3
# (C) Abdul Haseeb @Royalbotz

import 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
        "Info Bot",
        bot_token = os.environ["BOT_TOKEN"],
        api_id = int(os.environ["API_ID"]),
        api_hash = os.environ["API_HASH"]
)

START_TEXT = """
<b>Hello {}

I am a Simple Telegram Info Gathering Bot, Click /help to know my Commands and my uses,<b>
"""
HELP_TEXT = """
🤔 How to use me?

🔶 Forward a Message for take it's Details (in Private)

🔶 Send any Media to take its Details (in private)

🔶 Reply /info to a Message to take Message Details

🔶 Use /info Command to take your Details

🔶 Use /id in Group or Channel to get  Telegram ID
"""
ABOUT_TEXT = """
- **Bot :** `Info Bot`
- **Creator :** [Royalbotz](https://telegram.me/Royalbotz)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://t.me/Royalbotz/38)
- **Vertion :** 0.2.1
- **Channel :** [Royalbotz](https://t.me/Royalbotz)
"""

BOT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="⚠️ Updates ⚠️", url=f"https://t.me/Royalbotz")
        ]]
    )


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="🌐 channel 🌐", url=f"https://t.me/Royalbotz")
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="SOURCE", url=f"https://t.me/Royalbotz/38")
        ]]
    )

ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="🔶 channel 🔶", url=f"https://t.me/Royalbotz")
        ]]
    )
                
@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention) 
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"
    text = f"""
**First Name :** {update.from_user.first_name}

** Second Name :** {last_name}

**Your Username :** {update.from_user.username}

**🆔 Your Telegram ID :** {update.from_user.id}

**🔗 Your Profile Link :** {update.from_user.mention}
""" 
    reply_markup = BOT_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("id"))
async def id(bot, update):
    text = f"""
**Your Telegram ID :** {update.from_user.id}
"""
    reply_markup = BOT_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

Bot.run()
