from pprint import pprint

import discord
from discord.ext import commands

import formater
from tk import token
from datetime import datetime, timedelta

import ruz

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.event
async def on_ready():
    print("Ready!")


@bot.command()
async def get_file(ctx):
    def check_func(message: discord.Message) -> bool:
        return message.author == ctx.author and message.content in ("1", "2", "3")

    keys_of_materials = {
        'Все лекции за 1 семестр | АИП': "./data/materials/lektsii1semestr.pdf",
        'Все лекции за 2 семестр | АИП': "./data/materials/lektsii2semestr.pdf",
        'Лабароторные работы 3 модуль | АИП': "./data/materials/laba3modul.docx",
    }

    list_of_keys = """"""

    for i in range(len(list(keys_of_materials.keys()))):
        list_of_keys = list_of_keys + str(i + 1) + ". " + list(keys_of_materials)[i] + '\n'

    mes = "Выберите материал: \n" + list_of_keys
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


bot.run(token)
