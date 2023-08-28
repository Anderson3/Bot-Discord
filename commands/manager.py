
import random
from discord.ext import commands

class Manager(commands.Cog):
    #Código gerenciador do Bot
    def __init__(self, bot):
        self.bot = bot
    

    #Inicialização do Bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou pronto! Estou conectado como {self.bot.user}')
        
    
    #Impedir o Bot ver as próprias mensagens
    # Filtro de Palavras do Bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if 'guara' in message.content or 'guará' in message.content:
            list_resp = [
                (f'Desculpe, querido(a) {message.author.name}, mas eu não sou um Guará. \nEU SOU UM FLAMINGO!'),
                (f'Eu sou outro tipo de ave.'),
                (f'Amigo, eu sou um *Phoenicopterus*, esses ai são *Eudocimus*'),
                (f'{message.author.name}, você está querendo arranjar briga comigo? \nVem Tranquilo ...'),
            ]
            await message.channel.send(random.choice(list_resp))
        
        
        

        
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print('- comando inexistente')
        print('Erro: ', error)
        #await ctx.send('Comando inexistente.')


    

async def setup(bot):
    await bot.add_cog(Manager(bot))
