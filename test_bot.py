from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# User balances (in-memory)
user_data = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Initialize user if new
    if user_id not in user_data:
        user_data[user_id] = {"balance": 0, "claimed": False}

    balance = user_data[user_id]["balance"]

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⛏ Claim Coins", callback_data="claim")],
        [InlineKeyboardButton("⚡ Boost Mining", callback_data="boost")]
    ])

    await update.message.reply_text(
        f"👋 Welcome to Byyte Miner!\n\n"
        f"💰 Balance: ₹{balance:.2f}\n\nChoose an action below 👇",
        reply_markup=keyboard
    )

# Button click handler
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if user_id not in user_data:
        user_data[user_id] = {"balance": 0, "claimed": False}

    if query.data == "claim":
        if not user_data[user_id]["claimed"]:
            user_data[user_id]["balance"] += 1.00
            user_data[user_id]["claimed"] = True
            await query.edit_message_text(
                f"✅ Claimed ₹1.00!\nNew Balance: ₹{user_data[user_id]['balance']:.2f}")
        else:
            await query.answer("⛏ Already claimed! Try again later.", show_alert=True)

    elif query.data == "boost":
        await query.answer("⚡ Boost feature coming soon!", show_alert=True)

# Start bot
TOKEN = "8020306717:AAGnzyRSN1-kWyuAA34WK4Mf48N8tQ-sIy8"
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_buttons))
print("🚀 Miner bot is running...")
app.run_polling()
