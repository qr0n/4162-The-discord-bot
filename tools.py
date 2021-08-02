import os
import contextlib
import io
import logging
import textwrap
import traceback

from traceback import format_exception
switch = {}

class switch:
  @staticmethod
  def filter():
    for entry in switch:
      if entry == 0 and entry == 1:
        switch.clear()
  
class UiConstructor:
  def start(*, config):
    if config == None:
      return "Add a configeration"
    if config == "console" or config == "terminal":
      Var_mode = 1
    if config == "window":
      return "support for window based UI's is a work in progress"
      
    def internal_constructor(mode : Var_mode=None):
      pass

class Linkify:
  @staticmethod
  def linkify(linker):
    if linker.startswith("https://"):
      return
    else:
      magic = "https://" + linker + ".com"
      return magic

class Upload(Linkify):
  def upload(*item):
    @staticmethod
    async def start_process(item):
      bam = Linkify.linkify(linker=item)
      print("attempting to upload item to website: " + bam)

class Repeat:
  def constant(amount, logic):
    def start_repeat(amount: amount):
      for i in range(amount):
        van = exec(logic)
        return van

class CEPLID:
  @staticmethod
  def exe(code):
    try:
      pager = exec(code)
    except Exception as pager:
      
      return pager
