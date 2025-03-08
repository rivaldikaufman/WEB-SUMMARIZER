import logging
import google.generativeai as genai
from newspaper import Article
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, CallbackQueryHandler, filters, CallbackContext

# Konfigurasi API
BOT_TOKEN = "YOUR BOTFATHER TOKEN"
GEMINI_API_KEY = "YOUR GEMINI API"

genai.configure(api_key=GEMINI_API_KEY)

# Logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# Dictionary untuk menyimpan URL sementara
user_data = {}


# Fungsi untuk ekstrak teks dari artikel
def get_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Error mengambil artikel: {str(e)}"


# Fungsi untuk rangkum teks dengan Gemini
def summarize_text(text, language, style):
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    prompt = f"Ringkas artikel berikut dalam bahasa {language} dengan gaya bahasa {style}:\n\n{text[:4000]}"
    response = model.generate_content(prompt)
    return response.text if response.text else "Gagal merangkum artikel."


# Fungsi handle pesan
async def handle_message(update: Update, context: CallbackContext):
    url = update.message.text
    if url.startswith("http"):
        await update.message.reply_text("Mengambil artikel...")
        article_text = get_article_text(url)

        if "Error" in article_text:
            await update.message.reply_text(article_text)
        else:
            user_data[update.message.chat_id] = article_text  # Simpan teks artikel
            keyboard = [
                [InlineKeyboardButton("🇮🇩 Bahasa Indonesia", callback_data="lang_id"),
                 InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text("Pilih bahasa ringkasan:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Kirim link artikel yang valdi!")


async def handle_language_choice(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    language = "Indonesia" if query.data == "lang_id" else "English"
    user_data[chat_id + 1] = language  # Simpan pilihan bahasa

    keyboard = [
        [InlineKeyboardButton("📜 Formal", callback_data="style_formal"),
         InlineKeyboardButton("😎 Gaul", callback_data="style_gaul"),
         InlineKeyboardButton("🗿 Jaksel", callback_data="style_jaksel")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Pilih gaya bahasa:", reply_markup=reply_markup)
    await query.answer()

async def handle_style_choice(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    style_map = {
        "style_formal": "formal",
        "style_gaul": "gaul",
        "style_jaksel": "Jaksel"
    }
    style = style_map.get(query.data, "formal")
    language = user_data.get(chat_id + 1, "Indonesia")
    article_text = user_data.get(chat_id, "")

    await query.message.reply_text("Merangkum artikel...")
    summary = summarize_text(article_text, language, style)
    await query.message.reply_text(summary)
    await query.answer()


# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_language_choice, pattern="^lang_.*"))
    app.add_handler(CallbackQueryHandler(handle_style_choice, pattern="^style_.*"))

    logging.info("Bot berjalan...")
    app.run_polling()


if __name__ == "__main__":
    main()