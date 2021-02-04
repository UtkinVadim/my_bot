import telebot
import keyboard

bot = telebot.TeleBot('1647721344:AAFsO8PS_4tR8m09oET42dcuawVVu2Blo3E')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Привет! Я бот Вадима Уткина! Я хочу рассказать Вам, почему его стоит взять на работу, ведь я его знаю как никто другой! Рассказать?:)",
                         reply_markup=keyboard.keyboard_start)
    else:
        bot.send_message(message.from_user.id, "Напишите /start")


@bot.callback_query_handler(func=lambda call: True)
def buttons(call):
    if call.data == "start_no":
        bot.send_message(call.from_user.id, 'Точно?',
                         reply_markup=keyboard.keyboard_start_answer)
    if call.data == "start_yes":
        bot.send_message(call.from_user.id, 'Во первых - он очень ответственный!',
                         reply_markup=keyboard.keyboard_item_one)
    if call.data == "item_one":
        bot.send_message(call.from_user.id, 'Во вторых - он очень легко всему учится!',
                         reply_markup=keyboard.keyboard_item_two)
    if call.data == "item_two":
        love_it = open('love_it.jpg', 'rb')
        bot.send_message(call.from_user.id,
                         'В третьих - ему очень нравится программирование и всё, что связано с миром IT!')
        bot.send_photo(call.from_user.id, love_it, reply_markup=keyboard.keyboard_item_three)
    if call.data == "item_three":
        bot.send_message(call.from_user.id,
                         'В четвертых - он никогда не отчаиваится, если что-то не получается, а добивается желаемого результата!',
                         reply_markup=keyboard.keyboard_item_four)
    if call.data == "item_four":
        some_child = open('some_child.jpg', 'rb')
        bot.send_message(call.from_user.id, 'Он создал меня! =)')
        bot.send_photo(call.from_user.id, some_child,
                       reply_markup=keyboard.keyboard_item_five)
    if call.data == "item_five":
        bot.send_message(call.from_user.id, 'В шестых - во что бы то ни стало - он всегда доводит дело до конца!',
                         reply_markup=keyboard.keyboard_item_six)
    if call.data == "item_six_yes":
        bot.send_message(call.from_user.id,
                         'Ура! Напишите ему на почту utkinvadim1991@gmail.com, или позвоните ему по телефону +7-981-687-38-20. Он будет очень рад этой новости!', reply_markup=keyboard.keyboard_url)
    if call.data == "item_six_no":
        bot.send_message(call.from_user.id,
                         'Хорошо, зато теперь вы знаете немного больше про Вадима!=) Всего Вам доброго и хорошего дня!=)')


bot.polling(none_stop=True, interval=0)
