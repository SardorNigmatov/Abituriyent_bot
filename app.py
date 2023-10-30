from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import dotenv_values

app = dotenv_values(".env")
ADMIN_ID = app.get('ADMIN_ID')
TOKEN = app.get('TOKEN')


# Komandalar
def start_command(update,context):
    username = update.message.from_user.first_name
    commands = [
        BotCommand(command='start',description='botni ishga tushirish'),
        BotCommand(command='info',description='ma\'lumot olish'),
    ]

    buttons = [
        [KeyboardButton(text='Matematika'),KeyboardButton(text='Fizika')],
    ]

    context.bot.set_my_commands(commands=commands)
    update.message.reply_text(text=f"Xush kelibsiz! {username}",reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True))


def info_command(update,context):
    update.message.reply_text(
        text=f'Bu bot Sardorbek Nigmatov tomonidan yaratilgan.\n@SardorbekNigmatov03'
    )


# Buttons

def math_buttons(update,context):

    buttons = [
        [InlineKeyboardButton(text='📹 Video darslar',callback_data='video_lesson')],
        [InlineKeyboardButton(text='📚 Kitoblar',callback_data='books')],
        [InlineKeyboardButton(text='📢 Telegram kanallar',callback_data='channels')],
        [InlineKeyboardButton(text='🧮 Onlayn kalkulyatorlar',callback_data='calculator')],
        [InlineKeyboardButton(text='📩 Botni ulashish',switch_inline_query='Abituriyentlar uchun bot')],
    ]
    update.message.reply_photo(
        photo=open('photos/math.jpg','br'),
        caption='Matematika bo\'limi:',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def physics_buttons(update,context):
    buttons = [
        [InlineKeyboardButton(text='📹 Video darslar', callback_data='phsics_video_lesson')],
        [InlineKeyboardButton(text='📚 Kitoblar',url='https://t.me/Fizikadan_kitoblari')],
        [InlineKeyboardButton(text='📢 Telegram kanallar', callback_data='physics_channels')],
        [InlineKeyboardButton(text='🧮 Onlayn kalkulyatorlar', callback_data='phsics_calculator')],
        [InlineKeyboardButton(text='📩 Botni ulashish', switch_inline_query=' Abituriyentlar uchun bot')],
    ]
    update.message.reply_photo(
        photo=open('photos/physics.jpg', 'br'),
        caption='Fizika bo\'limi:',
        reply_markup=InlineKeyboardMarkup(buttons)
    )




def message_handler(update,context):
    message = update.message.text

    if message == 'Matematika':
        math_buttons(update,context)
    elif message == 'Fizika':
        physics_buttons(update,context)



def inline_message_handler(update,context):
    query = update.callback_query

    if query.data == 'video_lesson':
        buttons = [
            [InlineKeyboardButton(text='Sardorxon Urfonxonov darslari',url='https://youtube.com/@SardorxonUrfonxonov')],
            [InlineKeyboardButton(text='Hasankhoja Muhammad Sodiq darslari',url='https://www.youtube.com/@hasankhojamuhammadsodiq2168')],
            [InlineKeyboardButton(text='Umurzoq Uralov darslari', url='https://www.youtube.com/@Alphraganus')],
            [InlineKeyboardButton(text='Murodjon Xo\'janiyozov darslari',url='https://www.youtube.com/@MatematikRepetitor')],
            [InlineKeyboardButton(text='🔙 Ortga',callback_data='cancel1')]
        ]
        query.message.reply_photo(
            photo=open('photos/math_lesson.jpeg','rb'),
            caption='Video darsni tanlang:',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        query.message.delete()

    elif query.data == 'cancel1':
        buttons = [
            [InlineKeyboardButton(text='📹 Video darslar', callback_data='video_lesson')],
            [InlineKeyboardButton(text='📚 Kitoblar',url='https://t.me/Matematikadan_kitoblar')],
            [InlineKeyboardButton(text='📢 Telegram kanallar', callback_data='channels')],
            [InlineKeyboardButton(text='🧮 Onlayn kalkulyatorlar', callback_data='calculator')],
            [InlineKeyboardButton(text='📩 Botni ulashish', switch_inline_query='Abituriyentlar uchun bot')],
        ]
        query.message.reply_photo(
            photo=open('photos/math.jpg', 'rb'),
            caption='Matematika bo\'limi:',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        query.message.delete()

    elif query.data == 'calculator':
        buttons = [
            [InlineKeyboardButton(text='Ilmiy kalkulator',url='https://www.wolframalpha.com/')],
            [InlineKeyboardButton(text='Matritsalar uchun kalkulyator',url='https://matrixcalc.org/')],
            [InlineKeyboardButton(text='Oliy matematika uchun kalkulyator',url='https://www.emathhelp.net/en/geometry-calculator/')],
            [InlineKeyboardButton(text='Differensial tenglamalar uchun kalkulyator',url='https://mathdf.com/')],
            [InlineKeyboardButton(text='Geometriyadan chizma chizish uchun kalkulyator',url='https://www.geogebra.org/')],
            [InlineKeyboardButton(text='🔙 Ortga', callback_data='cancel1')]
        ]
        query.message.reply_photo(
            photo=open('photos/512x512bb.jpg','rb'),
            caption='Tanlang:',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        query.message.delete()
    elif query.data == 'phsics_video_lesson':
        buttons = [
            [InlineKeyboardButton(text='Razzaqov Xursand darslari',url='https://www.youtube.com/@razzaqovxursandfizika')],
            [InlineKeyboardButton(text='Khan Academy darslari',url='https://www.youtube.com/@KhanAcademyUzbek')],
            [InlineKeyboardButton(text='🔙 Ortga', callback_data='cancel2')],
        ]
        query.message.reply_photo(
            photo=open('photos/physics_lesson.png','rb'),
            caption='Tanlang:',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        query.message.delete()
    elif query.data == 'cancel2':
        buttons = [
            [InlineKeyboardButton(text='📹 Video darslar', callback_data='phsics_video_lesson')],
            [InlineKeyboardButton(text='📚 Kitoblar',url='https://t.me/Fizikadan_kitoblari')],
            [InlineKeyboardButton(text='📢 Telegram kanallar', callback_data='physics_channels')],
            [InlineKeyboardButton(text='🧮 Onlayn kalkulyatorlar',url='https://www.wolframalpha.com/')],
            [InlineKeyboardButton(text='📩 Botni ulashish', switch_inline_query=' Abituriyentlar uchun bot')],
        ]
        query.message.reply_photo(
            photo=open('photos/physics.jpg', 'br'),
            caption='Fizika bo\'limi:',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        query.message.delete()
    elif query.data == 'channels':
        buttons = [
            [InlineKeyboardButton(text='Super Matematika',url='https://t.me/super_matematika')],
            [InlineKeyboardButton(text='Matematika Kursi',url='https://t.me/SARDORXON_URFONXONOV')],
            [InlineKeyboardButton(text='Yangiyo\'l matematiklari',url='https://t.me/yangiyol_matematiklari')],
            [InlineKeyboardButton(text='ALPHRAGANUS',url='https://t.me/alphraganus')],
            [InlineKeyboardButton(text='Khan Academy O\'zbek',url='https://t.me/kau_kurslar')],
            [InlineKeyboardButton(text='🔙 Ortga', callback_data='cancel1')]
        ]
        query.message.reply_photo(
            photo=open('photos/math.jpg', 'rb'),
            caption='Telegram kanallar bo\'limi:',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        query.message.delete()
    elif query.data == 'physics_channels':
        buttons = [
            [InlineKeyboardButton(text='Исмоилов Шерзод',url='https://t.me/SherzodIsmoilovFiz')],
            [InlineKeyboardButton(text='Yangi fizik | Razzaqov Xursand',url='https://t.me/yangi_fizik')],
            [InlineKeyboardButton(text='FIZIKA FINE',url='https://t.me/Fiz_BookXatirchi')],
            [InlineKeyboardButton(text='Fizika | Berdiqulov Xolbek',url='https://t.me/GeneralPhysics_2021')],
            [InlineKeyboardButton(text='🔙 Ortga', callback_data='cancel2')],
        ]
        query.message.reply_photo(
            photo=open('photos/physics.jpg', 'br'),
            caption='Fizika kanallar bo\'limi:',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        query.message.delete()



def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start',start_command))
    dispatcher.add_handler(CommandHandler('info',info_command))
    dispatcher.add_handler(CallbackQueryHandler(inline_message_handler))
    dispatcher.add_handler(MessageHandler(Filters.text,message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()