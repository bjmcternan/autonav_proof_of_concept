MAX_ACCEL = 3
MAX_SPEED = 2

class Encoder():
  distancePrev = 0
  distance = 0
  speed = 0
  accel = 0
  
  def __init__(self):
    self.distancePrev = 0
    self.distance = 0
    self.speed = 0
    self.accel = 0

  def update(self):
    #save last distance
    self.distancePrev = self.distance 
    
    #set speed
    if(self.speed > MAX_SPEED):
      self.speed = MAX_SPEED
    
    #calculate distance
    self.distance += self.speed
    round(self.distance,3) #avoid floating point errors
          
  def accelerate(self, dV):
    self.accel = dV
    
  def getDistanceTraveled(self):
    return self.distance - self.distancePrev
  
  def setSpeedPower(self, power):
    if(power > 1):
      power = 1
    elif(power < -1):
      power = -1
    self.speed = MAX_SPEED * power
  
  def getSpeed(self):
    return self.speed
