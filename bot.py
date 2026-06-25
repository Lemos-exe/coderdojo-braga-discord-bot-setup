import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot ligado como {bot.user}")

@bot.command()
async def ola(ctx):
    await ctx.send("Olá!")

token=(token_aqui)

if not token:
    raise RuntimeError("DISCORD_TOKEN nao definido no ambiente")

bot.run(token)