"""Definitions of detector source materials."""

from dataclasses import dataclass

from . import units


@dataclass(frozen=True)
class Source:
    """Properties of a detector source material.

    Attributes
    ----------
    symbol
        Short identifier (e.g. "Ar", "H2O").
    protonsperunitmass
        Number of protons per unit detector mass.
    neutronsperunitmass
        Number of neutrons per unit detector mass.
    """

    symbol: str
    protonsperunitmass: float
    neutronsperunitmass: float


############################################################
# SOURCES --- DATABASE
############################################################

Ar = Source(
    symbol="Ar",
    protonsperunitmass=2.71e32 / units.kton,
    neutronsperunitmass=3.31e32 / units.kton,
)

H2O = Source(
    symbol="H2O",
    protonsperunitmass=3.34e32 / units.kton,
    neutronsperunitmass=2.68e32 / units.kton,
)

############################################################
# DICTIONARY
############################################################

sources = {
    Ar.symbol: Ar,
    H2O.symbol: H2O,
}

__all__ = ["Source", "Ar", "H2O", "sources"]

############################################################

if __name__ == "__main__":
    print("source.py executed directly")
    print(
        f"Protons per kton of argon: "
        f"{Ar.protonsperunitmass * units.kton:.1e}"
    )





    

'''

"""docstring for module source"""

from . import units
#import math



class Source:
    """docstring for Source"""

    def __init__(self, symbol, protonsperunitmass, neutronsperunitmass):
        super().__init__()
        self.symbol = symbol
        self.protonsperunitmass = protonsperunitmass # protons per unit mass
        self.neutronsperunitmass = neutronsperunitmass # neutrons per unit mass


############################################################
### SOURCES --- DATABASE

### Ar
symbol = 'Ar'
protonsperunitmass = 2.71E32*(1/units.kton)
neutronsperunitmass = 3.31E32*(1/units.kton)
Ar = Source(symbol, protonsperunitmass, neutronsperunitmass)

### H2O 
symbol = 'H2O'
protonsperunitmass = 3.34E32*(1/units.kton)
neutronsperunitmass = 2.68E32*(1/units.kton)
H2O = Source(symbol, protonsperunitmass, neutronsperunitmass)



##############################
### DICTIONARY ###############

sources = {Ar.symbol: Ar, H2O.symbol: H2O}

############################################################


if __name__ == '__main__':

    print ("source.py executed directly")
    #print ("Protons per kton of argon: {0:.1e}".format(Ar.protonsperunitmass/(1/units.kton)))
    print ("Protons per kton of argon: ", f"{Ar.protonsperunitmass/(1/units.kton):.1e}")

'''
