from discord import Attachment
from discord.ext import commands
class DevCommands(commands.Cog, name='Developer Commands'):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def translate(self, ctx, image: Attachment):
    await ctx.send(image)
      
def setup(bot):
  bot.add_cog(DevCommands(bot))
  print('Loaded!')