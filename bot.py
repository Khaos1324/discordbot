from __future__ import unicode_literals
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.ext import commands
import discord
import random
import asyncio
import json
import os
import secrets
import time
import asyncio




client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Current ping: {round(client.latency * 1000)}ms')

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)

client.run("NzA4NTk5NDY3MzIyMTE0MTI4.XrZsvQ.4hy7ANOZppdibc38skIy8haqjpM")
