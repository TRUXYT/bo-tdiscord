import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='-', description="hola")

@bot.command()
async def emoji(ctx, emoji:discord.Emoji):
  await ctx.send(emoji)
  print(emoji)
    
@bot.command()
async def ping(ctx):
	await ctx.send('¡Pong!<a:pong:689171698410586145>')
	
@bot.event
async def on_ready():
	print('EL BOT ESTA ON')
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Informacion del servidor", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="El servidor se creo el", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Dueño del servidor", value=f"{ctx.guild.owner}")
    embed.add_field(name="Region del servidor", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del servidor", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)
	
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    
    embed = discord.Embed(title="Title", timestamp=ctx.message.created_at)
    
    embed.set_author(name=f"Inforacion del usuario = {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Comando ejecutado por: {ctx.author}", icon_url=ctx.author.avatar_url)
    
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Nombre:", value=member.display_name)
    
    embed.add_field(name="Cuenta creada el:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Se unio el:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    
    embed.add_field(name="¿Es un bot?", value=member.bot)
    
    await ctx.send(embed=embed)

bot.remove_command("help")
bot.run('Njg3NjMwNTUzOTMxMTg2Mjc2.XnEEiQ.ik7UYsfl9dIIPe1-9nbPBGu8VFQ')
