
import random
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

    @commands.command(name='reka')
    async def camus(self, ctx):
        await ctx.send('A REKA é a CHEF dos Flamingos 🦩🦩🦩.')


    @commands.command(name='oi')
    async def send_hi(self, ctx):
        username = ctx.author.name
        response = 'Olá! '+ username
        await ctx.send(response)
    
    @commands.command(name='segredo')
    async def send_hi(self, ctx):
        #print('comando segredo')
        resp_list=[
            (f'{ctx.author.name}, eu não posso contar aqui, só no privado - *através do comando !privado*'),
            ('Meia-noite eu te conto!')
        ]
        await ctx.send(random.choice(resp_list))

    @commands.command(name='privado')
    async def send_private(self, ctx):
        #print('comando privado')
        try:
            await ctx.author.send('Então você quer saber qual é o segredo, não é mesmo?')
            await ctx.author.send('o segredo é ...')
            await ctx.author.send('||Meia-noite eu te conto!||')
        except discord.errors.Forbidden:
            await ctx.send('*Não consigo te contar o segredo, sua configuração de mensagens não permite. :/*')
        

    
        
    

async def setup(bot):
    await bot.add_cog(Talks(bot))