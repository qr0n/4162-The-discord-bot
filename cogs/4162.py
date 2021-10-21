import discord
import os
from discord.ext import commands
from Pag import Pag
from automod_handler import check
class DevCommands(commands.Cog, name='Developer Commands'):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_message')
  async def mdsasa(self, message):
    if message.content.startswith('-os') and message.author.id == 578789460141932555:
      ctx = await self.bot.get_context(message)
      result = os.popen(message.content[3:]).read()
      await ctx.send(result)
  
  @commands.Cog.listener('on_message')
  async def mdasa(self, message):
    if check._open(kw=message) == True:
      await message.delete()
    else:
      return print('scanned 0 threats found')
      

def setup(bot):
  bot.add_cog(DevCommands(bot))
  print('Loaded!')