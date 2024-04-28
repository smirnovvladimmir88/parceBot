from typing import List
import logging
from pyrogram import Client, idle, filters
from background import keep_alive
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
import asyncio
API_ID: int = 26973684
API_HASH: str = 'd2ff9778152b2b5445e152a31e28b87e'
# -1002008240526 - моя группа для тестов
# -1001892497462 - t.me/crypto группа @crypto
# -1001151342291 - https://t.me/coincunews
# -1001145462707 - https://t.me/whalebotalerts транзакции 
# -1001343081160 - https://t.me/cryptominers_news новости крипто
# -1001769001896 - https://t.me/CoingraphNews новости крипто
# -1001132611527 - https://t.me/Coin_Post новости крипто RU
# -1001321981396 - https://t.me/CRYPTUS_MEDIA новости крипто RU
BOT_TOKEN = '6287352550:AAGd5YkTUM7w01ECX7cVj63H3JJ5Upp7-lo'
donors_ids: List[int] = [-1001145462707, -1001151342291, -1002008240526, -1001892497462, -1001343081160,  -1001769001896, -1001132611527, -1001321981396 ]
technical_channel: int = -1002109162311
my_target_channel: int = -1001963897723
async def new_post(client: Client, message: Message):
    await client.copy_message(chat_id=technical_channel, from_chat_id=message.chat.id, message_id=message.id)
    
async def copy_to_my_channel(client: Client, message: Message):
  await client.copy_message(chat_id=my_target_channel, from_chat_id=message.chat.id, message_id=message.reply_to_message_id)
  await message.reply_to_message.delete()
  
async def start():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    
    user_bot = Client(name='user_bot', api_id=API_ID, api_hash=API_HASH)
    
    bot_content = Client(name='bot_content', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    user_bot.add_handler(MessageHandler(new_post, filters.chat(chats=donors_ids)))
    bot_content.add_handler(MessageHandler(copy_to_my_channel, filters.reply))
    
    await user_bot.start()
    await bot_content.start()
    await idle()
    await user_bot.stop()
    await bot_content.stop()
keep_alive()
if __name__ == '__main__':
    asyncio.run(start())
