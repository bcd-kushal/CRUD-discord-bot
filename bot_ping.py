import discord
import time 

async def bot_ping(interaction:discord.Interaction,client):
    start_time = time.time()
    await interaction.response.send_message(content='_pinging..._',ephemeral=True)
    end_time = time.time()
    latency = (end_time-start_time)*1000

    embed = discord.Embed(
        description=f':ping_pong: **Pong!**\nBot latency: **{client.latency * 1000:.0f}ms**\nMessage latency: **{latency:.0f}ms**',
        color=discord.Color.dark_orange()
    )
    await interaction.edit_original_response(content="",embed=embed)