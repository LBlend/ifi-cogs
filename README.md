# ifi-cogs

Cogs used for managing the Institute for Informatics @ University of Oslo Discord server.

This repo modifies the RSS cog from [aikaterna-cogs](https://github.com/aikaterna/aikaterna-cogs) to suit the needs of the server. Because of this, I have decided to fork the repo.

## Cogs

### coursechannel

The coursechannel cog allows for the creation of "course channels". It creates a channel with the name of a given course code and adds the course name as its description

### ifirss

ifirss is a modification of akiterna's rss cog and adds a couple of commands for fetching and deleting course feeds. Course feeds are RSS feeds containing updates about the course. These modifications attempts to automate the process of adding and removing these feeds based on channel names and the current time of year.
