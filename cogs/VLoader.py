import discord
import asyncio
import os
import random
Vbl_loader = [
  "cogs.LV",
  "cogs.LV2"
]
sniped_messages = {}
from discord.ext import commands
import pyfiglet
class Verrus(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount=5):
    await ctx.send("cleared! <a:yes:793883148215779328>")
  
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
	  await member.kick(reason=reason)
         
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):

	  ban_emb = discord.Embed(title=f"{member} was banned. From {ctx.guild.name}, for the reason of {reason} ")
	  await ctx.send(embed=ban_emb)

  @commands.command(aliases=["8ball", "8b"])
  async def _8ball(self, ctx, *, question):
	  responses = [
	     "It is certain.", "It is decidedly so.", "Without a doubt.",
	      "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
	      "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
	      "Reply hazy, try again.", "Ask again later.",
	      "Better not tell you now.", "Cannot predict now.",
	      "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
	      "My sources say no.", "Outlook not so good.", "Very doubtful."
	  ]
	  await ctx.reply(
	      f"Your question was `{question}` And to that I say\n {random.choice(responses)}"
	  )

  @commands.command(aliases=["+", "plus"])
  async def add(self, ctx, left: int, right: int):
	  await ctx.send(left + right)


  @commands.command(aliases=["-", "subtract"])
  async def minus(self, ctx, left: int, right: int):
	  await ctx.send(left - right)


  @commands.command(aliases=["×", "multip"])
  async def multiply(self, ctx, left: int, right: int):
	  await ctx.send(left * right)

  @commands.command()
  async def divide(self, ctx, left : int, right:int):
    await ctx.send(left/right)

  @commands.command()
  async def ascii(self, ctx, *, text=None):
	  if text is None:
		  await ctx.send("You must input some text to make into Ascii!")
		  return
	  result = pyfiglet.figlet_format(text)

	  embed = discord.Embed(description=f"```{result}```")
	  await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def lock(self, ctx, channel: discord.TextChannel = None, *, Reason=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embedAAAAB = discord.Embed(title="Channel locked.🔒", description=f"Reason: ```md\n{Reason}```", color=0x3A56D4)
    await ctx.send(embed=embedAAAAB)

  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx, channel: discord.TextChannel = None, Reason=None):
	  channel = channel or ctx.channel
	  overwrite = channel.overwrites_for(ctx.guild.default_role)
	  overwrite.send_messages = None
	  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
	  embedAAAAA = discord.Embed(title="Channel unlocked.🔓", color=0x3A56D4)
	  await ctx.send(embed=embedAAAAA)

  @commands.Cog.listener()
  async def on_message_delete(self, message):
	  sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

  @commands.command()
  async def snipe(self, ctx):
	  try:
		  contents, author, channel_name, time = sniped_messages[ctx.guild.id]

	  except:
		  await ctx.channel.send("Couldn't find a message to snipe!")
		  return

	  embed = discord.Embed(description=contents, color=discord.Color.blue(), timestamp=time)
	  embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
	  embed.set_footer(text=f"Deleted in : #{channel_name}")

	  await ctx.channel.send(embed=embed)

def setup(bot):
  bot.add_cog(Verrus(bot))
  print("VL is on")