import os
import contextlib
import io
import logging
import textwrap
import traceback
import random
Random_gen_chars = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 1,2,3,4,5,6,7,8,9)
Random_gen_ints = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
import random
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
class assigner:
    @staticmethod
    def Create(integer=False):
        if integer == True:
            a = random.choice(Random_gen_ints)
            b = random.choice(Random_gen_ints)
            c = random.choice(Random_gen_ints)
            d = random.choice(Random_gen_ints)
            e = random.choice(Random_gen_ints)
            f = random.choice(Random_gen_ints)
            g = random.choice(Random_gen_ints)
            h = random.choice(Random_gen_ints)
            i = random.choice(Random_gen_ints)
            j = random.choice(Random_gen_ints)
            en = f"{a}{b}{c}{d}{e}{f}{g}{h}{i}"
            return en
        a = random.choice(Random_gen_chars)
        b = random.choice(Random_gen_chars)
        c = random.choice(Random_gen_chars)
        d = random.choice(Random_gen_chars)
        e = random.choice(Random_gen_chars)
        f = random.choice(Random_gen_chars)
        g = random.choice(Random_gen_chars)
        h = random.choice(Random_gen_chars)
        i = random.choice(Random_gen_chars)
        j = random.choice(Random_gen_chars)
        toeken = f"{a}{b}{c}{d}{e}{f}{g}{h}{i}"
        return toeken