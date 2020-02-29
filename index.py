from math import radians

import calculate
import interval
import random

# initialLat = input("What is your latitude ") # 43.669378

# initialLon = input("What is your longitude ") # -79.338253

# initialLat = 43.669378 # 43.669378
initialLat = 43.1 # 43.669378

initialLon = -79.338253 # -79.338253

initialDistance = calculate.distanceToDuff(radians(initialLat), radians(initialLon))

print("You are " + str(initialDistance) + " km from the duff" )

def generateRandom():
  randomLat = random.uniform(42, 44)
  randomLon = random.uniform(-78, -80)
  newDistance = calculate.distanceToDuff(radians(randomLat), radians(randomLon))


  if newDistance < initialDistance:
    print("WARMER")
  elif newDistance > initialDistance:
    print("COLDER")
  else:
    print("Keep moving")

interval.set_interval(generateRandom, 2)
