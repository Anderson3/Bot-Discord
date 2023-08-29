
import random
import discord
from discord.ext import commands

class Talks(commands.Cog):

    # Conversar com o usuário
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='teste')
    async def test(self, ctx):
        await ctx.reply('Ta testado.')

    @commands.command(name='oi')
    async def send_hi(self, ctx):
        username = ctx.author.name
        response = 'Olá! '+ username
        await ctx.send(response)
    
    @commands.command(name='reka')
    async def reka(self, ctx):
        resp_list=[
            ('A REKA é a CHEF dos Flamingos 🦩🦩🦩.'),
            ('A Reh é a Rainha das utilitárias do CS.'),
            ('Ela quem manda e desmanda nesse servidor ...'),
            #(':rekathREKA:'),
            ('REKA KAREKA kakakakakakaakak'),
            ('Ela imita a voz do Google melhor que a mulher do Google.'),
        ]
        await ctx.send(random.choice(resp_list))
    
    @commands.command(name='rafa')
    async def rafa(self, ctx):
        resp_list=[
            ('A Raffa é uma amor de pessoa.'),
            ('Melhor Moderadora da live.'),
            ('Uma pessoa alegre, simpática e acolhedora.'),
        ]
        await ctx.send(random.choice(resp_list))
    
    @commands.command(name='camus')
    async def camus(self, ctx):
        resp_list=[
            ('O Camus é meu desenvolvedor.'),
            ('*Aquele nerd chato que vive comendo livros.*'),
            ('(...) Toníco, Chocotonione, Toni, 21pillots - *toda live chamam ele de um nome diferente.*'),
            ('quero saber quando esse cara vai querer atualizar meu código de novo, ta faltando implementar coisas ainda!'),
        ]
        await ctx.send(random.choice(resp_list))
    
    @commands.command(name='segredo')
    async def send_hi(self, ctx):
        #print('comando segredo')
        resp_list=[
            (f'{ctx.author.name}, eu não posso contar aqui, só no privado - *através do comando !privado*'),
            (f'Ai {ctx.author.name}, isso é confidencial, não sei se devo te contar. Mas tenta novamente.'),
            ('Meia-noite eu te conto!')
        ]
        await ctx.send(random.choice(resp_list))

    @commands.command(name='privado')
    async def send_private(self, ctx):
        #print('comando privado')
        try:
            await ctx.author.send('Então você quer saber qual é o segredo, não é mesmo?')
            await ctx.author.send('bem ...')
            await ctx.author.send('o segredo é ...')
            await ctx.author.send('||MEIA-NOITE EU TE CONTO!!!||')
        except discord.errors.Forbidden:
            await ctx.send('*Não consigo te contar o segredo, sua configuração de mensagens não permite que eu envie mensagens para você. :/*')
        
        

    
        
    

async def setup(bot):
    await bot.add_cog(Talks(bot))