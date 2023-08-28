
import asyncio, os
import discord
from discord.ext import commands
from decouple import config

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='f!', intents=intents)

TOKEN = config('TOKEN')

async def load_extensions(bot):
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            print(f' - Carregado: {filename[:-3]}')
            await bot.load_extension(f"commands.{filename[:-3]}")

async def main():
    await load_extensions(bot)
    await bot.start(TOKEN)

asyncio.run(main())