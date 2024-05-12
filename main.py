import discord
from discord.ext import commands

from open_list_of_educators import get_names
from tk import token

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
    pass
bot.run(token)
