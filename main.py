from pprint import pprint

import discord
from discord.ext import commands

import formater
import teachers
from tk import token
from datetime import datetime, timedelta

import ruz

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

keys_of_materials = {
    'Все лекции за 1 семестр | АИП': "./data/materials/lektsii1semestr.pdf",
    'Все лекции за 2 семестр | АИП': "./data/materials/lektsii2semestr.pdf",
    'Лабароторные работы 3 модуль | АИП': "./data/materials/laba3modul.docx",
}


help_msg = """
Доступные команды:
>bot_help  - Доступные команды
>get_file - Получить файл, который необходим пользователю
>get_schedule_today <email> - Выводит расписание на сегодня
>get_schedule_tomorrow <email> - Выводит расписание на завтра
>get_schedule_week <email> - Выводит расписание на неделю - считая с сегодняшнего дня
>get_teacher - Получить информацию о преподавателях"""

@bot.event
async def on_ready():
    print('Бот готов к работе')



@bot.command()
async def bot_help(ctx):
    await ctx.send(help_msg)


@bot.command()
async def get_file(ctx):
    def check_func(message: discord.Message) -> bool:
        return message.author == ctx.author and message.content in ("1", "2", "3")

    mes = "Выберите материал: \n" + formater.format_mes(keys_of_materials)
    await ctx.send(mes)
    user_message: discord.Message = await bot.wait_for('message', check=check_func, timeout=None)
    if user_message.content == "1":
        spr_file = "./data/materials/lektsii1semestr.pdf"
    elif user_message.content == "2":
        spr_file = "./data/materials/lektsii2semestr.pdf"
    else:
        spr_file = "./data/materials/laba3modul.docx"
    await ctx.send(file=discord.File(spr_file))

    # await user_message.reply(f'Hello, {user_message.author.mention}!')


@bot.command()
async def get_teacher(ctx):
    def check_func(message: discord.Message) -> bool:
        return message.author == ctx.author and message.content in ("1", "2", "3", "4", "5", "6", "7", "8", "9")

    mes = "Выберите преподавателя, с которым хотите связаться: \n" + teachers.get_teachers()
    await ctx.send(mes)
    user_message: discord.Message = await bot.wait_for('message', check=check_func, timeout=None)
    ans = teachers.get_teacher_info(int(user_message.content))
    await ctx.send(ans)



@bot.command()
async def get_schedule_today(ctx, email=None):
    if email == None:
        await ctx.send("Вы не ввели email :/\nПопробуйте еще раз")
    elif not ruz.email_is_valid(email):
        await ctx.send("Email введен некорректно :/\nВведите адрес от вашей вышкинской почты")
    else:
        today = datetime.today()
        formatted_date = today.strftime("%Y-%m-%d")
        schedule_not_formated = ruz.get_student_schedule(email, formatted_date, formatted_date, 1)
        schedule_formated = formater.format_schedule_one_day(schedule_not_formated)
        if schedule_formated != "В этот день нет пар, отдыхаем!":
            await ctx.send(f"Пары на сегодня:\n{schedule_formated}")
        else:
            await ctx.send("В этот день нет пар, отдыхаем!")


@bot.command()
async def get_schedule_tomorrow(ctx, email=None):
    if email == None:
        await ctx.send("Вы не ввели email :/\nПопробуйте еще раз")
    elif not ruz.email_is_valid(email):
        await ctx.send("Email введен некорректно :/\nВведите адрес от вашей вышкинской почты")
    else:
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        formatted_date = tomorrow.strftime("%Y-%m-%d")
        schedule_not_formated = ruz.get_student_schedule(email, formatted_date, formatted_date, 1)
        schedule_formated = formater.format_schedule_one_day(schedule_not_formated)
        if schedule_formated != "В этот день нет пар, отдыхаем!":
            await ctx.send(f"Пары на завтра:\n{schedule_formated}")
        else:
            await ctx.send("В этот день нет пар, отдыхаем!")


@bot.command()
async def get_schedule_week(ctx, email=None):
    if email == None:
        await ctx.send("Вы не ввели email :/\nПопробуйте еще раз")
    elif not ruz.email_is_valid(email):
        await ctx.send("Email введен некорректно :/\nВведите адрес от вашей вышкинской почты")
    else:
        today = datetime.today()
        week = today + timedelta(days=7)
        formatted_date_today = today.strftime("%Y-%m-%d")
        formatted_date_week = week.strftime("%Y-%m-%d")
        schedule_not_formated = ruz.get_student_schedule(email, formatted_date_today, formatted_date_week, 1)
        schedule_formated = formater.format_schedule_active(schedule_not_formated)

        if schedule_formated != "Сейчас нет пар":
            await ctx.send(f"Пары с {formatted_date_today} по {formatted_date_week}:\n")
            for elem in schedule_formated:
                await ctx.send(elem)

        else:
            await ctx.send("Сейчас нет пар")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Похоже, такой команды не существует. Введите >bot_help для списка доступных команд.")

bot.run(token)
