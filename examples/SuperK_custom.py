"""Generate a Super-Kamiokande nucleon-decay sensitivity curve."""

from pathlib import Path

import csv
import numpy as np

from ndksens import conflimits
from ndksens import experiment
from ndksens import mode
from ndksens import source
from ndksens import units


DATA_PATH = Path(__file__).resolve().parent.parent / "data"


def main():
    # Feldman-Cousins average upper limits
    fcm = conflimits.FCMemoizer(90)
    fcm.ReadTableAverageUpperLimits(DATA_PATH / "FC90.dat")

    # p → ν̄K⁺:
    #   efficiency = 9.1% + 10.0% = 19.1%
    #   background = 1.5 + 2.0 = 3.5 events/(Mt·yr)
    #   Source: arXiv:1408.1195
    #
    # p → μ⁺K⁰:
    #   efficiency = 6.7% + 3.0% = 9.7%
    #   background = 6.0 + 2.8 = 8.8 events/(Mt·yr)
    #   Source: arXiv:1205.6538
    #
    # p → e⁺π⁰ (SK-IV):
    #   efficiency = 45.0%
    #   background = 1.7 events/(Mt·yr)
    #   Source: arXiv:1203.4030
    
    # Super-Kamiokande detector configuration
    superk = experiment.Experiment(
        name="superk_p1",
        source=source.H2O,
        mass=22.5 * units.kton,
        mode=mode.p1,
        eff=0.450,
        bgr=1.7 / (units.Mton * units.year),
    )

    output_file = Path("superk_p1.dat")

    with output_file.open("w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        for exposure_kty in np.arange(5.0, 6005.0, 5.0):
            exposure = exposure_kty * units.kton * units.year
            sensitivity = superk.sensitivity(exposure, fcm)

            exposure_value = exposure / (units.kton * units.year)
            sensitivity_value = sensitivity / units.year

            print(
                f"{exposure_value:7.1f} kton·yr   "
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






