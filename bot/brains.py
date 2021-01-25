import math

DEFAULT_V = .5
ACCEPTABLE_DISTANCE_DELTA = 10
K1 = 1
K2 = 3
THETA_TARGET_CONSTANT = 57.3
THETA_TARGET_MAX = math.pi
THETA_TARGET_MIN = -math.pi

class Brains(): 
  body = None
  wheelbase = None
  current_target_pos = None
  target_coordinates = []

  def __init__(self, x, y, psi, body):
      self.body = body
      self.wheelbase = self.body.get_wheelbase()
      
  def add_coordinate(self, x, y, psi):
    self.target_coordinates.append((x, y, psi))

  def limit(self, n, min, max):
    if(n < min):
      n = min
    elif(n > max):
      n=max
    return n

  def calculate_velocity(self):
    vl = 0
    vr = 0
    #Is there a target position to move to?
    if(self.current_target_pos != None):
      #calculate distance to target position
      current_pos = self.body.get_pos()
      delta_x = self.current_target_pos[0] - current_pos[0]
      delta_y = self.current_target_pos[1] - current_pos[1] 
      rr = math.sqrt(delta_x**2 + delta_y**2) #distance left to target position
      
      if(rr <= ACCEPTABLE_DISTANCE_DELTA):
        # At target location, remove from list
        self.current_target_pos = None
      else:
        # Calculate new velocity percentage
        #Get current velocity
        vv = self.body.get_velocity()
        if(vv == 0):
          #Current speed is 0 so need to set to default???
          vv = DEFAULT_V
          
        r_angle = math.atan2(delta_y, delta_x)
        
        theta_target = (self.current_target_pos[2] / THETA_TARGET_CONSTANT) - r_angle
        theta_target = self.limit(theta_target, THETA_TARGET_MIN, THETA_TARGET_MAX)
        
        delta_r = (self.body.get_psi() / THETA_TARGET_CONSTANT) - r_angle
        delta_r = self.limit(delta_r, THETA_TARGET_MIN, THETA_TARGET_MAX)
        
        omega_des = -(vv/rr) * (K2 * (delta_r - math.atan(-K1*theta_target)) + math.sin(delta_r) * (1 + (K1 / (1 + ((K1 * theta_target)**2)))))

        vl = vv + ((self.wheelbase / 2) * omega_des)
        vr = vv - ((self.wheelbase / 2) * omega_des)

    return (vl,vr)

  def update(self):
    #No current target but there is another in the list
    if((self.current_target_pos == None) and (len(self.target_coordinates) != 0)):
      #Pop next coordinate from list and set as current target
      self.current_target_pos = self.target_coordinates.pop(0)
    