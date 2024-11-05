from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру первого порядка -------

# Создаем кнопки с ответом
button_help = KeyboardButton(text=LEXICON_RU['help_button'])

# Инициализируем билдер для клавиатуры с кнопкой "У меня вопрос!"
help_builder = ReplyKeyboardBuilder()

# Добавляем кнопку в билдер
help_builder.row(button_help, width=4)

# Создаем клавиатуру с кнопкой "У меня вопрос!"
help_kb: ReplyKeyboardMarkup = help_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)
# ------- Создаем клавиатуру с областями права -------

# Создаем кнопки
button_0 = KeyboardButton(text=LEXICON_RU['Затрудняюсь ответить'])
button_1 = KeyboardButton(text=LEXICON_RU['Гражданский процесс'])
button_2 = KeyboardButton(text=LEXICON_RU['Способы защиты гражданских прав'])
button_3 = KeyboardButton(text=LEXICON_RU['Корпоративные права'])
button_4 = KeyboardButton(text=LEXICON_RU['Интеллектуальные права'])
button_5 = KeyboardButton(text=LEXICON_RU['Семейное право'])
button_6 = KeyboardButton(text=LEXICON_RU['Наследственное право'])
button_7 = KeyboardButton(text=LEXICON_RU['Арбитражный процесс '])
button_8 = KeyboardButton(text=LEXICON_RU['Обеспечение обязательств'])
button_9 = KeyboardButton(text=LEXICON_RU['Обязательственные права'])
button_10 = KeyboardButton(text=LEXICON_RU['Вещные права'])



# Создаем клавиатуру
kodex_kb = ReplyKeyboardMarkup(
    keyboard=[[button_0,button_1],
              [button_2,button_3],
              [button_4,button_5],
              [button_6,button_7],
              [button_8,button_9],
              [button_10]],
    resize_keyboard=True,
    one_time_keyboard=True
)