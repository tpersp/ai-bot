import discord
from discord.ext import commands
from bot.utils.ai_client import chat_with_ai

class ChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if not self.bot.is_ready():
            return

        # Example: Only respond if bot is mentioned, or channel is whitelisted (expand as needed)
        if self.bot.user in message.mentions:
            context = [{"role": "user", "content": message.content}]
            ai_reply = chat_with_ai(context)
            await message.channel.send(ai_reply)

def setup(bot):
    bot.add_cog(ChatCog(bot))
