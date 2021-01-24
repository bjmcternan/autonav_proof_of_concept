import math
import pygame as pg
from bot.body import Body

# Player(pg.sprite.Sprite)
# responsible for keeping track of sprite
class Player(pg.sprite.Sprite):
  body = None
  polyPoints = None
  
  # __init__(self, pos, psi)
  # Init Player class
  def __init__(self, pos, psi):
    #init super
    super(Player, self).__init__()

    #init body
    self.body = Body(pos, psi)
    self.polyPoints = self.body.get_body_specs()

    bot_width, bot_height = max(self.polyPoints)

    #init image
    self.image = pg.Surface((bot_width, bot_height), pg.SRCALPHA)
    pg.draw.polygon(self.image, (50, 120, 180), self.polyPoints)
    self.original_image = self.image
    self.rect = self.image.get_rect(center=self.body.get_pos())
    self.image = pg.transform.rotozoom(self.original_image, -(self.body.get_psi()*(180/math.pi)), 1)

  def update(self):
    self.body.update()
    #update image rotation
    self.image = pg.transform.rotozoom(self.original_image, -(self.body.get_psi()*(180/math.pi)), 1)
    #update image position
    self.rect.center = (self.body.get_pos())
    # Create a new rect with the center of the old rect.
    self.rect = self.image.get_rect(center=self.rect.center)

  # add_coordinate(self, pos)
  # Pass new coordinate to body
  def add_coordinate(self, pos):
    self.body.add_coordinate(pos)