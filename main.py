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
    print(f"{client.user} has connected to Discord!")

    #================ Roles ===================

    roles_list = ["Name"]
    members_list = []
    members_dict = {}
    data = []

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
    csv_name = "members_in_roles.csv"
    df.to_csv(f"data/{csv_name}", index=False)
    print(f"success save file {csv_name}")

    #================ Channal ===================

    ArrayList = []
    MemberList = []
    TextChannelNameList = ["Name"]
    TextChannelMemberDict = {}

    for member in guild.members:
        if member.bot == False:
            MemberList.append(member.name)

    TextChannels = guild.text_channels
    for TextChannel in TextChannels:
        TextChannelMemberList = []
        TextChannelName = TextChannel.name
        TextChannelNameList.append(TextChannelName)
        for TextChannelMember in TextChannel.members:
            if TextChannelMember.bot == False:
                TextChannelMemberList.append(TextChannelMember.name)
        TextChannelMemberDict[TextChannelName] = TextChannelMemberList

    for key, val in TextChannelMemberDict.items():
        ArrayList.append([key] + val)

    TextChannelMemberDict = {}

    for MemberName in MemberList:
        data = []   
        for Datalist in ArrayList:
            if MemberName in Datalist:
                data.append(Datalist[0])
            TextChannelMemberDict[MemberName] = data
         
    df = pd.DataFrame(columns=TextChannelNameList)

    for name in TextChannelMemberDict:
        data = []
        for role in TextChannelNameList:
            if role in TextChannelMemberDict[name]:
                data.append(1)
            else:
                data.append(0)
        data[0] = name
        df.loc[len(df.index)] = data

    df = df.sort_values(by=["Name"])
    csv_name = "members_in_channels.csv"
    df.to_csv(f"data/{csv_name}", index=False)
    print(f"success save file {csv_name}")

client.run(DISCORD_TOKEN)

