import numpy

route = 320 # km
weight = 182.5 # Kg
wheels = 3 # Number of wheels
Crr = 0.005 # Coefficient of rolling resistance
Crr2 = 0.0502 # Rolling resistance component related to speed
Ap = 1.1 # Projected frontal area
Cd = 0.13 # Drag coefficient
m = 0.105 #
p = 1 # Fluid density
Vw = numpy.array([5,1]) # Wind velocity
Vv = numpy.array([3,2]) # Vehicle velocity
O = 1 # Slope angle of road

def energyStored(Ein, Eout): # Energy stored in batteries
    return Ein - Eout 

def magnitud(V): # Calculate magnitud of a vector
    return numpy.sqrt(V.dot(V))

def magnitud2(V1, V2): # Calculate magnitud between two vectors
    return numpy.sqrt(V1.dot(V1) - V2.dot(V2))

def yaw(): # Calculate yaw angle
    numerator = magnitud(Vw) - magnitud2(Vw, Vv) - magnitud(Vv)
    denominator = -2*magnitud2(Vw, Vv)*magnitud(Vv)
    return numpy.arccos(numerator/denominator)

def drag(): # Calculate drag
    return ((1/2)*Cd*p*Ap)*magnitud2(Vw, Vv)*numpy.cos(yaw())

def test():
    print(drag())
    print(yaw())

test()