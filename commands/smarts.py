
from pprint import pprint
from decouple import config
import requests
from discord.ext import commands

class Smarts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.reply(f'*Pong!* - **Latência de {round(self.bot.latency * 1000)}ms **')


    @commands.command(name='tempo')
    async def get_city_temperature(self, ctx, *args):
        cidade = ' '.join(args)
        print(cidade)
        API_TEMPO = 'ec5eb2abed5765d5372423e4d3a0cdfa'
        req = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+cidade+"&appid="+API_TEMPO+"&lang=pt_br")

        try:
            cidade = req.json()['name']
            termica_sensacao = int(req.json()['main']['feels_like'] - 273.15)
            temperatura = int(req.json()['main']['temp'] - 273.15)
            max_temperatura = int(req.json()['main']['temp_max'] - 273.15)
            min_temperatura = int(req.json()['main']['temp_min'] - 273.15)

            condicao_tempo = req.json()['weather'][0]['description']
            velocidade_vento = req.json()['wind']['speed']
            angulo_vento = req.json()['wind']['deg']

            await ctx.send(f'*{cidade.upper()} está atualmente com temperatura de {temperatura}°C (máxim: {max_temperatura}°C, e mínima: {min_temperatura}°C). A sensação térmica é de {termica_sensacao}°C, e as condições do tempo é {condicao_tempo}, com ventos de {velocidade_vento}Km/h a {angulo_vento}°.*')

            if temperatura > 15:
                await ctx.send('Essa temperatura é quente pra flamingos 🔥🌡️☀️.')
            else:
                await ctx.send('Essa temperatura é fria pra flamingos ❄️☃️🌨️.')


        except Exception as error:
            print('Erro: ', error)
            print('Infelizmente não foi possível verificar essa cidade no momento. Verifique se o nome da cidade está correto, meu nobre.')
            

        

    
        
    

async def setup(bot):
    await bot.add_cog(Smarts(bot))