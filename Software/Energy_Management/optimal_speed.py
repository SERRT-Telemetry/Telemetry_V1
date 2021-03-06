import numpy
import sympy

route = 320  # km
W = 182.5  # Kg
N = 3  # Number of wheels
Crr = 0.005  # Coefficient of rolling resistance
Crr2 = 0.0502  # Rolling resistance component related to speed
Ap = 1.1  # Projected frontal area
Cd = 0.13  # Drag coefficient
m = 0.105
p = 1.2  # Fluid density
Vw = numpy.array([1, 1])  # Wind velocity
Vv = numpy.array([3, 2])  # Vehicle velocity
Os = 0  # Slope angle of road
a = 1  # Acceleration of vehicle
g = 9.81  # Gravity
to = 1  # Initial time
tmax = 2  # Max time
Ind = 1  # Direct incident solar radiation
Is = 1  # Scattered solar radiation
Ih = 1  # Total horizontal solar radiation
O = 1  # Angle
B = 1  # Angle
pr = 1  # Ground refelctance
u = 1  # Overall energy conversion efficency
EBo = 5664  # Initial energy stored in batteries
ub = 1  # Batteries efficency
t = sympy.Symbol("t")  # Integration symbol
k = sympy.Symbol("k")  # Sumation symbol
Ca = 8  # Effective collector area
Nsa = 5 # Number of solar arrays


def magnitud(V):  # Calculate magnitud of a vector
    return numpy.sqrt(V.dot(V))


def magnitud2(V1, V2):  # Calculate magnitud between two vectors
    return numpy.sqrt(V1.dot(V1) - V2.dot(V2))


def cos(x):
    return sympy.cos(x)


def sin(x):
    return sympy.sin(x)


def yaw():  # Calculate yaw angle
    numerator = magnitud(Vw) - magnitud2(Vw, Vv) - magnitud(Vv)
    denominator = -2*magnitud2(Vw, Vv)*magnitud(Vv)
    return numpy.arccos(numerator/denominator)


def drag():  # Calculate drag
    return ((1/2)*Cd*p*Ap)*magnitud2(Vw, Vv)*numpy.cos(yaw())


def dotEout():  # Expended energy
    return W*(numpy.sin(Os)+Crr*numpy.cos(Os))*Vv+N*Crr2*Vv ^ 2*1/2*Cd*Ap*p*Vv(Vv+Vw) ^ 2+((W*a)/(2*g))*Vv


def Eout():  # Total energy used
    return sympy.integrate(dotEout(), (t, to, tmax))


def dotEin():  # Entering energy
    return sympy.summation(Ind*cos(O)+Is*(1+cos(B))/2 + pr*Ih*(1-cos(B))/2, (k, 1, Nsa))


def EinTotal():  # Total entering energy
    return sympy.integrate(u*dotEin(), (t, to, tmax)) + ub*EBo


def energyBalance():  # Energy stored in batteries
    return EinTotal() - Eout()


def test():  # Test functions
    print(EinTotal())


test()