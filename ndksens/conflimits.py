"""docstring for module conflimits"""

from abc import ABC, abstractmethod
from pathlib import Path
import array
import csv
import math

import numpy as np
from ROOT import TFeldmanCousins
from scipy import interpolate
from scipy.stats import poisson

DATA_PATH = Path(__file__).resolve().parent.parent / "data"


class ConfLimitsCalculator(ABC):
    """dosctring for class ConfLimitsCalculator"""

    def __init__(self, CL):
        self.CL = CL


    @abstractmethod
    def UpperLimit(self, obs: int, bkg: float) -> float:
        ...

    @abstractmethod
    def LowerLimit(self, obs: int, bkg: float) -> float:
        ...

    @abstractmethod
    def AverageUpperLimit(self, bkg: float) -> float:
        ...


class FeldmanCousins(ConfLimitsCalculator):
    """docstring for class FeldmanCousins"""

    def __init__(self, CL=90):
        super().__init__(CL)
        self.FC = TFeldmanCousins(self.CL/100.) # Requires CL as a fraction
        self.FC.SetMuMax(500.)

    def UpperLimit(self, obs, bkg):
        """
        obs: observed number of events
        bkg: mean number of background events
        """
        return self.FC.CalculateUpperLimit(obs,bkg)

    def LowerLimit(self, obs, bkg):
        """
        obs: observed number of events
        bkg: mean number of background events
        """
        return self.FC.CalculateLowerLimit(obs,bkg)

    def AverageUpperLimit(self, bkg):
        """
        For a number of events b, compute the average upper limit. That is:
        UL = Sum Po(n;b) * Upper (n,b)
        """
        ### The Poisson distribution, Po(n;b), is defined only for b>0.
        ### Therefore, this method returns 0 if bkg is negative, and uses
        ### a number close to 0 for the computation if bkg=0.
        if bkg<0.:
            return 0.
        elif bkg==0.:
            bkg=1.E-5

        ### We'll compute the sum in the range [-5sigma, +5sigma] around
        ### the mean, where sigma is the standard deviation of the Poisson
        ### distribution.
        sigma = math.sqrt(bkg)
        nmin = max(0,  int(bkg-5.*sigma))   # Use 0 if nmin<0
        nmax = max(20, int(bkg+5.*sigma)+1) # Use at least 20 for low means
        #print "nmin=%f, nmax=%f" % (nmin,nmax)

        po = poisson(bkg)
        UL = 0.

        for i in range(nmin, nmax):
            pmf = po.pmf(i)
            ul = self.FC.CalculateUpperLimit(i, bkg)
            #print "i=%i, Po(i)=%f, U(i,b)=%f" % (i, pmf, ul)
            UL += pmf * ul

        return UL



class FCMemoizer(FeldmanCousins):
    """docstring for FCMemoizer"""

    def __init__(self, CL=90):
        super(FCMemoizer, self).__init__(CL)
        self.AULs = None

    def ComputeTableAverageUpperLimits(self, bmin, bmax, step, filename):
        """Compute a lookup table of average upper limits."""

        #writer = csv.writer(open(filename, 'w'))
        brange = np.arange(bmin, bmax, step)
        
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)

            for b in brange:
                UL = super(FCMemoizer, self).AverageUpperLimit(b)
                writer.writerow([b,UL])

    def AverageUpperLimit(self, bkg):
        """Use tabulated data (or for large values of bkg, a mathematical 
        function extracted from a fit to the data) to speed up the computation
        of the Feldman-Cousins average upper limit for a given background
        prediction."""

        if bkg < 0:
            return 0.
        elif bkg < 100.:
            return self.AULs(bkg)
        else:
            return self.FitFunction(bkg)

    def ReadTableAverageUpperLimits(self, filename=''):

        if filename == '':
            filename = DATA_PATH + 'FC' + str(self.CL) + '.dat'

        try:
            '''
            reader = csv.reader(open(filename, 'r'))
            '''
            
            with open(filename, newline="") as f:
                reader = csv.reader(f)

                xs = array.array('f')
                ys = array.array('f')

                for row in reader:
                    xs.append(float(row[0]))
                    ys.append(float(row[1]))
                self.AULs = interpolate.interp1d(xs, ys)

        except OSError as exc:
            raise FileNotFoundError(
                f"Cannot read Feldman-Cousins lookup table '{filename}'."
            ) from exc


    def FitFunction(self, x):
        """Returns a value for the Feldman-Cousins average upper limit
        using a mathematical function extracted from a fit to the data."""

        if self.CL==90:
            return 1.225 + 1.7312 * math.sqrt(x)
        else:
            raise ZeroDivisionError


if __name__ == '__main__':

    print("\n| NDKsens.conflimits |\n")

    ##########

    print("# Compute Feldman–Cousins confidence intervals for b = 0 and n = 0–9.")
    print()
    
    fc = FeldmanCousins(90)
    for n in range(10):
        print(
            f" n = {n:d} : "
            f"[{fc.LowerLimit(n, 0):.2f}, {fc.UpperLimit(n, 0):.2f}]"
        )



    ##########

    print("""\n# Compute a lookup table of the average upper limit for CL=68%,
    then use it to calculate the average upper limit for several background 
    predictions.\n""")

    fcm = FCMemoizer(68)
    fcm.ComputeTableAverageUpperLimits(0.5,6.5, 1., 'fcmemoizer.dat')
    fcm.ReadTableAverageUpperLimits('fcmemoizer.dat')
    for b in range(1,6):
        #print " b = %i :  %.2f" % (b, fcm.AverageUpperLimit(b))
        print(f" b = {b:d} : {fcm.AverageUpperLimit(b):.2f}")

