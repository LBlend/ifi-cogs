from redbot.core import commands

from .course_channel import CourseChannel

__red_end_user_data_statement__ = "This cog does not persistently store data or metadata about users."


async def setup(bot: commands.Bot):
    cog = CourseChannel(bot)
    bot.add_cog(cog)
