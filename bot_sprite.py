import math
import pygame as pg
from bot.body import BOT_LENGTH, BOT_NOSE_LEN, BOT_WIDTH, Body

# Player(pg.sprite.Sprite)
# responsible for keeping track of sprite
class Player(pg.sprite.Sprite):
  body = None
  polyPoints = None
  
  # __init__(self, pos, psi)
  # Init Player class
  def __init__(self, pos, psi, tick_ms):
    #init super
    super(Player, self).__init__()

    #init body
    self.body = Body(pos, psi, tick_ms)
    self.polyPoints = self.body.get_body_specs()

    #init image
    self.image = pg.Surface((BOT_LENGTH+BOT_NOSE_LEN, BOT_WIDTH), pg.SRCALPHA)
    pg.draw.polygon(self.image, (50, 120, 180), self.polyPoints)
    self.original_image = self.image
    self.rect = self.image.get_rect(center=self.body.get_pos())
    self.image = pg.transform.rotozoom(self.original_image, (self.body.get_psi()*(180/math.pi)), 1)

  def update(self):
    self.body.update()
    #update image rotation
    self.image = pg.transform.rotozoom(self.original_image, (self.body.get_psi()*(180/math.pi)), 1)
    #update image position
    x,y = self.body.get_pos()
    y = 720 - y 
    self.rect.center = ((x,y))
    # Create a new rect with the center of the old rect.
    self.rect = self.image.get_rect(center=self.rect.center)

  # add_coordinate(self, pos)
  # Pass new coordinate to body
  def add_coordinate(self, x, y, psi):
    self.body.add_coordinate(x, 720-y, psi)
  
  def get_text(self):
    if(self.body.brain.current_target_pos == None):
      tx = 0
      ty = 0
      tp = 0
    else:
      tx = self.body.brain.current_target_pos[0]
      ty = self.body.brain.current_target_pos[1]
      tp = self.body.brain.current_target_pos[2]
      
    return "target x: " + str(tx) + "\n"     +\
           "target y: " + str(ty) + "\n"     +\
           "target p: " + str(tp) + "\n"     +\
           "x: " + str(self.body.x) + "\n"     +\
           "y: " + str(self.body.y) + "\n"     +\
           "p: " + str(self.body.psi) + "\n"   +\
           "r: " + str(self.body.r) + "\n"     +\
           "w: " + str(self.body.omega) + "\n" +\
           "vl: " + str(self.body.brain.vl) + "\n" +\
           "vr: " + str(self.body.brain.vr) + "\n"