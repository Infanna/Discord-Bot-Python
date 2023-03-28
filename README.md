# Discord-Bot-Python
step to use script get members detail in discord
1. Install python virtual environment
   ```
   python3 -m venv env
   ```
2. Enter env and install libary
   ```
   source env/bin/activate
   pip install -r requirements.txt
   ```
3. Create a folder for storing data
   ```
   mkdir data
   ```
4. Create your discord bot follow with [How to Get a DISCORD_TOKEN](https://www.writebots.com/discord-bot-token)
   and add bot in your discord server
5. Get GUILD_ID follow with [How to Get a Discord GUILD_ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-#:~:text=Obtaining%20Server%20IDs%20%2D%20Mobile%20App,name%20and%20select%20Copy%20ID.)
6. Change DISCORD_TOKEN and GUILD_ID in .env file
   ```
   DISCORD_TOKEN="your-token"
   GUILD_ID="your-server-id"
   ```
