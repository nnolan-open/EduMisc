
#### physics forces for later
#
#CONTACT FORCES
#
#        mechanical, friction, tension, spring, normal, air resistance, etc... (direct contact)
#
#LONG RANGE FORCES
#
#        gravity, electrostatic, strong nuclear, magnetic
#
#newton = 1kg/m/s^2
#


from math import sqrt,pi

def deg_to_rad(d):
   #super dirty..
   if 'pi' not in globals():
      pi = 3.141592653589793
   return d*pi/180

def rad_to_deg(r):
   #super dirty..
   if 'pi' not in globals():
      pi = 3.141592653589793
   return float(r*180)/pi


# actually just pathagor
def magnitude(A,B):
   return (math.sqrt(A**2+B**2))


#Physics classes seem to like degrees. 
#Matlab has builtin's called sind and cosd. 
#just recreating that. Should expand to sec,tan, ar*
def sind(D):
   R = (D*math.pi/180)
   return(math.sin(R))

def cosd(D):
   R = (D*math.pi/180)
   return(math.cos(R))


