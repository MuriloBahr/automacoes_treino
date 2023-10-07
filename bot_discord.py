from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = True
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')
    mensagem_padrao = "OI MARIO FERNANDES"
    canal = discord.utils.get(bot.get_all_channels(), name='💬┃chat-staff')
    if canal:
        print(f'Encontrou o canal: {canal.name}')
        await canal.send(mensagem_padrao)
    else:
        print('ERROR: Canal nao encontrado')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!enviar'):
        mensagem = message.content[len('!enviar'):].strip()
        await message.channel.send(f'Enviando a mensagem: "{mensagem}"')

token = 'MTExODY2MjAwMzk2ODQ1ODk5Mg.G5gcks.CkrmkAplvb8jQoVEBXHwQ4AhnG7UCYRnpg9C0Q'
bot.run(token)