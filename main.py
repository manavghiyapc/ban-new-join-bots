import discord
from datetime import datetime, timedelta, timezone

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

    guild_id = 864766766932426772
    guild = client.get_guild(guild_id)
    if guild is None:
        print(f"Guild with ID {guild_id} not found.")
        return

    print("Scanning members...")
    now = datetime.now(timezone.utc)
    for member in guild.members:
        account_age = now - member.created_at
        join_age = now - member.joined_at

        if (
            timedelta(days=780) < account_age < timedelta(days=781) and
            timedelta(days=1) < join_age < timedelta(days=2)
        ):
            print(f"{member.id}")

    print("Done.")
    

client.run('token')
