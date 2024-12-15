from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# Создание экземпляра бота
bot = Bot(token='8152024081:AAHpyXyhqVO-deUnwXhsRzt0Q5cPsEogca8')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Пример обработчика команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я ваш Telegram бот.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
