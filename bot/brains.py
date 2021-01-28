import math

DEFAULT_V = 5
ACCEPTABLE_DISTANCE_DELTA = 10
K1 = 1
K2 = 3
RAD_TO_DEGREES_CONSTANT = 57.3
THETA_LIMIT = math.pi


class Brains(): 
  body = None
  wheelbase = None
  current_target_pos = None
  target_coordinates = []

  def __init__(self, x, y, psi, body):
      self.body = body
      self.r = 0
      self.omega = 0
      self.vl = 0
      self.vr = 0
      self.wheelbase = self.body.get_wheelbase()
      
  def add_coordinate(self, x, y, psi):
    self.target_coordinates.append((x, y, psi))
    
  def limit(self, n):
    while(n > math.pi):
      n = n - 2 * math.pi
    while(n < -math.pi):
      n = n + 2 * math.pi
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
        
        theta_target = (self.current_target_pos[2] / RAD_TO_DEGREES_CONSTANT) - r_angle
        theta_target = self.limit(theta_target)
        
        delta_r = (self.body.get_psi() / RAD_TO_DEGREES_CONSTANT) - r_angle
        delta_r = self.limit(delta_r)
        omega_des = -(vv/rr) * (K2 * (r_angle - math.atan(-K1*theta_target)) + math.sin(r_angle) * (1 + (K1 / (1 + ((K1 * theta_target)**2)))))
        
        #delta_d = (vv/rr)*math.sin(self.body.psi)+omega_des
        
        vl = vv - ((self.wheelbase / 2) * omega_des)
        vr = vv + ((self.wheelbase / 2) * omega_des)
        
        #Save data so it can be printed
        self.vl = vl
        self.vr = vr
        self.r = rr
        self.omega = omega_des

    return (vl,vr) 
    
  def update(self):
    #No current target but there is another in the list
    if((self.current_target_pos == None) and (len(self.target_coordinates) != 0)):
      #Pop next coordinate from list and set as current target
      self.current_target_pos = self.target_coordinates.pop(0)
    