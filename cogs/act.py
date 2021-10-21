import discord
from replit import db
from discord.ext import commands
class DevCommands(commands.Cog, name='Developer Commands'):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def clear_vc_logs(self, ctx):
    for i in db.keys():
      del db[i]
      await ctx.send(f"deleting key {i}")
      
def setup(bot):
  bot.add_cog(DevCommands(bot))
  print('Loaded!')