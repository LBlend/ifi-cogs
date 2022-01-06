from redbot.core import commands
from redbot.core.bot import Red

from datetime import datetime
import re
import requests


class CourseChannel(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    def _get_semesters(self):
        """
        Get the next, previous and current semester code based on current date.
        """

        now = datetime.now()
        current_year = int(str(now.year)[-2:])

        if now.month < 8:
            previous_sem = f"{current_year - 1}h"
            current_sem = f"{current_year}v"
            next_sem = f"{current_year}h"
        else:
            previous_sem = f"{current_year}v"
            current_sem = f"{current_year}h"
            next_sem = f"{current_year + 1}v"

        return next_sem, current_sem, previous_sem

    @commands.guild_only()
    @commands.command(name="coursechannel")
    async def _coursechannel(self, ctx: commands.Context, *, course_code: str):
        """
        Create a course channel for a given course code.

        This command will fetch the course name, create a channel with the course code as its name and attempt to place it in the correct category.
        """

        is_valid_course = re.search(r"^[a-zA-Z]+\d{4}", course_code)
        if not is_valid_course:
            await ctx.send("Invalid course code.")
            return

        semesters = self._get_semesters()
        found = False
        for semester in semesters:
            if found:
                break

            courses = requests.get(f"https://tp.uio.no/uio/ws/course/?id=185&sem={semester}").json()

            for course in courses["data"]:
                if course["id"] == course_code.upper():
                    found = True
                    course_name = course["name"]
                    break

        if not found:
            await ctx.send("Course not found.")
            return

        course_level = re.findall(r"([a-zA-Z]+)(\d{4})", course_code)[0][1][
            0
        ]  # Get the first digit of the course number code

        #  Hardcoded because fuck you.
        course_categories = {
            "1": 804048618205478982,
            "2": 804048709225939015,
            "3": 804049027339124766,
        }
        other = 804049077309538315

        category_id = course_categories.get(course_level, other)

        category = ctx.guild.get_channel(category_id)
        channel = await category.create_text_channel(
            f"{course_code}-diskusjon", reason="auto-generated course channel with command", topic=course_name
        )

        await ctx.send(f"Created channel {channel.mention} in {category.mention}")
