import os 
os.system("pip install discord-py-slash-command")
import discord_slash
from discord_slash import SlashCommand
import discord
from selenium.webdriver.chrome.options import Options
import contextlib
import io
import logging
import textwrap
import discord.ext
muted_mods = [462633211697168384]
whitelisted = []
reduced_mods = []
import time
intents = discord.Intents.default()
intents.members = True
intents.presences = True
from discord.ext import commands
import asyncio
import random
from asyncio import sleep as s
import json
import contextlib
import io
import urllib.parse, urllib.request
import regex as re
os.system("pip install droblox")
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

web = os.environ['web']


def get_prefix(client,message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

eng_to_morse = {
    'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--', ' ' : '/'
}

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

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
    
@bot.event
async def on_ready():
    for guild in bot.guilds:
        bot.warnings[guild.id] = {}
        
        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    bot.warnings[guild.id][member_id][0] += 1
                    bot.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    bot.warnings[guild.id][member_id] = [1, [(admin_id, reason)]] 
    
    print(bot.user.name + " is ready.")



@bot.event
async def on_guild_join(guild):
    bot.warnings[guild.id] = {}

@bot.listen("on_guild_join")
async def am(guild):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

    prefixes[str(guild.id)] = "!"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
        
    if reason is None:
        return await ctx.send("Please provide a reason for warning this user.")

    try:
        first_warning = False
        bot.warnings[ctx.guild.id][member.id][0] += 1
        bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = bot.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")

@bot.command()
@commands.has_permissions(administrator=True)
async def warnings(ctx, member: discord.Member=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
    
    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in bot.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: '{reason}'.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError: # no warnings
        await ctx.send("This user has no warnings.")



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

            await msg.channel.send(f"My prefix for this server is {pre}")

    except:
        pass
    await bot.process_commands(msg)

tags_dict = {"CEPLID" : "Python Code Execution Engine in discord"}
print("Loaded tags: {}".format(tags_dict))

token = os.environ.get("runawayT")


bot.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}
    


@bot.command()
async def test(ctx, taggo):
  for tag in taggo:
    if tag in tags_dict:
      print(tag)
    else:
      print("tag was not found")
@bot.command()
async def ping(ctx, web, *, data):
  import aiohttp
  async with aiohttp.post("https://gdm.bothost.repl.co", data=None):
    await ctx.send("pinging webserver with data")


@bot.command()
async def tag(ctx, tag):
  for tag in tags_dict:
    if tag in tags_dict:
      print(tags_dict)
    else:
      print("didnt work")

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
  if message.channel.id == 854037584665903156:
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
        f"{ctx.author.id}" : f"current code : {message.content}"
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
async def hello(ctx):
  await ctx.send("hi!")

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

@slash.slash(guild_ids=guild_ids)
@commands.has_role("Vice Admiral")
async def sudo(ctx, member : discord.Member, *, arg):
	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(f'{web}',
		                           adapter=AsyncWebhookAdapter(session))
		await webhook.send(f"{arg}",
		                   username=f"{member.display_name}",
		                   avatar_url=f"{member.avatar_url}")

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

@slash.slash(guild_ids=guild_ids)
async def exe(ctx, *, arg):


    code = arg
    recode = clean_code(code)


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
        "os" : os
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




k()
bot.run(a)