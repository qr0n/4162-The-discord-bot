from discord_webhook import DiscordWebhook
import os
web_url = os.environ['durl']

class logging:
  def send(content):
    DiscordWebhook(url=web_url, content=content).execute()