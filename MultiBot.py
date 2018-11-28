#Bot made by Khaos1324

#List of imports
from __future__ import unicode_literals
import discord
import json
import os
import secrets
import time
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

players = {}
queues = {}

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')
os.chdir(r'C:\Users\Charl\Desktop\Discord Bot')

#Leveling Command


#Startup

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='.help for commands | In Develepment! :D'))
    print ("ready when you are xd")
    print ("i am running on " + bot.user.name)
    print ("with the ID" + bot.user.id)

from discord.ext import commands





#Voice Channel

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)

@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_bot = bot.voice_client_in(server)
    await voice_bot.disconnect()

@bot.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_bot = bot.voice_client_in(server)
    player = await voice_bot.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()
    
@bot.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@bot.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@bot.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@bot.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    bot_client = bot.voice_client_in(server)
    player = await bot_client.create_ytdl_player(url)

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await bot.say('Video Queued')



#Ping Command

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")

#Info command

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name),description="Here's what I could find:", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)






#Help Command

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Help",description="Here are all the commands for the bot", color=0x00ff00)
    embed.add_field(name=".help", value='Show the commands for the bot', inline=True)
    embed.add_field(name=".ping", value='A simple ping pong command', inline=True)
    embed.add_field(name=".info (username)", value='Shows information of the user on the server', inline=True)
    embed.add_field(name=".clear (#)", value='Clears messages ; Min = 2 Max = 100', inline=True)
    embed.add_field(name=".join", value='Makes the bot join the voice channel (You must be in one)', inline=True)
    embed.add_field(name=".play (YouTube Link)", value='Plays the youtube link', inline=True)
    embed.add_field(name=".resume", value='Makes the bot continue the music', inline=True)
    embed.add_field(name=".pause", value='Makes the bot pause the music', inline=True)
    embed.add_field(name=".stop", value='Makes the bot stop playing the music', inline=True)
    embed.add_field(name=".leave", value='Makes the bot leave the channel', inline=True)
    embed.add_field(name="LEVELING SYSTEM IS OFF", value='There is a bug with the leveling system that needs to be fixed. All data is saved.', inline=True)
    embed.add_field(name="Reminder:", value='This bot is still in development. To request commands or report a bug, please go to this link: https://goo.gl/forms/x7jBnKKGFxGq2Ui92', inline=True)
    embed.set_thumbnail(url=bot.user.avatar_url)
    await bot.say(embed=embed)

#Clear Command

@bot.command(pass_context=True)
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("{} messages deleted".format(amount))






#Token for bot

bot.run("NDk0MjgzMDQ3OTkxMjQ2ODU4.DoxgNg.GhwefeK2qboH4uhKMMv5jhLXOGw")

#https://discordapp.com/oauth2/authorize?client_id=494283047991246858&scope=bot