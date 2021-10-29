import ocrspace
import aiohttp
import os

api = ocrspace.API(api_key=os.environ['ocr_key'])

def run_ocr(img_url):
  print('running ocr')
  return api.ocr_url(url=img_url)