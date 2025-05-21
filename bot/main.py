import discord
from discord.ext import commands
from bot.utils.config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs
bot.load_extension("bot.cogs.chat")
bot.load_extension("bot.cogs.memory")

@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
