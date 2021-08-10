import discord
import random
import asyncio
from asyncio import sleep as s  
from discord.ext import commands
class Verrus2(commands.Cog, name='Verrus 2.0'):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def a(self, ctx, arg=None):
    await ctx.send("a_thing")
    
  @commands.Cog.listener()
  async def on_command_error(self,ctx, error):
    print(error)

  @commands.command()
  async def ranmem(self, ctx, member: discord.Member = None):
    await ctx.send(f"@{random.choice(ctx.guild.members)}")
  
  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def pin(self, ctx, ID):
    message = await ctx.channel.fetch_message(ID)
    await message.pin()

  @commands.command()
  async def reminder(self, ctx, tme:int , *, msg):
    async with ctx.typing():

      author = ctx.author
    while True:
      await s(60*tme)
      embed = discord.Embed(title="Reminder", description=f"**{msg}** time of next reminder {tme} Minutes", colour=ctx.author.color, timestamp=ctx.message.created_at)
      await ctx.send(ctx.author.mention)
      await ctx.send(embed=embed)
      await author.send(embed=embed)

  @commands.command()
  async def tier(self, ctx, tm=10):
    while True:
      await s(1*tm)
      embed = discord.Embed(title="Timer", description=f"timer set for 10 min\n time remaining {tm}", color=ctx.author.color, timestamp=ctx.message.created_at)
      await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(Verrus2(bot))
  print('Loaded!')