from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢 Join Our Channel", url=client.invitelink) ]]
    text = "**Please Join My Update Channel Before Using Me..**"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
