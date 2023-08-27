import discord
from discord.ext import commands

class Talks(commands.Cog):
    # Conversar com o usuário
    def __init__(self, bot):
        self.bot = bot
    
    # Aplicação de Comandos
    @commands.command(name='camus')
    async def camus(self, ctx):
        await ctx.send('Camus é o meu desenvolvedor.')

    @commands.command(name='oi')
    async def send_hi(self, ctx):
        name = ctx.author.name
        response = 'Olá! '+ name
        await ctx.send(response)
    
    @commands.command(name='segredo')
    async def send_hi(self, ctx):
        #print('comando segredo')
        await ctx.send('Meia-noite eu te conto!')

    @commands.command(name='privado')
    async def send_private(self, ctx):
        #print('comando privado')
        await ctx.author.send('Então você quer saber qual é o segredo, não é mesmo?')
        await ctx.author.send('o segredo é ...')
        await ctx.author.send('||Meia-noite eu te conto!||')
    

async def setup(bot):
    await bot.add_cog(Talks(bot))