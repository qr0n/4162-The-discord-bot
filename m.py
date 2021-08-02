import discord
from discord.ext import commands
import os
from selenium.webdriver.chrome.options import Options
Token = os.environ.get("TOKEN")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

bot = commands.Bot(command_prefix="?")
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
driver = webdriver.Chrome(options=None)
driver.get('https://www.cleverbot.com')
driver.find_element_by_id('noteb').click()

def get_response(message):
    driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(message + Keys.RETURN)
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="snipTextIcon"]')
            break
        except:
            continue
    response = driver.find_element_by_xpath('//*[@id="line1"]/span[1]').text
    return response

@bot.event
async def on_ready(self):
  print('Logged on as', self.user)
@bot.event
async def on_message(message):
    if message.author != bot.user:
      reponse = get_response(message.content)
      await message.channel.send(f"{message.author.mention} {reponse}")

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

self.driver = webdriver.Chrome(
            executable_path=DRIVER_PATH, chrome_options=chrome_options)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

bot.run(f'{Token}')