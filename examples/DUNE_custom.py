###

import os.path
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = FILE_PATH + '/../data/'
import sys
sys.path.append(FILE_PATH + '/..')

import csv
from numpy import arange
from ndksens import units
from ndksens import source
from ndksens import mode
from ndksens import experiment
from ndksens import conflimits

FCM = conflimits.FCMemoizer(0.9)
FCM.ReadTableAverageUpperLimits(DATA_PATH+'FC90.dat')

name = 'DUNE_custom'
source = source.Ar
mass = 40*units.kton
eff = 0.47
bgr = 2./(units.Mton*units.year)
DUNE = experiment.Experiment(name, source, mass, mode.p16, eff, bgr)
filename = 'dune_p16.dat'
writer = csv.writer(open(filename, 'w'))

for expo in arange(5.,6005.,5.):
	expo = expo * units.kton * units.year
	sens = DUNE.sensitivity(expo,FCM)
	print expo/(units.kton*units.year), sens/units.year
	writer.writerow([expo/(units.kton*units.year), sens/units.year])
