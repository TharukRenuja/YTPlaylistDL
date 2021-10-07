from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("start"))
async def start_msg(client, message):
	await message.reply_text(
		f"👨‍💻 Hello ⚡ {message.from_user.mention}, I Am Powerfull Youtube Video dodownloader bot✳️. You Can Download Youtube Videos And Play Lists🤖.🎈Get A Help Send /help Command Or Click 🎲Help🎲 Button🤓.  This Bot Made By @SLBotsOfficial ❤️❤️..",
		reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🎲 𝙷𝚎𝚕𝚙 🎲", callback_data=f"help"),
					InlineKeyboardButton("👨‍💻 𝙰𝚋𝚘𝚞𝚝 👨‍💻", callback_data=f"about")
				]]
			),
		quote=True)

@Client.on_callback_query()
async def cb_handler(client, update):
	cb_data = update.data
	
	if "help" in cb_data:
		await update.message.edit_text("🎲🎲Just Send URL with Format.(🎸Audio🎸/🎬Video🎬)\n🤔Example Play Lists: `https://youtube.com/playlist?list=xxxxxxxxxx audio`🤔Example Youtube video:`(youtube Url) Audio 😆\n\nPowered by @SLBotsOfficial 💥💥",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("⚡ 𝙰𝚋𝚘𝚞𝚝 ⚡", callback_data=f"about"),
					InlineKeyboardButton("🔙 𝙴𝚡𝚒𝚝 👈", callback_data=f"back")
				]]
			))
	elif "about" in cb_data:
		await update.message.edit_text("🤓Language: Python 🌟\n👨‍🦳 Framework: Pyrogram\n🤖Engine: YTDL 🤖\n🔥Corded By: @TharukRenuja 🔥\n\n🗣️Powered by @SLBotsOfficial 🤡🤡",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🛠 𝙷𝚎𝚕𝚙 🔥", callback_data=f"help"),
					InlineKeyboardButton("🔙 𝙱𝚊𝚌𝚔 👈", callback_data=f"back")
				]]
			))
	elif "back" in cb_data:
		await update.message.edit_text(f"🔥 Hi {update.from_user.mention},🌟If you need any help, Just click help button💥.\n\n🗣️Project by @SLBotsOfficial 🤡🤡",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🛠 𝙷𝚎𝚕𝚙 🌀", callback_data=f"help"),
					InlineKeyboardButton("🌀 𝙰𝚋𝚘𝚞𝚝 💎", callback_data=f"about")
				]]
			))
