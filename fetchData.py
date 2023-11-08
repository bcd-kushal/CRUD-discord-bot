import discord
import os

from sendEmbed import send_embed


def search_my_table(table: list, filter: str = None):
    result = {}
    i = 0

    filter = "" if filter is None else filter.lower()

    res = ""

    for row in table:
        aux = ""
        flag = False
        for key, val in row.items():
            aux += f".   ╰ **{key}:** \t\t{val}\n"
            flag = True if filter == "" else True if filter in str(val).lower() else False

        if flag:
            res += f"\n〓 **Row {i+1}** 〓"
            res += f"\n{aux}"
            i += 1
            print()

    return res+"\n"
    """
    for key, value in table.items():
        if isinstance(value, dict):
            sub_result = search_my_table(value, filter)
            if sub_result:
                result[key] = sub_result
        elif filter in value:
            result[key] = value
    return result
    """


async def fetch_data(interaction: discord.Interaction,cursor,filter: str = None):
    await interaction.response.send_message(content='_fetching..._',ephemeral=False)

    filter = "" if filter is None else filter.lower()

    #await bot_ping(interaction,client)
    #get all data from cursor
    if (filter == "" or filter == None):
        cursor.execute(f"SELECT * FROM {str(os.environ['TABLE_NAME'])};")
    else:
        query = f"SELECT * FROM {str(os.environ['TABLE_NAME'])} WHERE "

        cursor.execute(f"SELECT * FROM {str(os.environ['TABLE_NAME'])} WHERE 'productName' like '%{filter}%'")

    data = cursor.fetchall()

    print(data)


    res = search_my_table(data, filter)
    await send_embed(ctx=interaction, title="My Data", desc=res)
    return
    """
    res=""
    i=1

    for row in data:
        res+=f"〓 Row {i} 〓\n"
        for key,val in row.items():
            print(f"{key}: {val}")
            res+=f".   ╰ **{key}:** \t\t{val}\n"
        res+="\n"
        print()
        i+=1

    await send_embed(ctx=interaction,title="My Data",desc=res)
    """
