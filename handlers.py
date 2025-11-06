from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup

from db import add_user


def start(update: Update, context: CallbackContext):
    if add_user(
        tg_id=update.message.from_user.id,
        full_name=update.message.from_user.full_name,
        username=update.message.from_user.username
    ):
        update.message.reply_text(
            text=f'salom {update.message.from_user.full_name}, botga xush kelibsiz.',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    ['Bosh Sahifa', 'Aloqa']
                ]
            )
        )
    else:
        update.message.reply_text(
            text=f'qaytganingiz bilan {update.message.from_user.full_name}.',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    ['Bosh Sahifa', 'Aloqa']
                ]
            )
        )

def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=f'{update.message.from_user.full_name}, qanday yordam kerak?',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                ['button 1', 'button 2'],
                ['button 3', 'button 4', 'button 5']
            ]
        )
    )

def echo_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        update.message.text
    )

def echo_photo(update: Update, context: CallbackContext):
    update.message.reply_photo(
        update.message.photo[1]
    )

def send_products(update: Update, context: CallbackContext):
    update.message.reply_text('mana barcha mahsulotlar')

def main_menu(update: Update, context: CallbackContext):
    update.message.reply_text('asosiy sahifaga keldiz')
