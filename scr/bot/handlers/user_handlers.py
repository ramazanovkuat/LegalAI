from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import kodex_kb, help_kb
from lexicon.lexicon_ru import LEXICON_RU
from retrievers import bm25_faiss_rerank
from llms import YandexGPT

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=help_kb)

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=help_kb)

# Этот хэндлер срабатывает на желание задать вопрос
@router.message(F.text == LEXICON_RU['help_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=kodex_kb)

# Этот хэндлер срабатывает на кодексы
@router.message(F.text.in_([LEXICON_RU['Гражданский процесс'],
                            LEXICON_RU['Способы защиты гражданских прав'],
                            LEXICON_RU['Корпоративные права'],
                            LEXICON_RU['Интеллектуальные права'],
                            LEXICON_RU['Семейное право'],
                            LEXICON_RU['Наследственное право'],
                            LEXICON_RU['Арбитражный процесс '],
                            LEXICON_RU['Обеспечение обязательств'],
                            LEXICON_RU['Обязательственные права'],
                            LEXICON_RU['Вещные права']]))
async def process_yes_answer(message: Message):
        await message.answer(text=LEXICON_RU['choise_yes'], remove_keyboard=True)
        @router.message()
        async def process_game_button(message: Message):
            await message.answer('Спасибо за вопрос! Сейчас решим его, нужно только немного подождать😉')
            await message.reply(YandexGPT(bm25_faiss_rerank(message.text), message.text))
            await message.answer(text=LEXICON_RU['end'], reply_markup=help_kb)


# Этот хэндлер срабатывает на затруднение
@router.message(F.text.in_([LEXICON_RU['Затрудняюсь ответить']]))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['choise_no'])

    @router.message()
    async def process_game_button(message: Message):
        await message.answer('Спасибо за вопрос! Сейчас решим его, нужно только немного подождать😉')
        await message.reply(YandexGPT(bm25_faiss_rerank(message.text),message.text))
        await message.answer(text=LEXICON_RU['end'], reply_markup=help_kb)
