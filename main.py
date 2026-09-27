import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# PASTDAGI QO'SHTIRNAQ ICHIGA BOTFATHER'DAN OLGAN TOKENINGIZNI QO'YING:
BOT_TOKEN = "BU_YERGA_TOKENINGIZNI_TASHLANG"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Bot ekranidagi tugmalar
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ℹ️ Biz haqimizda"), KeyboardButton(text="📞 Aloqa")],
        [KeyboardButton(text="📝 Savol yuborish")]
    ],
    resize_keyboard=True
)

# /start bosilganda
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.first_name}!\n\n"
        f"Men @abdukar1mov_bot yordamchisiman. Kerakli bo'limni tanlang:",
        reply_markup=main_keyboard
    )

# Tugmalar bosilganda qaytadigan javoblar
@dp.message(F.text == "ℹ️ Biz haqimizda")
async def info_btn(message: types.Message):
    await message.answer("Bu bot shaxsiy murojaatlar va savollarni qabul qilish uchun yaratilgan.")

@dp.message(F.text == "📞 Aloqa")
async def contact_btn(message: types.Message):
    await message.answer("Bog'lanish uchun: @abdukarimov (shaxsiy profilingiz)")

@dp.message(F.text == "📝 Savol yuborish")
async def ask_btn(message: types.Message):
    await message.answer("Savolingizni yozib qoldiring, tez orada javob beramiz.")

# Foydalanuvchi oddiy matn yozsa
@dp.message(F.text)
async def echo_msg(message: types.Message):
    await message.answer("Xabaringiz qabul qilindi! Rahmat, tez orada javob beramiz.")

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
