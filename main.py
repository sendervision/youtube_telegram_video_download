import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
import yt_dlp

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("The TELEGRAM_BOT_TOKEN environment variable is missing.")

# Extract video information
def get_video_info(url):
    try:
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title"),
            "views": info.get("view_count"),
            "channel": info.get("channel"),
            "formats": info.get("formats")
        }
    except Exception as e:
        return None

async def start(update: Update, context):
    await update.message.reply_text("Envoyez-moi un lien YouTube valide pour commencer.")

async def handle_url(update: Update, context):
    url = update.message.text.strip()
    video_info = get_video_info(url)
    if not video_info:
        await update.message.reply_text("Le lien YouTube n'est pas valide ou l'extraction a échoué.")
        return
    
    buttons = [
        [InlineKeyboardButton("MP3", callback_data=f"mp3:{url}")],
        [InlineKeyboardButton("720p", callback_data=f"720p:{url}"),
         InlineKeyboardButton("360p", callback_data=f"360p:{url}")]
    ]
    message = f"**Titre** : {video_info['title']}\n" \
              f"**Vues** : {video_info['views']}\n" \
              f"**Chaîne** : {video_info['channel']}"
    await update.message.reply_text(message, reply_markup=InlineKeyboardMarkup(buttons), parse_mode="Markdown")


async def handle_download(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    # Extract format and url
    format, url = query.data.split(":", 1)
    await query.edit_message_text(f"Téléchargement en cours ({format})...")
    
    # Options pour yt-dlp
    ydl_opts = {"format": "bestaudio/best" if format == "mp3" else f"bestvideo[height={format[:-1]}]+bestaudio"}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            file_info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(file_info)
        
        # Send file
        await query.message.reply_document(document=open(file_path, 'rb'))
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        await query.edit_message_text("Le téléchargement a échoué.")

if __name__ == "__main__":
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_url))
    app.add_handler(CallbackQueryHandler(handle_download))
    
    app.run_polling()
