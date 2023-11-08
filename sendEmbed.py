import discord 
import os
from datetime import datetime

async def send_embed(ctx, desc, title=None, col=None, add_fld:dict=None, thumbnail=None, img=None, author:list=None, footer:list=None):
    if(not col):
        col = discord.Color.blurple()

    embed = discord.Embed(
        title=title if ((not None) or len(title)>0) else None,
        description=desc,
        color=col
    )

    if(add_fld):
        for key,val in add_fld.items():
            embed.add_field(name=str(key),value=str(val),inline=False)

    if(thumbnail):
        embed.set_thumbnail(url=str(thumbnail))

    if(author):
        embed.set_author(
            name=str(author[0]),
            icon_url=str(author[1]) if len(author)>1 else None
        )

    if(not footer):
        embed.set_footer(
            text=f"database: {str(os.environ['TABLE_NAME'])}",
            icon_url="https://www.shutterstock.com/image-vector/database-icon-simple-linear-symbol-600w-1115643338.jpg"
        )

    embed.timestamp = datetime.now()


    await ctx.followup.send(embed=embed)