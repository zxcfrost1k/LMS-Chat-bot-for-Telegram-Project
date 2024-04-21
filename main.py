import telebot
from telebot import types


my_bot = telebot.TeleBot('6384079003:AAGFeXHw4EzPt6AeAftFdLFDCfzx48fBucI')


@my_bot.message_handler(commands=['start', 'restart'])
def init_bot(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Начать', callback_data='start'))
    my_bot.send_sticker(message.chat.id,
                        'CAACAgQAAxkBAAEKhQZlKXAg2YRMJjaMTbkUPQZrFU8mCQACxA4AAkJaCFMhI834J3CWbjAE')
    my_bot.send_message(message.chat.id, f'🎆 Приветствую тебя, {message.from_user.first_name}\n'
                                         f'Далее, я попрошу вас ответить на несколько вопросов.', reply_markup=markup)


@my_bot.message_handler(commands=['info'])
def help_bot(message):
    my_bot.send_sticker(message.chat.id,
                        'CAACAgQAAxkBAAEKhT1lKZ23pOYMkTAGO1Ps7StjSKjzyAACrBIAApWbaVL0T9mX-fVngzAE')
    my_bot.send_message(message.chat.id, '<code>💟 frost1k`s stylist bot</code>'
                                         '\nВаш личный помощник, готовый помочь вам создать собственную уникальную '
                                         'стилизацию и неповторимый образ\n'
                                         '- - - - - - - - - - - - - - - - - - - - - - - - - - - -\n'
                                         '<code>🧩 История создания</code>'
                                         '\nСоздан в конце 2023 года, учеником 11IT класса, специально для LMS\n'
                                         '\n\n'
                                         '\n🎯 <em>made by @zxcfrost1k</em>', parse_mode='html')


@my_bot.callback_query_handler(func=lambda callback: True)
def gender(callback):
    if callback.data == 'start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        gender_buttons = ['Парень', 'Девушка']
        markup.add(*gender_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_sticker(callback.message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.send_message(callback.message.chat.id, 'Ну и кто ты у нас?', reply_markup=markup)
        my_bot.register_next_step_handler(callback.message, on_click_gender)


def on_click_gender(message):
    if message.text == 'Парень':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        age_buttons = ['15-17', '18-25', '25+']
        markup.add(*age_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.send_message(message.chat.id, 'Ну и сколько тебе?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_age_male)
    elif message.text == 'Девушка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        age_buttons = ['15-17', '18-25', '25+']
        markup.add(*age_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.send_message(message.chat.id, 'Ну и сколько тебе, миледи?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_age_female)
    elif message.text == 'Назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Начать', callback_data='start'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhQZlKXAg2YRMJjaMTbkUPQZrFU8mCQACxA4AAkJaCFMhI834J3CWbjAE')
        my_bot.send_message(message.chat.id, f'🎆 Приветствую тебя, {message.from_user.first_name}\n'
                                             f'Далее, я попрошу вас ответить на несколько вопросов.',
                            reply_markup=markup)
    elif 'start' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Начать', callback_data='start'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhQZlKXAg2YRMJjaMTbkUPQZrFU8mCQACxA4AAkJaCFMhI834J3CWbjAE')
        my_bot.send_message(message.chat.id, f'🎆 Приветствую тебя, {message.from_user.first_name}\n'
                                             f'Далее, я попрошу вас ответить на несколько вопросов.',
                            reply_markup=markup)
    else:
        my_bot.send_message(message.chat.id, 'Кнопку нажми, дуралей')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhm1lKrleMk5iAm6MBM6DlRFuq6UrcgACsBkAAkTzcFJV5Dheo2nFUDAE')
        my_bot.register_next_step_handler(message, on_click_gender)


def on_click_age_male(message):
    if message.text == '15-17':
        my_bot.send_message(message.chat.id, 'гы, малолетка')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhmtlKrd-qWklFgqQ3-6dE4QWRt7htgACARMAArBlaVJx7MNtm_KkaDAE')
        my_bot.send_message(message.chat.id, 'За шмотки шаришь?\nЕс что, напечатать надо')
        my_bot.register_next_step_handler(message, age1_fashion_demon)
    elif message.text == '18-25':
        my_bot.send_message(message.chat.id, 'гм, солидно')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEL9jtmJN4jk7dFBzlfy0Jw23282szG3AACsA8AAo5wcVL0lHRnyeREbTQE')
        my_bot.send_message(message.chat.id, 'За вещички шаришь?\nМодные показы там, стилизация и тп\nЕсли что,'
                                             ' напечатать надо')
        my_bot.register_next_step_handler(message, age1_fashion_demon)
    elif message.text == '25+':
        my_bot.send_message(message.chat.id, 'ухх, ну ты и старичок')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhnVlKr4bhe8vkILsCoKTxmecm05JJAAC3w8AAhJmWFNEOjmAE2qcPTAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что желаешь?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == 'Назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        gender_buttons = ['Парень', 'Девушка']
        markup.add(*gender_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.send_message(message.chat.id, 'Ну и кто ты у нас?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_gender)
    elif 'start' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Начать', callback_data='start'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhQZlKXAg2YRMJjaMTbkUPQZrFU8mCQACxA4AAkJaCFMhI834J3CWbjAE')
        my_bot.send_message(message.chat.id, f'🎆 Приветствую тебя, {message.from_user.first_name}\n'
                                             f'Далее, я попрошу вас ответить на несколько вопросов.',
                            reply_markup=markup)
    else:
        my_bot.send_message(message.chat.id, 'Кнопку нажми, дуралей')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhm1lKrleMk5iAm6MBM6DlRFuq6UrcgACsBkAAkTzcFJV5Dheo2nFUDAE')
        my_bot.register_next_step_handler(message, on_click_age_male)


def on_click_age_female(message):
    if message.text == '15-17':
        my_bot.send_message(message.chat.id, 'оу, малолеточка')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhn9lKsI6Yjc8KA-gJjwEoM7_eN1PjwACwg4AAvtHAAFTlMfejBtQwoQwBA')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '18-25':
        my_bot.send_message(message.chat.id, 'оаоаоа, да ты в самом расцвете 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhnhlKsIc-V6ueq8RgXc5u8y7MMteRAACdw0AAvEUWFOUVhzRUGKbKTAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        age_buttons = ['Что-нибудь на каждый день', 'Хочется быть самой самой на тусе']
        markup.add(*age_buttons)
        markup.add(types.KeyboardButton('Хочу красивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, красотка?', reply_markup=markup)
        # my_bot.register_next_step_handler(message, on_click_purpose_female_2age)
    elif message.text == '25+':
        my_bot.send_message(message.chat.id, 'ооо, мил..., проехали')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhotlKsLId5CitK8ojuRDW8FLPKWDpQACTBAAAhGHAAFTQ_29KqJRnZ0wBA')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное, костюмчик там какой-нибудь'))
        markup.add(types.KeyboardButton('Хочется выглядить стильно на работе'))
        markup.add(types.KeyboardButton('Хочу модное платье на выход'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаешь, королева?', reply_markup=markup)
        # my_bot.register_next_step_handler(message, on_click_purpose_female_3age)
    elif message.text == 'Назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добилась?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        gender_buttons = ['Парень', 'Девушка']
        markup.add(*gender_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.send_message(message.chat.id, 'Ну и кто ты у нас?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_gender)
    elif 'start' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Начать', callback_data='start'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhQZlKXAg2YRMJjaMTbkUPQZrFU8mCQACxA4AAkJaCFMhI834J3CWbjAE')
        my_bot.send_message(message.chat.id, f'🎆 Приветствую тебя, {message.from_user.first_name}\n'
                                             f'Далее, я попрошу вас ответить на несколько вопросов.',
                            reply_markup=markup)
    else:
        my_bot.send_message(message.chat.id, 'Кнопку нажми, дурочка')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhm1lKrleMk5iAm6MBM6DlRFuq6UrcgACsBkAAkTzcFJV5Dheo2nFUDAE')
        my_bot.register_next_step_handler(message, on_click_age_female)


def age1_fashion_demon(message):
    true = ['да', 'конечно', 'ага', 'угу', 'кнш', 'типо да', 'ну тип', 'есс', 'ес', 'обижаешь', 'yes', 'da',
            'aga', 'ye', 'yep']
    false = ['нет', 'неа', 'никак нет', 'тип нет', 'ну нет', 'не', 'ноу', 'ноуп', 'no', 'net', 'ne', 'nop']
    if message.text.lower() in true:
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKho1lKscMUosv691vvJHs8HZXjC16mAACzg0AAn--aFL252f3QwvglTAE')
        my_bot.send_message(message.chat.id, 'Да ты рил fashion demon')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text.lower() in false:
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKho9lKsn7tPY14vLyU-IcZvo09_uQaQAC_A0AApSdYVODq4RGhWU7ETAE')
        my_bot.send_message(message.chat.id, 'Ясно')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        age_buttons = ['15-17', '18-25', '25+']
        markup.add(*age_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.send_message(message.chat.id, 'Ну и сколько тебе?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_age_male)
    elif 'start' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Начать', callback_data='start'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhQZlKXAg2YRMJjaMTbkUPQZrFU8mCQACxA4AAkJaCFMhI834J3CWbjAE')
        my_bot.send_message(message.chat.id, f'🎆 Приветствую тебя, {message.from_user.first_name}\n'
                                             f'Далее, я попрошу вас ответить на несколько вопросов.',
                            reply_markup=markup)
    else:
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhm1lKrleMk5iAm6MBM6DlRFuq6UrcgACsBkAAkTzcFJV5Dheo2nFUDAE')
        my_bot.send_message(message.chat.id, 'Те надо просто написать да/нет, дуралей')
        my_bot.register_next_step_handler(message, age1_fashion_demon)


def on_click_purpose_male_1age_fashion(message):
    if message.text == 'Y2K':
        my_bot.send_message(message.chat.id, 'Ну держи')
        image = open('Files/male_1age_fashion_y2k_1.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_y2k_like1)
    elif message.text == 'opium':
        my_bot.send_message(message.chat.id, 'Ну держи')
        image = open('Files/male_1age_fashion_opium_1.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_opium_like1)
    elif message.text == 'casual':
        my_bot.send_message(message.chat.id, 'Ну держи')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_casual_like1)
    elif message.text == 'drill':
        my_bot.send_message(message.chat.id, 'Ну держи')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_drill_like1)
    elif message.text == 'old money':
        my_bot.send_message(message.chat.id, 'Ну держи')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_oldmoney_like1)
    elif message.text == 'street wear':
        my_bot.send_message(message.chat.id, 'Ну держи')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_streetwear_like1)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhmtlKrd-qWklFgqQ3-6dE4QWRt7htgACARMAArBlaVJx7MNtm_KkaDAE')
        my_bot.send_message(message.chat.id, 'Так шаришь или нет, определись?\nЕс что, напечатать надо, напоминаю')
        my_bot.register_next_step_handler(message, age1_fashion_demon)


def on_click_purpose_male_1age_none_fashion(message):
    if message.text == 'Хочется что-нибудь простое и стильное':
        my_bot.send_message(message.chat.id, 'Ну держи')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion_1_like1)
    if message.text == 'Нужно классику (тип солидненько выгдять)':
        my_bot.send_message(message.chat.id, 'Ну держи')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion_2_like1)
    if message.text == 'Хочу, чтобы туса за мной осталась':
        my_bot.send_message(message.chat.id, 'Ну держи')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion_3_like1)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhmtlKrd-qWklFgqQ3-6dE4QWRt7htgACARMAArBlaVJx7MNtm_KkaDAE')
        my_bot.send_message(message.chat.id, 'Так шаришь или нет, определись?\nЕс что, напечатать надо, напоминаю')
        my_bot.register_next_step_handler(message, age1_fashion_demon)


def on_click_purpose_male_3age(message):
    if message.text == 'Нужно что-нибудь солидное':
        my_bot.send_message(message.chat.id, 'Как вам?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_age3_1_like1)
    if message.text == 'Хочется выглядить помоложе на работе':
        my_bot.send_message(message.chat.id, 'Как вам?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_age3_2_like1)
    if message.text == 'Хочу быть более стильным, чем сын':
        my_bot.send_message(message.chat.id, 'Как вам?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_age3_3_like1)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        age_buttons = ['15-17', '18-25', '25+']
        markup.add(*age_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.send_message(message.chat.id, 'Ну и сколько тебе?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_age_male)


def on_click_purpose_female_1age(message):
    if message.text == 'Хочу классику (пиджачок там, рубашечку)':
        my_bot.send_message(message.chat.id, 'Как те?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age_1_like1)
    if message.text == 'Что-нибудь на каждый день, но не быть стадом':
        my_bot.send_message(message.chat.id, 'Как те?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age_2_like1)
    if message.text == 'Хочу карсивенькое платьеце с маленькой сумочкой':
        my_bot.send_message(message.chat.id, 'Как те?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age_3_like1)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        age_buttons = ['15-17', '18-25', '25+']
        markup.add(*age_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.send_message(message.chat.id, 'Ну и сколько тебе?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_age_female)


def on_click_purpose_male_1age_fashion_y2k_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>Зипка</b> — <code>PALACE FW23 SPIDER ZIP HOOD SHOCK</code>'
                            '\n<b>Штансы</b> — <code>Voguo Relay [no model]</code>'
                            '\n<b>Кроссы</b> — <code>Bathing Ape Sta PINK</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/male_1age_fashion_y2k_2.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_y2k_like2)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_opium_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>Куртка</b> — <code>Supreme x H.R. Giger JACQUARD DOWN PUFFER JACKET</code>'
                            '\n<b>Штансы</b> — <code>Voguo Relay [no model]</code>'
                            '\n<b>Кроссы</b> — <code>Rick Owens DRKSHDW</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/male_1age_fashion_opium_2.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_opium_like2)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_casual_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_casual_like2)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_drill_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_drill_like2)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_oldmoney_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_oldmoney_like2)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_streetwear_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_streetwear_like2)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_none_fashion_1_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion_1_like2)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)


def on_click_purpose_male_1age_none_fashion_2_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion_2_like2)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)


def on_click_purpose_male_1age_none_fashion_3_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, вам понравилось\nТогда держите:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Как насчёт этого?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion_3_like2)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)


def on_click_purpose_male_age3_1_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, вам понравилось\nТогда держите:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Как насчёт этого?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_age3_1_like2)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)


def on_click_purpose_male_age3_2_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, вам понравилось\nТогда держите:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Как насчёт этого?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_age3_2_like2)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)


def on_click_purpose_male_age3_3_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, вам понравилось\nТогда держите:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Как насчёт этого?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_age3_3_like2)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)


def on_click_purpose_female_1age_1_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, те зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Как насчёт этого?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age_1_like2)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)


def on_click_purpose_female_1age_2_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, те зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Как насчёт этого?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age_2_like2)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)


def on_click_purpose_female_1age_3_like1(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, те зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Как насчёт этого?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age_3_like2)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)


def on_click_purpose_male_1age_fashion_y2k_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>Зипка</b> — <code>KAKAZZY SONIC</code>'
                            '\n<b>Штансы</b> — <code>THEWIZBRAND [no model]</code>'
                            '\n<b>Кроссы</b> — <code>Bathing Ape Sta BLUE</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Та ты надоел, на')
        image = open('Files/male_1age_fashion_y2k_3.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_y2k_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_opium_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>Лонгслив</b> — <code>Veidoorn x Pokemon</code>'
                            '\n<b>Штансы</b> — <code>GDRX [no model]</code>'
                            '\n<b>Кроссы</b> — <code>BALENSIAGA track 1</code>'
                            '\n<b>Балаклава</b> — <code>Baijuan</code>'
                            '\n<b>Очки</b> — <code>Astar Hades</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Согласен, предыдущий образ мне тож не зашёл')
        image = open('Files/male_1age_fashion_opium_3.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_opium_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_casual_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_casual_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_drill_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_drill_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_oldmoney_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_oldmoney_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_streetwear_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion_streetwear_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_none_fashion_1_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion_1_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)


def on_click_purpose_male_1age_none_fashion_2_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion_2_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)


def on_click_purpose_male_1age_none_fashion_3_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion_3_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)


def on_click_purpose_male_age3_1_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, вам понравилось\nТогда держите:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Может тогда это?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_age3_1_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)


def on_click_purpose_male_age3_2_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, вам понравилось\nТогда держите:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Может тогда это?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_age3_2_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)


def on_click_purpose_male_age3_3_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, вам понравилось\nТогда держите:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Может тогда это?')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_male_age3_3_like3)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)


def on_click_purpose_female_1age_1_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age_1_like3)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)


def on_click_purpose_female_1age_2_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age_2_like3)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)


def on_click_purpose_female_1age_3_like2(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '👎':
        my_bot.send_message(message.chat.id, 'Ну на ещё')
        image = open('Files/soon.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        like_buttons = ['👍', '👎']
        markup.add(*like_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_photo(message.chat.id, image, reply_markup=markup)
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKhTtlKZ1F4BTW6fWSv2Ynd4KepFg7rAAC4Q8AArxbaFLSuZM4g2wrLzAE')
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age_3_like3)
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)


def on_click_purpose_male_1age_fashion_y2k_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>Зипка</b> — <code>BAPE zip hoodie [no model]</code>'
                            '\n<b>Штансы</b> — <code>Stussy FW22</code>'
                            '\n<b>Кроссы</b> — <code>Bathing Ape Sta PINK</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_opium_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id, '<b>Жакет</b> — <code>GDRX [no model]</code>'
                                             '\n<b>Штансы</b> — <code>Voguo Relay [no model]</code>'
                                             '\n<b>Кроссы</b> — <code>Rick Owens DRKSHDW</code>'
                                             '\n<b>Очки</b> — <code>[no name]</code>', parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_casual_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_drill_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_oldmoney_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)

    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_fashion_streetwear_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что-то ещё нужно?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        style_buttons = ['Y2K', 'opium', 'casual', 'drill', 'old money', 'street wear']
        markup.add(*style_buttons)
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_fashion)


def on_click_purpose_male_1age_none_fashion_1_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)


def on_click_purpose_male_1age_none_fashion_2_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)


def on_click_purpose_male_1age_none_fashion_3_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочется что-нибудь простое и стильное'))
        markup.add(types.KeyboardButton('Нужно классику (тип солидненько выгдять)'))
        markup.add(types.KeyboardButton('Хочу, чтобы туса за мной осталась'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Ну и что надо?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_1age_none_fashion)


def on_click_purpose_male_age3_1_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что желаешь?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Очень жаль')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что желаешь?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)


def on_click_purpose_male_age3_2_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что желаешь?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Очень жаль')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что желаешь?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)


def on_click_purpose_male_age3_3_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что желаешь?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Очень жаль')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что желаешь?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Нужно что-нибудь солидное'))
        markup.add(types.KeyboardButton('Хочется выглядить помоложе на работе'))
        markup.add(types.KeyboardButton('Хочу быть более стильным, чем сын'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что пожелаете?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_male_3age)


def on_click_purpose_female_1age_1_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда, бе')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)


def on_click_purpose_female_1age_2_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда, бе')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)


def on_click_purpose_female_1age_3_like3(message):
    if message.text == '👍':
        my_bot.send_message(message.chat.id, 'Я погляжу, тебе зашло\nТогда лови:')
        my_bot.send_message(message.chat.id,
                            '<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>'
                            '\n<b>*</b> — <code>*</code>',
                            parse_mode='html')
        my_bot.send_message(message.chat.id, 'Рад был помочь 🌸')
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKh_1lLB_c5OzTJwS7oRPaHI_JtGyYbQACxA4AAkJaCFMhI834J3CWbjAE')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text == '👎':
        my_bot.send_sticker(message.chat.id,
                            'CAACAgQAAxkBAAEKiAdlLClVXU6S1O9xlkJzkZH2ujIrxwACgQwAAqSVWVNWgoz58fdq8TAE')
        my_bot.send_message(message.chat.id, 'Ну и катись отсюда, бе')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)
    elif message.text.lower() == 'назад':
        my_bot.send_message(message.chat.id, '🔪 ну и чего ты этим добился?')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Хочу классику (пиджачок там, рубашечку)'))
        markup.add(types.KeyboardButton('Что-нибудь на каждый день, но не быть стадом'))
        markup.add(types.KeyboardButton('Хочется быть самой самой на тусе'))
        markup.add(types.KeyboardButton('Хочу карсивенькое платьеце с маленькой сумочкой'))
        markup.add(types.KeyboardButton('Назад'))
        my_bot.send_message(message.chat.id, 'Что предпочтёшь, принцесса?', reply_markup=markup)
        my_bot.register_next_step_handler(message, on_click_purpose_female_1age)


my_bot.polling(none_stop=True)
