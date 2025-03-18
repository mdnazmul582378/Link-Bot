from pyrogram import Client, filters
import urllib.parse

config = {
    "api_id": 25534833,  # নিজের আপি আইডি
    "api_hash": "8ec7028f3b0871fe6f0ee68e8230e4bc",
    "bot_token": "7822994174:AAFXQzXudaGS_3mEPuc-y3Bq_0AneonWN4Q"
}

link_bot = Client("movie_linkser_bot", api_id=config["api_id"], api_hash=config["api_hash"], bot_token=config["bot_token"])

@link_bot.on_message(filters.command("start"))
def start(client, message):
    if len(message.command) > 1:
        data = message.command[1]
        decoded = urllib.parse.unquote(data)
        title, link = decoded.split("|", 1)
        message.reply_text(f"🎥 **Your requested movie:** {title}\n\n🔗 [Click here to Watch/Download]({link})", disable_web_page_preview=True)
    else:
        message.reply_text("👋 Welcome! Please use the movie bot buttons to get your movie links.")

link_bot.run()
