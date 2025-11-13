import discord
import os
import asyncio

bot = commands.Bot(command_prefix='stv!' intents=intents

# event
@bot.event
async def on_ready():
print("I am working")

#command
#ping
latency_ms = round(bot.latency * 1000)
@bot.command()
async def ping():
   await ctx.send(f"pong! my ping is {laency_ms}")
#invites
@bot.command()
async def create(args):
   await ctx.send("I am not ready yet Stop trying to use me")




#token
bot.run(token)



