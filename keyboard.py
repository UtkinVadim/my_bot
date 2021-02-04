from telebot import types

# Привет, я бот Вадима Уткина! Рассказать?
keyboard_start = types.InlineKeyboardMarkup()
start_key_yes = types.InlineKeyboardButton(text='Да!', callback_data='start_yes')
keyboard_start.add(start_key_yes)
start_key_no = types.InlineKeyboardButton(text='Нет!', callback_data='start_no')
keyboard_start.add(start_key_no)

keyboard_item_one = types.InlineKeyboardMarkup()
key_item_one = types.InlineKeyboardButton(text="Что ещё?", callback_data='item_one')
keyboard_item_one.add(key_item_one)

keyboard_item_two = types.InlineKeyboardMarkup()
key_item_two = types.InlineKeyboardButton(text='Продолжай', callback_data='item_two')
keyboard_item_two.add(key_item_two)

keyboard_item_three = types.InlineKeyboardMarkup()
key_item_three = types.InlineKeyboardButton(text='Очень интересно, что ещё?', callback_data='item_three')
keyboard_item_three.add(key_item_three)

keyboard_item_four = types.InlineKeyboardMarkup()
key_item_four = types.InlineKeyboardButton(text='Что дальше?', callback_data='item_four')
keyboard_item_four.add(key_item_four)

keyboard_item_five = types.InlineKeyboardMarkup()
key_item_five = types.InlineKeyboardButton(text='Как мило! А что еще?', callback_data='item_five')
keyboard_item_five.add(key_item_five)

keyboard_item_six = types.InlineKeyboardMarkup()
key_item_six_yes = types.InlineKeyboardButton(text='Хватит! Живо к нам на собеседование!', callback_data='item_six_yes')
keyboard_item_six.add(key_item_six_yes)
key_item_six_no = types.InlineKeyboardButton(text='Хватит! Просто хватит=)', callback_data='item_six_no')
keyboard_item_six.add(key_item_six_no)


# Точно не рассказывать?
keyboard_start_answer = types.InlineKeyboardMarkup()
start_answer_no = types.InlineKeyboardButton(text="Ладно, рассказывай!", callback_data='start_yes')
keyboard_start_answer.add(start_answer_no)
start_answer_yes = types.InlineKeyboardButton(text="Точно!", callback_data='start_no')
keyboard_start_answer.add(start_answer_yes)

keyboard_url = types.InlineKeyboardMarkup()
url_key = types.InlineKeyboardButton(text='Ссылка на резюме.', url="https://spb.hh.ru/resume/befcc292ff08a997a60039ed1f693936706a48")
keyboard_url.add(url_key)
