from redbot.core import commands

from .rss import IFIRSS

__red_end_user_data_statement__ = "This cog does not persistently store data or metadata about users."


async def setup(bot: commands.Bot):
    n = IFIRSS(bot)
    bot.add_cog(n)
    n.initialize()
