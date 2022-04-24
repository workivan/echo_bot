from aiogram import executor, types, Dispatcher

import config

dp = Dispatcher(config.bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await config.storage.add_sub(message.chat.id)
    await message.reply("Вы подписаны на библиотеку")


async def on_startup(dp):
    await config.storage.init(config.DB_URL)
    # await config.bot.set_webhook(config.WEBHOOK_URL)


async def on_shutdown(dp):
    # await config.bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
