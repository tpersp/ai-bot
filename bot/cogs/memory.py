from discord.ext import commands
from db.models import get_session, UserMemory

class MemoryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        session = get_session()
        user_mem = session.query(UserMemory).filter_by(discord_id=str(message.author.id)).first()
        if not user_mem:
            user_mem = UserMemory(discord_id=str(message.author.id), memory="")
            session.add(user_mem)
        user_mem.memory = (user_mem.memory or "")[-1000:] + "\n" + message.content  # Simple append, limit size
        session.commit()

def setup(bot):
    bot.add_cog(MemoryCog(bot))
