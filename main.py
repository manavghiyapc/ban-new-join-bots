import discord
import os
from datetime import datetime, timedelta, timezone

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

    guild_id = 864766766932426772
    role_id = 1228604532469141504
    guild = client.get_guild(guild_id)
    if guild is None:
        print(f"Guild with ID {guild_id} not found.")
        return

    print("Scanning members...")
    for member in guild.members:
        if (
            (datetime.now(timezone.utc) - member.created_at > timedelta(days=764)) and
            (datetime.now(timezone.utc) - member.created_at < timedelta(days=765)) and
            (any(role.id == role_id for role in member.roles))
        ):
            print(f"{member.id}")

    print("Done.")
    
token = os.environ['TOKEN']
client.run(token)
