from discord import Attachment
from discord.ext import commands
from translate import Translator
from orc import run_ocr
class DevCommands(commands.Cog, name='Developer Commands'):
  '''These are the developer commands'''
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def t_to(self, ctx, lang, *, arg):
    await ctx.send(Translator(to_lang=f"{lang}").translate(f"{arg}"))
  
  @commands.command()
  async def t_from(self, ctx, lang, *, arg):
    await ctx.send(Translator(to_lang="en", from_lang=f"{lang}").translate(f"{arg}"))
  
  @commands.command(name="ocr")
  async def ocr_(self, ctx, image):
    await ctx.send(run_ocr(img_url=image))
      
def setup(bot):
  bot.add_cog(DevCommands(bot))
  print('Loaded!')