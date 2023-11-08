import discord
from discord.ext import commands
import os
import mysql.connector

from checkPing import bot_ping
from fetchData import fetch_data

#=================================================================


DB_HOST = str(os.environ["DB_HOST"])
DB_USERNAME = str(os.environ["DB_USERNAME"])
DB_PASSWORD = str(os.environ["DB_PASSWORD"])
DB_DATABASE = str(os.environ["DB_NAME"])

connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_DATABASE,
    ssl_verify_identity=True,
    ssl_ca="/etc/ssl/certs/ca-certificates.crt"
)

print("Connected to PlanetScale DB...:", connection.is_connected())

#create cursors to connect and interact with DB
cursor = connection.cursor(dictionary=True)

flag=True

#=================================================================

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('.'),intents=discord.Intents.all())

    async def on_ready(self):
        print(f'Logged in as {self.user.name}') # ----------------------- add timestamp later 
        synced = await self.tree.sync()
        custom_status = discord.Game(name="with data")
        await client.change_presence(activity=custom_status,status=discord.Status.idle)
        print(f'Slash commands synced: {len(synced)}')

client = Client()


                #PING
@client.tree.command(name='ping',description='Check the bot\'s present latency')
async def ping_check(interaction:discord.Interaction):
    await bot_ping(interaction,client)
    return




                #GET ALL DATA OF TABLE
@client.tree.command(name='all_data',description='Get all data there is')
async def send_data(interaction:discord.Interaction,filter:str=None):
    await fetch_data(interaction,cursor,filter)
    return


#===================================================================
client.run(str(os.environ['BOT_TOKEN']))
