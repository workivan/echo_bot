import os
import shutil
from zipfile import ZipFile
from pathlib import Path

from aiogram import executor, types, Dispatcher

import config
from uploader import Uploader

dp = Dispatcher(config.bot)


async def send_file(chat_id, file_path):
    file = await config.storage.get_pack_by_path(file_path)
    if file:
        temp_dir = config.TMP_FILES_DIR + Uploader.get_random_dir_name()
        os.mkdir(temp_dir)
        with ZipFile(temp_dir + '/' + file.name + '.zip', 'w') as zf:
            for wav in Path(file.path).rglob('*'):
                if wav.name.startswith('.'):
                    continue
                zf.write(wav, wav.name)
        await config.bot.send_document(
            chat_id,
            document=open(temp_dir + '/' + file.name + '.zip', 'rb')
        )
        shutil.rmtree(temp_dir + '/', ignore_errors=True)
    await config.bot.send_audio(
            chat_id,
            audio=open(file_path.strip(), 'rb')
    )



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    chat_id = message.chat.id
    await config.storage.add_sub(message.chat.id)
    await message.reply("Вы подписаны на библиотеку")
    await config.main_bot.send_message(message.chat.id, "Теперь все ваши звуки будут загружаться в библиотеку")
    pays = await config.storage.get_pays(chat_id)
    if len(pays) > 0:
        await config.bot.send_message(
            chat_id,
            "Сейчас вы получите паки, которые оплатили ранее"
        )
        for pay in pays:
            await send_file(chat_id, pay.product)
            await config.storage.update_pay(chat_id, pay.product)


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
