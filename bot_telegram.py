import asyncio
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, MessageHandler, filters, ContextTypes,  CommandHandler
from telegram import Bot
from db import crear_tabla
from calculos import calcular_total, mostrar_total
from registro import registrar_ingreso, registrar_egreso
from telegram_conect import mostrar_consultas, teclado_proveedores

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def borrar_webhook_si_existe():
    bot = Bot(token=TOKEN)
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url:
        print(f"🌐 Webhook detectado: {webhook_info.url} — eliminando...")
        await bot.delete_webhook()
    else:
        print("✅ No hay webhook activo.")

# --- Handlers ---
async def manejar_mensaje(update, context):
    # Tu código aquí...
    pass

async def manejar_boton(update, context):
    # Tu código aquí...
    pass

# --- App principal ---
async def start(update, context):
    await update.message.reply_text("¡Hola!")
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    await app.run_polling()  # ya maneja el loop

if __name__ == "__main__":
    asyncio.run(main()) 
