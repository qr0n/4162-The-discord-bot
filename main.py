import os 
os.system("pip install discord-py-slash-command")
import discord_slash
from discord_slash import SlashCommand
import discord
import discord 
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
controled_vc = []
whitelisted_user = []
vc_state = []
memer = []
from selenium.webdriver.chrome.options import Options
import contextlib
import io
import logging
import textwrap
banned_nick = []
status = []
import discord.ext
muted_mods = []
whitelisted = []
reduced_mods = []
import time
vcs = []
intents = discord.Intents.default()
intents.members = True
intents.presences = True
from discord.ext import commands, tasks
import asyncio
import random
from asyncio import sleep as s
import json
import contextlib
import io
import urllib.parse, urllib.request
import regex as re
from pathlib import Path
import aiofiles
import wikipedia, os
import logging
#from discord.ext import menus
import jishaku
from discord import Webhook, AsyncWebhookAdapter
from Pag import Pag
from rsap import RSAP
from tools import *
import aiohttp
db = []
switch = {}
web_logs = []
ceplid_verified = [874882719715295245, 854037584665903156]
web = os.environ['web']

def get_tag(tag_name):
  with open("jsons/tag.json", "r") as D:
    tag_loader = json.load(D)
  try:  
    loaded = tag_loader[tag_name]

    return loaded
  except KeyError:
    return "Tag does not exist."

def get_prefix(client,message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.author_id = 578789460141932555
extensions = [
  "cogs.music",
  "cogs.Main_cog",
  "cogs.Tools",
  "cogs.VLoader",
  "cogs.VLoader2",
  "cogs.gitsearch",
  
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)


cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

def read_json(filename):
    with open(f"{cwd}/bot_config/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{cwd}/bot_config/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

eng_to_morse = {
    'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--', ' ' : '/'
}



bo = RSAP(f"{os.environ.get('api')}", bot_name="Verrus", dev_name="Infinity Iron", type="unstable")
sel_O = RSAP(f"{os.environ.get('api')}", bot_name="Verrus", dev_name="Infinity Iron", type="stable")
obot2 =RSAP(f"{os.environ.get('api2')}", bot_name="Verrus", dev_name="Infinity Iron", type="stable")

obot3 = RSAP(f"{os.environ.get('api3')}", bot_name="Verrus", dev_name="Infinity Iron", type="stable")
slash = SlashCommand(bot, sync_commands=True)
guild_ids = [759474157330366506, 781968220482699314]
evaluators = [708124746872651807, 578789460141932555]
from keep_alive import keep_alive as k
# Third party libraries
import textwrap
from traceback import format_exception
a = os.environ.get("token")


@bot.listen("on_message")
async def fewifew(message):
  ctx = await bot.get_context(message)
  relay = message.content
  name = ctx.author.name
  server = ctx.guild.name
  


bot.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}






@bot.listen("on_guild_join")
async def am(guild):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

    prefixes[str(guild.id)] = "!"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)




@bot.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)    

    await ctx.send(f"The prefix was changed to {prefix}")



@bot.event
async def on_message(msg):

    try:
        if msg.mentions[0] == bot.user:

            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            pre = prefixes[str(msg.guild.id)] 

            await msg.channel.send(f"My prefix for this server is `{pre}`")

    except:
        pass
    await bot.process_commands(msg)



token = os.environ.get("runawayT")


bot.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}
    


@bot.command()
async def ping(ctx, web, *, data):
  import aiohttp
  async with aiohttp.post("https://gdm.bothost.repl.co", data=None):
    await ctx.send("pinging webserver with data")



@bot.command()
async def jsn(ctx, arg1, arg2):
  with open('b.json', 'w') as h:
    m = json.load(h)
    await ctx.send(a)

@bot.command()
async def everything(ctx):
  for guild in bot.guilds:
    names = guild.name
    id = guild.id
    le = len(bot.guilds)
  embed = discord.Embed(title=f"Hi my name is {bot.user.name} my id is {bot.user.id}, and my nick name in this server is {bot.user.display_name}", description=f"i am currently connected to[{le}] {names} with a ping of {round(bot.latency * 1000)}")
  await ctx.send(embed=embed)

@bot.command()
async def ytsearch(ctx, *, search):
  qry_string = urllib.parse.urlencode({
    "search_query" : search
  })
  htm_content = urllib.request.urlopen(
    'https://www.youtube.com/results?' + qry_string
  )
  search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
  await ctx.send("https://www.youtube.com/watch?v" + str(list(str(search_results))))

@bot.command()
async def channelinfo(ctx, channel : discord.TextChannel):
  embed = discord.Embed(title=f"Showing infomation for {channel.name}", description=f"ID : {channel.id}\nPos : {channel.position}\nName : {channel.name}\nTopic : {channel.topic}")
  await ctx.send(embed=embed)




@bot.listen("on_message")
async def collect(message):
  if message.author.id == 786982798883422238:
    return
  imp_args = (f"Generate some text! ill give you some information thier name is {message.author.name}, but you can call them {message.author.nick} and what you need to generate from is {message.content} and this was send on {message.created_at} you will be provided addional infomation such as channel name topic and others")
  addional_args = (message.channel.topic, message.channel.name)
  if message.content.startswith("$gen"):
    ctx = await bot.get_context(message)
    mychannel = bot.get_channel(ctx.channel.id)
    ab = await message.channel.send("Generating Text...")
    collection = bo.ai_response(f"{imp_args}{message.content}"[-1:], "Gen_ID")
    print(collection)
    collection2 = obot2.ai_response(f"{imp_args}{collection}", "Gen_ID")
    print(collection2)
    collection3 = bo.ai_response(f"{imp_args}{collection2}", "Gen_ID")
    print(collection3)
    collection4 = obot2.ai_response(f"{collection3}", "Gen_ID")
    print(collection4)
    collection5 = obot3.ai_response(f"{collection4}", "Gen_ID")
    print(collection5)
    collection6 = bo.ai_response(f"{imp_args}{collection5}", "Gen_ID")
    print(collection6)
    collection7 = obot2.ai_response(f"{collection6}", "Gen_ID")
    print(collection7)
    collection8 = obot3.ai_response(f"{collection7}", "Gen_ID")
    print(collection8)
    collection9 = bo.ai_response(f"{imp_args}{collection8}", "Gen_ID")
    print(collection9)
    collection10 = obot2.ai_response(f"{collection9}", "Gen_ID")
    print(collection10)
    all = f"{collection} {collection2} {collection3} {collection4} {collection5} {collection6} {collection7} {collection8} {collection8} {collection9} {collection10}"
  
    if message.content.endswith("!bothR"):
      eve = bo.ai_response(f"{all}", "Gen_ID")
      await ctx.reply(f"```\nResponse from all collections: \n{all}\n\nResponse from all collections(Unified): \n{eve}```")
      return
    if message.content.endswith("!astable"):
      c1 = obot2.ai_reponse(f"{message.content}", )
    print(all)
    
    await ctx.reply(f"```\n{all}\n```", mention_author=True)


@bot.command()
async def logout(ctx):
  await bot.close()

@bot.command()
async def tts(ctx):
  await ctx.send(content="moyai", tts=True)

@bot.command()
async def slot(ctx, member : discord.Member=None):
  maybe = await bot.fetch_user_profile(member.id)
  await ctx.send(maybe)


@bot.listen('on_message')
@commands.has_role("Evaluators")
async def _eval(message):
  if message.content.startswith("ceplid"):
    await message.channel.send("Ceplid is a python code execution engine where you can run code prefixless and free of cost with lighting fast speeds powered with love and care - Infinity Iron#4170")
  
  if message.content.startswith("%"):
    return
  if message.author.id == 780835623006240809:
    return
  if message.channel.id in ceplid_verified:
    code = message.content
    recode = clean_code(code)

    ctx = await bot.get_context(message)
    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": bot,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message,
        "token" : token,
        "os" : os,
        f"{ctx.author.id}" : f"current code : {message.content}",
        "thebad" : f"{os.environ.get('the_bad')}",
        
    }

    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
        result = "".join(format_exception(e, e, e.__traceback__))

    pager = Pag(
        timeout=100,
        entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```"
    )

    a = await pager.start(ctx)
    await ctx.send(a)
  else:
    return



def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content


@bot.listen("on_message")
async def verruschaneler(message):
  if message.author.id == 780835623006240809:
    return
  if message.content.startswith("#"):
    print("ignoring message \"{}\"".format(message.content))
    resp =  bo.ai_response(f"{message.content}!", "One_ID")
    print(resp)
    return
  else:
    channeler = bot.get_channel(848338279383957534)
    if(message.channel.id == 848338279383957534):
      channeler = bot.get_channel(848338279383957534)
    else:
      return
    ctx = await bot.get_context(message)
    await ctx.trigger_typing()
    response = bo.ai_response(f"{message.content}", f"{message.author.id}")
    ctx = await bot.get_context(message)
    if response == "<html>":
      await ctx.reply("Shard Disconnecting.")
    if response == "":
      resp =  bo.ai_response(f"{message.content}!", "One_ID")
      await ctx.reply(resp, mention_author=False)
    await ctx.reply(response, mention_author=False)

@bot.command()
async def trustat(ctx, member : discord.Member):
  getting = await bot.fetch_user(member.id)
  tru = discord.Embed(title=f"Showing true status for {member}", description=f"{member.status}")
  await ctx.send(embed=tru)



@bot.command()
@commands.is_owner()
async def restartBot(ctx):

    await ctx.bot.login(f"{os.environ.get('token')}", bot=True)



@bot.command()
async def lo(ctx):
  await ctx.send("hi!")

@bot.command()
async def mcode(ctx, word):
  outstr = ''
  space = ' '
  senc = 0
  wordprocces = 0

  lenword = len(word)

  for i in word:
    if i not in eng_to_morse:
        await ctx.send('Data not formatted properly', delete_after=5)
        time.sleep(5)
        break
    else:
      mcodetranslation = (eng_to_morse[i])
      print(eng_to_morse[i], end=' ')
      await ctx.send(mcodetranslation)

@bot.command()
async def set_logging(ctx, channel : discord.TextChannel=None):
  if channel == None:
    channel = ctx.channel.id
    db.append(int(channel))
    got = bot.get_channel(channel)
  else:
    channel = channel
    get = await bot.get_channel(channel)
    await ctx.send("ser ")

@bot.command()
async def toggle(ctx, arg:int):
  switch.filter()


@bot.command()
async def mute(ctx, user : discord.Member):
  muted_mods.append(user.id)
  await ctx.send(f"<@{user.id}> is muted")

@bot.command()
async def unmute(ctx, user : discord.Member):
  if ctx.author.id in muted_mods:
    await ctx.send(f"{ctx.author.mention} Sorry but you are being restricted from doing this action.")
    return
  muted_mods.remove(user.id)
  await ctx.send(f"<@{user.id}> is unmuted")

@bot.listen("on_message")
async def listen(message):
  if message.author.id in muted_mods:
    await message.delete()
  else:
    return

@bot.command()
async def upload(ctx, thing):
  Upload.upload(thing)
  await ctx.send("ok")

@bot.command()
async def linkify(ctx, ya):
  await ctx.send(Link.linkify(linker=ya))
        
@bot.listen("on_message")
async def testing(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await bot.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))



@bot.command()
async def CEPLIDify(ctx, code):
  await ctx.send(CEPLID.exe(code=code))

mass_dict = {}


my_secret = os.environ['token']


json_data = None

@bot.command()
async def get_json(ctx):
  await ctx.send("working on it.")
  with open("jsons/data.json", "r") as f:
    raw = f.read()
    json_data = json.loads(raw)
  
  await ctx.send(str(json_data))

@bot.command()
async def settopic(ctx, *, arg):
  await ctx.send("working on it.")

  with open("jsons/data.json", "w") as j:
    json.dump(arg, j)


@bot.listen("on_message")
async def whatsthetopic(message):
  if message.content == "whats the topic" or message.content ==  "what are we talking about?":
    await message.channel.send("Hey here's what we're talking about! https://gdm.bothost.repl.co/HTopic")
  elif message.content == ":deadchat:" or message.content == "<:deadchat:628795754672029696>":
    await message.channel.send("We know!")


@bot.command()
async def update(ctx):
  with open("jsons/news.json", "w") as ne:
    chan = bot.get_channel(838255151823061002)
    msgs = await chan.history(limit=10).flatten()
    s1 = msgs[0].content
    s2 = msgs[1].content
    s3 = msgs[2].content
    s4 = msgs[3].content
    s5 = msgs[4].content 
    s6 = msgs[5].content
    strin = f"{s1}\n{s2}\n{s3}\n{s4}\n{s5}\n{s}"

    usable_content = str(strin)
    jData = json.dump(usable_content, ne)
    await ctx.send("Updated")

@bot.command()
async def add_banned_nick(ctx, *,arg):
  banned_nick.append(arg)
  await ctx.send("added")

@bot.listen("on_member_update") # This event runs whenever a user updates: status, game playing, avatar, nickname or role
async def on_member_(before, after): 
    n = after.nick 
    if n: # Check if they updated their username
        if n.lower() in banned_nick: # If username contains an item in banned_nick
            last = before.nick
            if last: # If they had a usernae before change it back to that
                await after.edit(nick=f"[Moderated Nickname] {assigner.Create(integer=False)}")
            else: 
                await after.edit(nick=f"[Moderated Nickname] {assigner.Create(integer=False)}")

@bot.command()
async def switch(ctx, statnus):
    if statnus == "on":
        statnus = "on"
        star = 1
        status[star] = statnus
        await ctx.send(str(status))
    elif statnus == "off":
        statnus = "off"
        star = 0
        status[star] = statnus
        await ctx.send(str(status))
    elif statnus == "reset":
        status.clear()
        await ctx.send("reset")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:

        if after.channel.id == 866069991290568744:
            if member.id == 5787894141932555:
                return
            chan = bot.get_channel(838155702350381137)

            await chan.send(f"{member.mention} This vc is locked.", delete_after=5)
            await member.edit(voice_channel=None)



@bot.command()
async def vc_config(ctx, vc_id : discord.VoiceChannel, state, *, whitelisted : discord.Member):
  if state == "locked" or state == "unlocked":
    if state == "unlocked":
      vc_state.remove("locked")
    print("check passed")
  controled_vc.append(vc_id.id)
  vc_state.append(state)
  whitelisted_user.append(whitelisted.id)
  await ctx.send(f"<#{vc_id.id}> is {state} and only {whitelisted_user} can join")

@bot.listen("on_voice_state_update")
async def assin(member, before, after):
    if before.channel is None and after.channel is not None:

        if after.channel.id in controled_vc:
            if member.id in whitelisted_user:
                return
            chan = bot.get_channel(838155702350381137)

            await chan.send(f"{member.mention} This vc is locked.", delete_after=5)
            await member.edit(voice_channel=None)

@bot.command()
async def unlock_all(he):
  await he.send("clearing cache")

@bot.listen('on_ready')
async def dewfuew():
  for guild in bot.guilds:
      if guild.id == 876139985231806465:
        for channel in guild.text_channels:
          print(channel)
          

@bot.command()
async def cbc(ctx, cmd):
  channel = bot.get_channel(876139985231806468)
  await channel.send(f"name= {cmd}")
  await channel.send(f"guild_id= {ctx.guild.id}")
  await channel.send(f"channnel_id= {ctx.channel.id}")

@bot.listen('on_message')
async def uqwd(msg):
  m = msg.content
  if msg.author.id == 578789460141932555 and m.startswith("```") and m.endswith("```"):
    await msg.channel.send("BAD IRON")
    await msg.delete()

@bot.command()
async def p(ctx):
  """Get the bot's current websocket and API latency."""
  start_time = time.time()
  message = await ctx.send("Testing Ping...")
  end_time = time.time()


  await message.edit(content=f"Pong! {round(bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")

@bot.command()
async def wta(ctx):
  await ctx.send(file=discord.File("Screenshot 2021-08-15 000324.png"))

@bot.command()
async def add_tag(ctx, tag_name, *, tag_response):
  with open("jsons/tag.json", "r") as E:
    a = json.load(E)
    a[str(tag_name)] = tag_response
  with open("jsons/tag.json", "w") as E:
    json.dump(a, E)
  await ctx.send("Tag saved!")

@bot.command()
async def tag(ctx, tag):
  await ctx.send(get_tag(tag_name=tag))

@bot.listen("on_message")
async def asd(message):
    #ignore ourselves
    if message.author.id == bot.user.id:
        return

    #blacklist system
    if message.author.id in bot.blacklisted_users:
        return


    await bot.process_commands(message)

@bot.command()
@commands.is_owner()
async def blacklist(ctx, userA: discord.Member):
    if ctx.message.author.id == user.id:
        await ctx.send("Hey, you cannot blacklist yourself!")
        return

    bot.blacklisted_users.append(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].append(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Hey, I have blacklisted {user.name} for you.")

@bot.command()
@commands.is_owner()
async def unblacklist(ctx, user: discord.Member):
    bot.blacklisted_users.remove(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].remove(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Hey, I have unblacklisted {user.name} for you.")

k()
bot.run(a)