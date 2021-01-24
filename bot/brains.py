import math

class Brains(): 
  body = None
  x = 0
  y = 0
  psi = 0
  current_target_pos = None
  target_coordinates = []

  def __init__(self, x, y, psi, body):
      self.body = body
      self.x = x
      self.y = y
      self.psi = psi
      
  def add_coordinate(self, pos):
    self.target_coordinates.append(pos)

  def update(self):
    #No current target but there is another in the list
    if((self.current_target_pos == None) and (len(self.target_coordinates) != 0)):
      #Pop next coordinate from list and set as current target
      self.current_target_pos = self.target_coordinates.pop(0)
    