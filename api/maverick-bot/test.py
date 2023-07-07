"""
    Helper Telegram bot for the payment processing

    Author: Yaekob Demisse
    Date: July 2 2023
"""


import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    Filters,
    MessageHandler,
    Updater,
)

welcome_message = """Welcome to Maverick-Habesh Payment processor Bot
Please Select from the Following: """

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

EMAIL, USERNAME, PAYMENT_REASON, SCREENSHOT_UPLOAD = range(4)


def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help")],
        [InlineKeyboardButton("About", callback_data="about")],
        [InlineKeyboardButton("Upload Screenshot", callback_data="upload_screenshot")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=update.effective_user.id,
        text=welcome_message,
        reply_markup=reply_markup,
    )

    return USERNAME


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "upload_screenshot":
        query.edit_message_text(text="Please enter your email.")
        return USERNAME
    elif query.data == "help":
        query.edit_message_text(text="Help message goes here!")
        return ConversationHandler.END
    elif query.data == "about":
        query.edit_message_text(text="About message goes here!")
        return ConversationHandler.END


def email(update: Update, context: CallbackContext):
    context.user_data["email"] = update.message.text
    keyboard = [
        [
            InlineKeyboardButton(
                "Get Game Access Code", callback_data="game_access_code"
            )
        ],
        [
            InlineKeyboardButton(
                "Get Power Partner Referral Link", callback_data="partner_referral_link"
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=update.effective_user.id,
        text="Please select a reason.",
        reply_markup=reply_markup,
    )

    return PAYMENT_REASON


def reason_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    context.user_data["payment_reason"] = query.data
    query.answer()
    query.edit_message_text(text="Please upload your screenshot.")

    return SCREENSHOT_UPLOAD


def screenshot_upload(update: Update, context: CallbackContext):
    photo_file = update.message.photo[-1].file_id
    if context.user_data["payment_reason"] == "game_access_code":
        chat_id = -1001926622279
    elif context.user_data["payment_reason"] == "partner_referral_link":
        chat_id = -1001839933103

    context.bot.forward_message(
        chat_id=chat_id,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id,
    )
    context.bot.send_message(
        chat_id=chat_id,
        text=f"Username: {context.user_data.get('username')}\nReason: {context.user_data.get('payment_reason')}",
    )

    context.bot.send_message(
        chat_id=update.effective_user.id,
        text="Thank you! Your screenshot is received and posted.",
    )

    return ConversationHandler.END


def main():
    updater = Updater(
        "5834158625:AAHeAeI2vy8WmrKKE9-cgLRmBV5IhRBnHyU", use_context=True
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            USERNAME: [
                MessageHandler(Filters.text & ~Filters.command, username),
                CallbackQueryHandler(button),
            ],
            PAYMENT_REASON: [CallbackQueryHandler(reason_selection)],
            SCREENSHOT_UPLOAD: [MessageHandler(Filters.photo, screenshot_upload)],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    updater.dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
