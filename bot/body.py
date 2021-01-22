import math
import pygame as pg
from bot.brains import Bot_Brains
from bot.encoder import Encoder
from pygame.math import Vector2

BOT_NOSE_LEN = 10
BOT_HEIGHT = 40
BOT_HEIGHT_HALF = BOT_HEIGHT/2
BOT_BASE = 80
BOT_BASE_HALF = BOT_BASE/2

class Player(pg.sprite.Sprite):
  x = 0
  y = 0
  psi = 0
  polyPoints = [
      (0,0),
      (BOT_BASE,0),
      (0,BOT_HEIGHT),
      (BOT_BASE, BOT_HEIGHT)
    ]
  
  def __init__(self, pos=(420, 420), psi=(0)):
    #init super
    super(Player, self).__init__()
    
    #init encoders
    self.encL = Encoder()
    self.encR = Encoder()
    
    #init brain
    self.brain = Bot_Brains(self.x, self.y, self.psi)
    
    #init self variables
    self.x, self.y = pos
    self.psi = psi * (math.pi / 180)
    
    #init image
    self.image = pg.Surface((BOT_BASE, BOT_HEIGHT), pg.SRCALPHA)
    pg.draw.polygon(self.image, (50, 120, 180), self.polyPoints)
    self.original_image = self.image
    self.rect = self.image.get_rect(center=pos)
    self.image = pg.transform.rotozoom(self.original_image, -(self.psi*(180/math.pi)), 1)

  def move(self):
    #save old values
    x_old = self.x
    y_old = self.y
    psi_old = self.psi
    
    #get distance traveled
    dLeft = self.encL.getDistanceTraveled()
    dRight = self.encR.getDistanceTraveled()
    
    #Calculate new attitude angle
    delPsi = (dLeft - dRight) / BOT_BASE
    
    #Compute average distance traveled
    dAve = (dLeft + dRight) / 2
    
    #Compute incremental field position with correction
    c1 = (1 - (delPsi * delPsi) / 6)
    c2 = delPsi / 2;
    cPsi = math.cos(psi_old)
    sPsi = math.sin(psi_old)
    delX = dAve * (c1*cPsi - c2*sPsi)
    delY = dAve * (c1*sPsi - c2*cPsi)
    
    #update position
    self.x = x_old + delX
    self.y = y_old + delY
    self.psi = psi_old + delPsi
    
    #update image
    self.image = pg.transform.rotozoom(self.original_image, -(self.psi*(180/math.pi)), 1)
    self.rect.center = (self.x, self.y)
    # Create a new rect with the center of the old rect.
    self.rect = self.image.get_rect(center=self.rect.center)
    
  def update(self, lInc, rInc):
    self.encL.setSpeedPower(lInc)
    self.encR.setSpeedPower(rInc)
    self.encL.update()
    self.encR.update()
    self.move()
    # Update the position vector and the rect.
    #self.position += self.direction * self.speed
    #self.rect.center = self.position