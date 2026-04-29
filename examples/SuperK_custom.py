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

name = 'superk_p1'
source = source.H2O
mass = 22.5*units.kton
# p19: take efficiency and background numbers from arXiv:1408.1195 Super-K publication, summing contributions from prompt gamma and pi+ pi0
# eff: 9.1% + 10.0% = 19.1%
# p16 eff = 6.7+3.0% = 9.7% from Tab.I SK-III numbers in arXiv:1205.6538, only Ks -> pi0 pi0 and Ks -> pi+ pi- method 2 
# p1 eff = 45.0% for SK-IV from arXiv:1203.4030
eff = 0.450
# p19 bgr: 1.5/Mt*yr + 2.0/Mt*yr = 3.5 / Mt*yr
# p16 bgr: (6.0+2.8)  /Mt*yr = 8.8 / Mt*yr
# p1 bgr: 1.7 /Mt*yr for SK-IV from arXiv:1203.4030
bgr = 1.7/(units.Mton*units.year)
SuperK = experiment.Experiment(name, source, mass, mode.p1, eff, bgr)
filename = 'superk_p1.dat'
writer = csv.writer(open(filename, 'w'))

for expo in arange(5.,6005.,5.):
	expo = expo * units.kton * units.year
	sens = SuperK.sensitivity(expo,FCM)
	print expo/(units.kton*units.year), sens/units.year
	writer.writerow([expo/(units.kton*units.year), sens/units.year])
