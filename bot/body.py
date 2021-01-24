import math
import pygame as pg
from bot.brains import Brains
from bot.encoder import Encoder
from pygame.math import Vector2

BOT_NOSE_LEN = 10
BOT_HEIGHT = 40
BOT_HEIGHT_HALF = BOT_HEIGHT/2
BOT_BASE = 80
BOT_BASE_HALF = BOT_BASE/2

# Body
# Controls the body of the robot
class Body():
  x = None
  y = None
  psi = None
  brain = None
  enc_l = None
  enc_r = None

  # __init__(self, pos, psi)
  # takes initial position and psi (heading)
  def __init__(self, pos, psi):
    #init encoders
    self.enc_l = Encoder()
    self.enc_r = Encoder()
    self.x, self.y = pos
    self.psi = psi
    
    #init brain
    self.brain = Brains(self.x, self.y, self.psi, self)

  # get_pos(self)
  # gets current position
  def get_pos(self):
    return (self.x, self.y)
  
  # get_psi(self)
  # gets current psi
  def get_psi(self):
    return self.psi

  # get_body_specs(self)
  # returns a list of body polygon points
  def get_body_specs(self):
    return_points = [
      (0,0),
      (BOT_BASE,0),
      (0,BOT_HEIGHT),
      (BOT_BASE, BOT_HEIGHT)
    ]
    return (return_points)

  # update(self)
  # update function to update controls
  def update(self):
    self.brain.update()
    self.enc_l.update()
    self.enc_r.update()
    self.update_current_position()
  
  # add_coordinate(self, pos)
  # Pass new coordinate to brain
  def add_coordinate(self, pos):
    self.brain.add_coordinate(pos)

  # update_current_position(self)
  # Use kinematics to keep update current position
  def update_current_position(self):
    #save old values
    x_old = self.x
    y_old = self.y
    psi_old = self.psi
    
    #get distance traveled
    del_left = self.enc_l.getDistanceTraveled()
    del_right = self.enc_r.getDistanceTraveled()
    
    #Calculate new attitude angle
    del_psi = (del_left - del_right) / BOT_BASE
    
    #Compute average distance traveled
    del_ave = (del_left + del_right) / 2
    
    #Compute incremental field position with correction
    c1 = (1 - (del_psi * del_psi) / 6)
    c2 = del_psi / 2;
    cos_psi = math.cos(psi_old)
    sin_psi = math.sin(psi_old)
    del_x = del_ave * (c1*cos_psi - c2*sin_psi)
    del_y = del_ave * (c1*sin_psi - c2*cos_psi)
    
    #update position
    self.x = x_old + del_x
    self.y = y_old + del_y
    self.psi = psi_old + del_psi
