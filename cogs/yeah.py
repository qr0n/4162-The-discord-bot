import discord
from discord.ext import commands
class DevCommands(commands.Cog, name='Developer Commands'):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot


    @commands.command()
    async def a_command(self, ctx, arg=None):
      await ctx.send("a_thing")
      
def setup(bot):
  bot.add_cog(DevCommands(bot))
  print('Loaded!')