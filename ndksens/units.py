"""Basic system of units (copied from Geant4).

The basic units are :
            millimeter              (millimeter)
            nanosecond              (nanosecond)
            Mega electron Volt      (MeV)
            positron charge         (eplus)
            degree Kelvin           (kelvin)
            the amount of substance (mole)
            luminous intensity      (candela)
            radian                  (radian)
            steradian               (steradian)

Below is a non exhaustive list of derived and pratical units 
(i.e. mostly the SI units). You can add your own units.

The SI numerical value of the positron charge is defined here,
as it is needed for conversion factor : positron charge = e_SI (coulomb)
"""

from math import pi

# ---------------------------------------------------------------------
# Length [L]
# ---------------------------------------------------------------------

millimeter = 1.0                        
millimeter2 = millimeter * millimeter
millimeter3 = millimeter * millimeter * millimeter

centimeter = 10.0 * millimeter   
centimeter2 = centimeter * centimeter
centimeter3 = centimeter * centimeter * centimeter

meter = 1000.0 * millimeter                  
meter2 = meter * meter
meter3 = meter * meter*meter

kilometer = 1000.0 * meter                   
kilometer2 = kilometer * kilometer
kilometer3 = kilometer * kilometer * kilometer

parsec = 3.0856775807e+16 * meter

micrometer = 1e-6 * meter             
nanometer = 1e-9 * meter
angstrom = 1e-10 * meter
fermi = 1e-15 * meter

barn = 1e-28 * meter2
millibarn = 1e-3 * barn
microbarn = 1e-6 * barn
nanobarn = 1e-9 * barn
picobarn = 1e-12* barn

## Symbols
mm = millimeter                        
mm2 = millimeter2
mm3 = millimeter3

cm = centimeter   
cm2 = centimeter2
cm3 = centimeter3

m = meter                  
m2 = meter2
m3 = meter3

km = kilometer                   
km2 = kilometer2
km3 = kilometer3

pc = parsec


# ---------------------------------------------------------------------
# Angle
# ---------------------------------------------------------------------


radian = 1.0                  
milliradian = 1e-3 * radian

degree = (pi / 180.0) * radian

steradian = 1.0
        
## symbols
rad = radian      
mrad = milliradian
sr = steradian
deg = degree


# ---------------------------------------------------------------------
# Time [T]
# ---------------------------------------------------------------------


nanosecond  = 1.0
second = 1e+9 * nanosecond
millisecond = 1e-3 * second
microsecond = 1e-6 * second
picosecond = 1e-12 * second

year = 31556925.445 * second

hertz = 1.0 / second
kilohertz = 1e+3 * hertz
megahertz = 1e+6 * hertz

## symbols
ns = nanosecond                    
s = second
ms = millisecond


# ---------------------------------------------------------------------
# Electric charge [Q]
# ---------------------------------------------------------------------

eplus = 1.0                 ## positron charge
e_SI = 1.60217733e-19     ## positron charge in coulomb
coulomb = eplus / e_SI       ## coulomb = 6.24150 e+18 * eplus


# ---------------------------------------------------------------------
# Energy [E]
# ---------------------------------------------------------------------


megaelectronvolt = 1.0 
electronvolt = 1e-6 * megaelectronvolt
millielectronvolt = 1e-9 * megaelectronvolt
kiloelectronvolt = 1e-3 * megaelectronvolt
gigaelectronvolt = 1e+3 * megaelectronvolt
teraelectronvolt = 1e+6 * megaelectronvolt
petaelectronvolt = 1e+9 * megaelectronvolt

joule = electronvolt / e_SI  ## joule = 6.24150 e+12 * MeV

## symbols
MeV = megaelectronvolt
eV = electronvolt
meV = millielectronvolt
keV = kiloelectronvolt
GeV = gigaelectronvolt
TeV = teraelectronvolt
PeV = petaelectronvolt


# ---------------------------------------------------------------------
# Mass [E][T^2][L^-2]
# ---------------------------------------------------------------------


kilogram = joule * second * second / (meter * meter)   
gram = 1e-3 * kilogram
milligram = 1e-3 * gram
tonne = 1e+3 * kilogram
kilotonne = 1e+3 * tonne
megatonne = 1e+3 * kilotonne

## symbols
kg = kilogram
g = gram
mg = milligram
ton = tonne
kton = kilotonne 
Mton = megatonne


# ---------------------------------------------------------------------
# Power [E][T^1]
# ---------------------------------------------------------------------

watt = joule / second        ## watt = 6.24150 e+3 * MeV/ns


# ---------------------------------------------------------------------
# Force [E][L^-1]
# ---------------------------------------------------------------------


newton = joule / meter       ## newton = 6.24150 e+9 * MeV/mm


# ---------------------------------------------------------------------
# Pressure [E][L^-3]
# ---------------------------------------------------------------------


pascal = newton/m2        ## pascal = 6.24150 e+3 * MeV/mm3
bar = 100000 * pascal ## bar    = 6.24150 e+8 * MeV/mm3
atmosphere = 101325 * pascal ## atm    = 6.32420 e+8 * MeV/mm3


# ---------------------------------------------------------------------
# Electric current [Q][T^1]
# ---------------------------------------------------------------------


ampere = coulomb / second ## ampere = 6.24150 e+9 * eplus/ns
milliampere = 1e-3 * ampere
microampere = 1e-6 * ampere
nanoampere  = 1e-9 * ampere


# ---------------------------------------------------------------------
# Electric potential [E][Q^-1]
# ---------------------------------------------------------------------


megavolt = megaelectronvolt / eplus
kilovolt = 1e-3 * megavolt
volt = 1e-6 * megavolt


# ---------------------------------------------------------------------
# Electric resistance [E][T][Q^-2]
# ---------------------------------------------------------------------


ohm = volt / ampere  ## ohm = 1.60217e-16*(MeV/eplus)/(eplus/ns)


# ---------------------------------------------------------------------
# Electric capacitance [Q^2][E^-1]
# ---------------------------------------------------------------------


farad = coulomb / volt       ## farad = 6.24150e+24 * eplus/Megavolt
millifarad = 1e-3 * farad
microfarad = 1e-6 * farad
nanofarad = 1e-9 * farad
picofarad = 1e-12 * farad


# ---------------------------------------------------------------------
# Magnetic Flux [T][E][Q^-1]
# ---------------------------------------------------------------------


weber = volt * second        ## weber = 1000*megavolt*ns


# ---------------------------------------------------------------------
# Magnetic Field [T][E][Q^-1][L^-2]
# ---------------------------------------------------------------------

tesla = volt * second / meter2     ## tesla =0.001*megavolt*ns/mm2

gauss = 1e-4 * tesla
kilogauss = 1e-1 * tesla


# ---------------------------------------------------------------------
# Inductance [T^2][E][Q^-2]
# ---------------------------------------------------------------------


henry = weber / ampere       ## henry = 1.60217e-7*MeV*(ns/eplus)**2


# ---------------------------------------------------------------------
# Temperature
# ---------------------------------------------------------------------

kelvin = 1.0


# ---------------------------------------------------------------------
# Amount of substance
# ---------------------------------------------------------------------

mole = 1.0


# ---------------------------------------------------------------------
# Activity [T^-1]
# ---------------------------------------------------------------------

becquerel = 1.0 / second 
curie = 3.7e+10 * becquerel


# ---------------------------------------------------------------------
# Absorbed dose [L^2][T^-2]
# ---------------------------------------------------------------------

gray = joule / kilogram 


# ---------------------------------------------------------------------
# Luminous intensity [I]
# ---------------------------------------------------------------------

candela = 1.0


# ---------------------------------------------------------------------
# Luminous flux [I]
# ---------------------------------------------------------------------

lumen = candela * steradian


# ---------------------------------------------------------------------
# Illuminance [I][L^-2]
# ---------------------------------------------------------------------

lux = lumen / meter2


# ---------------------------------------------------------------------
# Miscellaneous
# ---------------------------------------------------------------------

perCent = 0.01 
perThousand = 0.001
perMillion = 0.000001
