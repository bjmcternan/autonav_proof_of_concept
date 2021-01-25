MAX_ACCEL = 3
MAX_SPEED = 2

class Encoder():
  distance_prev = 0
  distance = 0
  speed = 0
  accel = 0
  
  # __init__(self)
  # Initializes the encoder
  def __init__(self):
    self.distance_prev = 0
    self.distance = 0
    self.speed = 0
    self.accel = 0

  # update(self)
  # updates the current state
  def update(self):
    #save last distance
    self.distance_prev = self.distance 
    
    #set speed
    if(self.speed > MAX_SPEED):
      self.speed = MAX_SPEED
    
    #calculate distance
    self.distance += self.speed
    self.distance = round(self.distance,3) #avoid floating point errors

  # get_distance_traveled(self)
  # returns the distance traveled since last update    
  def get_distance_traveled(self):
    return self.distance - self.distance_prev
  
  # set_power(self, power)
  # sets the current speed to power * MAX_SPEED
  def set_power(self, power):
    if(power > 1):
      power = 1
    elif(power < -1):
      power = -1
    self.speed = MAX_SPEED * power
  
  # get_speed(self)
  # returns the current speed
  def get_speed(self):
    return self.speed
