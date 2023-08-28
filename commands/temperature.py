
from pprint import pprint
from decouple import config
import requests
from discord.ext import commands

class Temperature(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='reka')
    async def camus(self, ctx):
        await ctx.send('A REKA é a CHEF dos Flamingos 🦩🦩🦩.')

    @commands.command(name='camus')
    async def camus(self, ctx):
        await ctx.send('Camus é o meu desenvolvedor.')


    @commands.command(name='tempo')
    async def load_clips(self, ctx, *args):
        city = args[0]
        req = requests.get('https://api.api-ninjas.com/v1/geocoding?city='+city, headers={'X-Api-Key': '8zF4dEsOBx4cfzqQ4Pc8Xw==7VukABeFVan7N5R9'})
        cidade = req.json()[0]
        lat, long = cidade['latitude'], cidade['longitude']

        req = requests.get('https://api.open-meteo.com/v1/dwd-icon?latitude='+str(lat)+'&longitude='+str(long)+'&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')


        humidade_relativa = req.json()['hourly']['relativehumidity_2m'][0]
        temperatura = req.json()['hourly']['temperature_2m'][0]
        horario = req.json()['hourly']['time'][0]
        vento_velocidade = req.json()['hourly']['windspeed_10m'][0]

        await ctx.send(f'*{city.upper()}, está atualmente com Temperatura de {temperatura}°C, Humidade relativa de {humidade_relativa}% e ventos a {vento_velocidade} km/h.* Resgistrado em {horario}.')
        
        if temperatura > 15:
            await ctx.send('Essa temperatura é quente pra flamingos 🔥🌡️☀️.')
        else:
            await ctx.send('Essa temperatura é fria pra flamingos ❄️☃️🌨️.')
        
    

async def setup(bot):
    await bot.add_cog(Temperature(bot))