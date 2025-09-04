import os
import discord
from dotenv import load_dotenv

# load environment and get the Bot token from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# setup client with default intents
intents = discord.Intents().all()
client = discord.Client(intents=intents)

# see if you can connect
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)