
import discord
from discord.ext import commands

class Clips(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='carregar_clip')
    async def load_clips(self, ctx):
        #Implementar API para captura de clips
        await ctx.send('Erro - Verifique o Log de registro no terminal')
        await ctx.send('Desculpe, comando ainda não implementado.')
        await ctx.send('Tomar Nota:  caso não conseguir api livre da twitch, gerar um db sqlite3 com links dos clipes para administração pelo bot.')


    

async def setup(bot):
    await bot.add_cog(Clips(bot))