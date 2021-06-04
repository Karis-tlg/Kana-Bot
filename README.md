# Basic Discord Bot

Intended to be a starting point for experimenting with [discord.py](https://discordpy.readthedocs.io/en/stable/) bots in a replit (depends on [replit-db](https://github.com/replit/replit-py)).

Combines various snippets and features from tutorials, Replit templates and [discord.py](https://discordpy.readthedocs.io/en/stable/) docs.

WIP

### Setup

Store bot secret token and owner id in env vars called `TOKEN` and `BOT_OWNER_ID` respectively as in `.env.example` file.

Command prefix and enabled extensions can be configured in settings.py

### Usage

`python run.py`

Also run flask web server to keep a Repl alive: 

`python run.py --keepalive`


### Project Structure
Settings are stored in a `settings.py` file. Management commands can be added to `run.py` using [click](https://click.palletsprojects.com/). Extensions packages or modules can be placed in the extensions folder.

### Extensions
- admin - manage `discord.py` extensions
- economy - extremely minimal virtual currency extension using replit-db
- encouragements - encouragements bot from freecodecamp tutorial (see below) put into a cog and extension
- greetings - minimal greetings bot verbatim from `discord.py` docs

### Contributing

[https://github.com/bk62/basic-discord-bot](https://github.com/bk62/basic-discord-bot)

[https://replit.com/@bk62/Basic-Discord-Bot](https://replit.com/@bk62/Basic-Discord-Bot)

### References

+ https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ (starting point for `extensions.encouragements`)
+ https://replit.com/@templates/Discordpy-bot-template-with-commands-extension (starting point for `extensions.admin`)
+ https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html and  https://github.com/Rapptz/discord.py/tree/v1.7.2/examples (starting point for `extensions.economy` and `extensions.greetings`)

### License
[MIT](https://choosealicense.com/licenses/mit/)