MAX_ACCEL = 3
MAX_SPEED = 10

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
    self.speed += self.accel
    if(self.speed > MAX_SPEED):
      self.speed = MAX_SPEED
    
    #calculate distance
    self.distance += self.speed
    round(self.distance,3) #avoid floating point errors
          
  def accelerate(self, dV):
    self.accel = dV
    
  def getDistanceTraveled(self):
    return self.distance - self.distancePrev
  
  def getSpeed(self):
    return self.speed
