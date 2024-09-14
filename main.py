from aiogram import Dispatcher, Bot, filters, types, F
import asyncio
from confiq import TOKEN, ADMIN
from database import Database
from buttons.reply_button import all_users_button
from aiogram.types import ReplyKeyboardMarkup




bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
db = Database()




@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    if message.from_user.id == ADMIN:
        db.create_table_users()
        user_id = message.from_user.id
        user_full_name = message.from_user.full_name
        db.add_user(user_id, user_full_name)
        await message.answer("salom admin", reply_markup=all_users_button)
    else:
        db.create_table_users()
        user_id = message.from_user.id
        user_full_name = message.from_user.full_name
        db.add_user(user_id, user_full_name)
        await message.answer("salom", reply_markup=ReplyKeyboardMarkup())



@dp.message(F.text == "hammalarni korish")
async def get_all_users(message: types.Message):
    all_users = db.select_user()
    my_list = []
    for user in all_users:
        my_list.append(f"ID: {user[0]}  ism: {user[1]}")
    await message.answer(f"{"\n".join(my_list)}")




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
