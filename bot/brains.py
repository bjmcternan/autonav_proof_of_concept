class Bot_Brains():
  velL = 0
  velR = 0
  def __init__(self, x, y, psi):
      super(Bot_Brains, self).__init__()
      self.x = x
      self.y = y
      self.psi = psi
      
  def getVelocityPower(self):
    return (self.velL, self.velR)