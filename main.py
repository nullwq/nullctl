import discord
import os
import asyncio
from typing import Optional

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
#multiply
@bot.command()
async def multiply(ctx, num1: float, num2: float):
   result = num1 * num2
   await ctx.send(f"The answer of {num1} multiplied by {num2} is {result}")

#addition
@bot.command()
async def add(ctx, num1: float, num2: float):
   result = num1 + num2
   await ctx.send(f"The answer of {num1} + {num2} is {result}")

#Subtract
@bot.command()
async def Subtract(ctx, num1: float, num2: float):
   result = num1 - num2
   await ctx.send(f"The answer of {num1} Subtracted by {num2} is {result}")

#divided
@bot.command()
async def divide(ctx, num1: float, num2: float):
   result = num1 / num2
   await ctx.send(f"The answer of {num1} divided by {num2} is {result}")
   
   



#token
bot.run(token)




