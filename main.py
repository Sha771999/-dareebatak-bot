
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

WELCOME = (
    "أهلاً بك في بوت ضريبتك للاستشارات الضريبية.\n\n"
    "يمكنك إرسال سؤالك الضريبي مباشرة، أو اختر نوع الاستشارة:\n"
    "- التسجيل في ضريبة القيمة المضافة\n"
    "- تقديم الإقرار الضريبي\n"
    "- مشكلة في الفاتورة الإلكترونية\n"
    "- استفسار عام\n\n"
    "بعد إرسال سؤالك، سيتم تزويدك بمعلومات الدفع."
)

PAYMENT = (
    "تكلفة الاستشارة: 30 ريال فقط.\n\n"
    "خيارات الدفع:\n"
    "- STC Pay\n"
    "- تحويل بنكي\n\n"
    "أرسل إثبات الدفع (صورة أو نص)، وسيتم الرد خلال أقل من ساعة."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PAYMENT)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
