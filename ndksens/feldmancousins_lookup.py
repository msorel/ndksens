"""docstring for module feldmancousins_lookup."""

from pathlib import Path
import csv
import math

import numpy as np
from .feldmancousins import FeldmanCousins
from scipy import interpolate

DATA_PATH = Path(__file__).resolve().parent.parent / "data"


class AverageUpperLimitLookup:
    """
    docstring for AverageUpperLimitLookup.
    This is the lookup-table implementation of the
    Feldman–Cousins average upper limit calculation.
    """

    def __init__(self, cl=0.90):
        self.cl = cl
        self.fc = FeldmanCousins(cl) # Requires CL as a fraction
        self.interpolator = None

    def write_table(self, bmin, bmax, step, filename):
        """Compute a lookup table of average upper limits."""

        brange = np.arange(bmin, bmax, step)
        
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)

            for b in brange:
                UL = self.fc.average_upper_limit(b)
                writer.writerow([b,UL])


    def read_table(self, filename=''):

        if filename == '':
            filename = DATA_PATH / f"FC{int(100*self.CL)}.dat"

        try:
            '''
            reader = csv.reader(open(filename, 'r'))
            '''
            
            with open(filename, newline="") as f:
                reader = csv.reader(f)

                xs = []
                ys = []

                for row in reader:
                    xs.append(float(row[0]))
                    ys.append(float(row[1]))
                self.interpolator = interpolate.interp1d(xs, ys)

        except OSError as exc:
            raise FileNotFoundError(
                f"Cannot read Feldman-Cousins lookup table '{filename}'."
            ) from exc


    def average_upper_limit(self, bkg):
        """Use tabulated data (or for large values of bkg, a mathematical 
        function extracted from a fit to the data) to speed up the computation
        of the Feldman-Cousins average upper limit for a given background
        prediction."""

        if bkg < 0:
            return 0.
        elif bkg < 100.:
            return self.interpolator(bkg)
        else:
            return self.fit_function(bkg)

        
    def fit_function(self, x):
        """Returns a value for the Feldman-Cousins average upper limit
        using a mathematical function extracted from a fit to the data."""

        if self.cl==0.90:
            return 1.225 + 1.7312 * math.sqrt(x)
        else:
            raise NotImplementedError(
                f"No asymptotic fit available for CL={int(100*self.cl)}%."
            )


if __name__ == '__main__':

    print("\n| NDKsens.conflimits |\n")

    ##########

    print("# Compute Feldman–Cousins confidence intervals for b = 0 and n = 0–9.")
    print()
    
    fc = FeldmanCousins(0.90)
    for n in range(10):
        print(
            f" n = {n:d} : "
            f"[{fc.lower_limit(n, 0):.2f}, {fc.upper_limit(n, 0):.2f}]"
        )



    ##########

    print("""\n# Compute a lookup table of the average upper limit for CL=68%,
    then use it to calculate the average upper limit for several background 
    predictions.\n""")

    lookup = AverageUpperLimitLookup(cl=0.68)
    lookup.write_table(0.5,6.5, 1., 'lookup.dat')
    lookup.read_table('lookup.dat')
    for b in range(1,6):
        print(f" b = {b:d} : {lookup.average_upper_limit(b):.2f}")

