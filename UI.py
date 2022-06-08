from __main__ import *
import os
import time
import random


# This file will be used for UI, loops and all.
# Pure organisation purposes...
# UF selection of word to print

def wordboard(currentcharacters, count, guesslist, score):
  time.sleep(0.5)

  dashboxtop = ("---")
  dashboxside1 = ("| " + currentcharacters[looperL] +" |")

  # Top layer
  looper1 = count
  while looper1 != 0:
    looper1 -= 1
    print(dashboxtop)

  # Middle layer
  looper1 = count
  while looper1 != 0:
    looper1 -= 1
    print(dashboxside1)

  # Bottom layer
  looper1 = count
  while looper1 != 0:
    looper1 -= 1
    print(dashboxtop)
    print("")
    print("Letter number " + looperL)

  
  

