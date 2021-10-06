import numpy

#Parameters for Efficiency of Electrical Systems
#   Module         Efficiency
#Solar Array        14.0%
#MPPT               97.0%
#Battery            80.0%
#Motor+Controller   90.0%

class electricalCaracteristics:
    def __inti__(self, solarArrayEff, MPPTEff, batteryEff, motorAndControllerEff):
        self.solarArrayEff = solarArrayEff
        self.MPPTEff = MPPTEff
        self.batteryEff = batteryEff
        self.motorAndController = motorAndControllerEff

#Parameters for Efficiency of Electrical Systems
#   Module         Efficiency
#Solar Array        14.0%
#MPPT               97.0%
#BatteryEff         80.0%
#Motor+Controller   90.0%

class mechanicalCharacteristics:
    
    def __init__(self, W, N, Crr, Crr2, Ap, Cd, m):
        self.W = W
        self.N  = N
        self.Crr = Crr
        self.Crr2 = Crr2
        self.Ap = Ap
        self.Cd = Cd
        self.m = m

class solarCar:
    
    def __init__(self, electricalParams, mechanicalParams):
        self.electricalParams = electricalParams
        self. mechanicalParams = mechanicalParams

    def Eout(self, ma, Fa, Fr):
    
    
