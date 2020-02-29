from math import radians
from time import sleep

import calculate
import interval
import random

import pygame
from pygame import mixer

# initialLat = input("What is your latitude ") # 43.669378

# initialLon = input("What is your longitude ") # -79.338253

# initialLat = 43.669378 # 43.669378
initialLat = 43.1 # 43.669378

initialLon = -79.338253 # -79.338253

initialDistance = calculate.distanceToDuff(radians(initialLat), radians(initialLon))

print("You are " + str(initialDistance) + " km from the duff" )

pygame.init()
mixer.init()

def generateRandom():
  randomLat = random.uniform(42, 44)
  randomLon = random.uniform(-78, -80)
  newDistance = calculate.distanceToDuff(radians(randomLat), radians(randomLon))


  if newDistance < initialDistance:
    print("WARMER")
  elif newDistance > initialDistance:
    sound = mixer.Sound("really.wav")
    sound.play()
    sleep(5)
  else:
    sound = mixer.sound("really.wav")
    sound.play()

interval.set_interval(generateRandom, 5)
