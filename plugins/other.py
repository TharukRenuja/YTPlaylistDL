from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("start"))
async def start_msg(client, message):
	await message.reply_text(
		f"๐จโ๐ป Hello โก {message.from_user.mention}, I Am Powerfull Youtube Video dodownloader botโณ๏ธ. You Can Download Youtube Videos And Play Lists๐ค.๐Get A Help Send /help Command Or Click ๐ฒHelp๐ฒ Button๐ค.  This Bot Made By @SLBotsOfficial โค๏ธโค๏ธ..",
		reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("๐ฒ ๐ท๐๐๐ ๐ฒ", callback_data=f"help"),
					InlineKeyboardButton("๐จโ๐ป ๐ฐ๐๐๐๐ ๐จโ๐ป", callback_data=f"about")
				]]
			),
		quote=True)

@Client.on_callback_query()
async def cb_handler(client, update):
	cb_data = update.data
	
	if "help" in cb_data:
		await update.message.edit_text("๐ฒ๐ฒJust Send URL with Format.(๐ธAudio๐ธ/๐ฌVideo๐ฌ)\n๐คExample Play Lists: `https://youtube.com/playlist?list=xxxxxxxxxx audio`๐คExample Youtube video:`(youtube Url) Audio ๐\n\nPowered by @SLBotsOfficial ๐ฅ๐ฅ",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("โก ๐ฐ๐๐๐๐ โก", callback_data=f"about"),
					InlineKeyboardButton("๐ ๐ด๐ก๐๐ ๐", callback_data=f"back")
				]]
			))
	elif "about" in cb_data:
		await update.message.edit_text("๐คLanguage: Python ๐\n๐จโ๐ฆณ Framework: Pyrogram\n๐คEngine: YTDL ๐ค\n๐ฅCorded By: @TharukRenuja ๐ฅ\n\n๐ฃ๏ธPowered by @SLBotsOfficial ๐คก๐คก",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("๐  ๐ท๐๐๐ ๐ฅ", callback_data=f"help"),
					InlineKeyboardButton("๐ ๐ฑ๐๐๐ ๐", callback_data=f"back")
				]]
			))
	elif "back" in cb_data:
		await update.message.edit_text(f"๐ฅ Hi {update.from_user.mention},๐If you need any help, Just click help button๐ฅ.\n\n๐ฃ๏ธProject by @SLBotsOfficial ๐คก๐คก",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("๐  ๐ท๐๐๐ ๐", callback_data=f"help"),
					InlineKeyboardButton("๐ ๐ฐ๐๐๐๐ ๐", callback_data=f"about")
				]]
			))
