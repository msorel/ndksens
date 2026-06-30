"""Generate a custom DUNE nucleon-decay sensitivity curve."""

from pathlib import Path

import csv
import numpy as np

from ndksens import feldmancousins_lookup
from ndksens import experiment
from ndksens import mode
from ndksens import source
from ndksens import units


DATA_PATH = Path(__file__).resolve().parent.parent / "data"


def main():
    # Feldman-Cousins average upper limits
    aul_lookup = feldmancousins_lookup.AverageUpperLimitLookup(cl=0.90)
    aul_lookup.read_table(DATA_PATH / "FC90.dat")

    # Custom DUNE configuration
    dune = experiment.Experiment(
        name="DUNE_custom",
        source=source.Ar,
        mass=40 * units.kton,
        mode=mode.p16,
        eff=0.47,
        bgr=2.0 / (units.Mton * units.year),
    )

    output_file = Path("dune_p16.dat")

    with output_file.open("w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        for exposure_kty in np.arange(5.0, 6005.0, 5.0):
            exposure = exposure_kty * units.kton * units.year
            sensitivity = dune.sensitivity(exposure, aul_lookup)

            exposure_value = exposure / (units.kton * units.year)
            sensitivity_value = sensitivity / units.year

            print(
                f"{exposure_value:.1f} kton·yr   "
                f"{sensitivity_value:.3e} years"
            )

            writer.writerow(
                [
                    f"{exposure_value:.1f}",
                    f"{sensitivity_value:.3e}",
                ]
            )


if __name__ == "__main__":
    main()

    

