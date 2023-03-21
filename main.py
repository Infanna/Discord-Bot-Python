import discord
import pandas as pd
from dotenv import dotenv_values

config = dotenv_values(".env")
DISCORD_TOKEN = config["DISCORD_TOKEN"]
GUILD_ID = int(config["GUILD_ID"])

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    roles_list = ["Name"]
    members_list = []
    members_dict = {}
    data = []

    print(f"{client.user} has connected to Discord!")

    guild = client.get_guild(GUILD_ID)

    roles = guild.roles
    for role in roles:
        if role.is_bot_managed() == False:
            roles_list.append(role.name)

    df = pd.DataFrame(columns=roles_list)

    members = guild.members
    for member in members:
        if member.bot == False:
            for r in member.roles:
                members_list.append(r.name)
            members_dict[member.name] = members_list
        members_list = []

    for name in members_dict:
        for role in roles_list:
            if role in members_dict[name]:
                data.append(1)
            else:
                data.append(0)
        data[0] = name
        df.loc[len(df.index)] = data
        data = []

    df = df.sort_values(by=["Name"])
    df.to_csv("data/member.csv", index=False)
    print("success")


client.run(DISCORD_TOKEN)
