# IDLE (Python 3.8.0)

# Constants

# Possible Constants Related To Worms

def PCRTW():
    MinLOHP = # ly 
    # MinLOHP means Minimum Length Of Hyperspace Pathway.
    MaxLOHP = # ly
    # MaxLOHP means Maximum Length Of HP.
    MSDBITOHP = 0.0001369863 # ly
    # MSDBITOHP means Minimum Safe Distance Between Intermediate Terminals Of HPs. Note:
    # 0.0001369863 ly is 0.5 days of travel at 0.1 c. It's 1 295 103 418.56 km. 
    MinLOW = # km
    # MinLOW means Minimum Length Of Worm.
    MinDOW = # km
    # MinDOW means Minimum Diameter Of Worm.
    MaxDOW = # km
    # MaxDOW means Maximum Diameter Of Worm.
    TOH = # km
    # TOH means Thickness Of Hull.
    DOCC = # km
    # DOCC means Diameter Of Conduit Coil.
    DOHP = # km
    # DOHP means Diameter Of HP.
    HC = (TOH + DOCC) * 2
    MMF = MaxDOW / MinDOW
    # MMF means Maximum Multiplication Factor for diameter of worm.
    MaxLOHPCWWOVD = ((MaxDOW + (HC * MMF - HC)) / MinDOW) ** 2 * MinLOHP
    # MaxLOHPCWWOVD means Maximum Length Of HP Created With Worm Of Variable Diameter.
