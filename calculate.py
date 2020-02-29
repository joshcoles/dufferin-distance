from math import sin, cos, sqrt, atan2, radians

def distanceToDuff(lat1, lon1):
    
# approximate radius of earth in km
  R = 6373.0
  
  duffLat = radians(43.655830)
  duffLon = radians(-79.435360)

  lat2 = duffLat
  lon2 = duffLon

  dlon = lon2 - lon1
  dlat = lat2 - lat1

  a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  c = 2 * atan2(sqrt(a), sqrt(1 - a))

  distance = R * c

  x = distance

  return x
  