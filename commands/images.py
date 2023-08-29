
import random
from pexels_api import API
from decouple import config

import discord
from discord.ext import commands


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='flamingo')
    async def get_flamingo(self, ctx):

        PEXELS_API_KEY = config('PEXELS_API_KEY')
        p_api = API(PEXELS_API_KEY)
        p_api.search('flamingo', page=random.randint(0,5), results_per_page=10)
        photos = p_api.get_entries()

        photo = photos[random.randint(0,len(photos))]
        print('Photographer: ', photo.photographer)
        print('Photo original size: ', photo.original)
        print(photo)

        url_image = photo.original
        name_photographer =  photo.photographer

        embed = discord.Embed(
            title = 'Flamingos',
            #description = 'flamingos aleatórios',
            color=0x00BFFF,
        )

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        embed.set_footer(text='Flamingo bolado')

        embed.add_field(name='Descrição', value='Uma imagem aleatória de um ou mais membros da minha família.')
        embed.add_field(name='Fonte', value=name_photographer)
        embed.add_field(name='Imagem', value=url_image, inline=False)

        embed.set_image(url=url_image)

        await ctx.send(embed = embed)
    

    @commands.command(name='imagem')
    async def get_image(self, ctx, *args):

        imagem_pesq = args[0]

        PEXELS_API_KEY = config('PEXELS_API_KEY')
        p_api = API(PEXELS_API_KEY)
        p_api.search(imagem_pesq, page=random.randint(0,5), results_per_page=10)
        photos = p_api.get_entries()

        photo = photos[random.randint(0,len(photos))]
        print('Photographer: ', photo.photographer)
        print('Photo original size: ', photo.original)
        print(photo)

        url_image = photo.original
        name_photographer =  photo.photographer

        embed = discord.Embed(
            title = str(imagem_pesq),
            #description = 'flamingos aleatórios',
            color=0x00BFFF,
        )

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        embed.set_footer(text='Flamingo bolado')

        embed.add_field(name='Descrição', value=f'Uma imagem aleatória sobre {imagem_pesq}.')
        embed.add_field(name='Fonte', value=name_photographer)
        embed.add_field(name='Imagem', value=url_image, inline=False)

        embed.set_image(url=url_image)

        await ctx.send(embed = embed)



async def setup(bot):
    await bot.add_cog(Images(bot))