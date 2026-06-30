"""Definitions of nucleon-decay search experiments."""

from dataclasses import dataclass

from . import feldmancousins_lookup
from . import mode
from . import source
from . import units


@dataclass
class Experiment:
    """An experimental search for a specific nucleon decay mode."""

    name: str
    source: source.Source
    mass: float
    mode: mode.Mode
    eff: float
    bgr: float

    def Nbkg(self, exposure: float) -> float:
        """Expected number of background events."""
        return self.bgr * exposure

    def sensitivity(self, exposure: float,
                    aul_lookup: feldmancousins_lookup.AverageUpperLimitLookup) -> float:
        """Partial lifetime sensitivity."""
        aul = aul_lookup.average_upper_limit(self.Nbkg(exposure))
        return (
            self.source.protonsperunitmass
            * self.eff
            * exposure
            / aul
        )


############################################################
# DUNE nucleon decay searches
############################################################

argon = source.Ar
detector_mass = 40 * units.kton

dune_p1 = Experiment(
    "dune_p1",
    argon,
    detector_mass,
    mode.p1,
    0.45,
    1.0 / (units.Mton * units.year),
)

dune_n1 = Experiment(
    "dune_n1",
    argon,
    detector_mass,
    mode.n1,
    0.44,
    8.0 / (units.Mton * units.year),
)

dune_p16 = Experiment(
    "dune_p16",
    argon,
    detector_mass,
    mode.p16,
    0.47,
    2.0 / (units.Mton * units.year),
)

dune_p19 = Experiment(
    "dune_p19",
    argon,
    detector_mass,
    mode.p19,
    0.97,
    1.0 / (units.Mton * units.year),
)

dune_n34 = Experiment(
    "dune_n34",
    argon,
    detector_mass,
    mode.n34,
    0.96,
    2.0 / (units.Mton * units.year),
)

dune_p41 = Experiment(
    "dune_p41",
    argon,
    detector_mass,
    mode.p41,
    0.98,
    1.0 / (units.Mton * units.year),
)

experiments = {
    exp.name: exp
    for exp in (
        dune_p1,
        dune_n1,
        dune_p16,
        dune_p19,
        dune_n34,
        dune_p41,
    )
}


if __name__ == "__main__":

    print("experiment.py executed directly")

    dune_test = Experiment(
        "dune_test",
        source.Ar,
        40 * units.kton,
        mode.n1,
        1.0,
        1.0 / (units.Mton * units.year),
    )

    aul_lookup = feldmancousins_lookup.AverageUpperLimitLookup(cl=0.90)
    aul_lookup.read_table()

    sens = dune_test.sensitivity(
        400 * units.kton * units.year,
        FC,
    )

    print(
        f"Sensitivity (90% CL): "
        f"{sens / units.year:.1e} years."
    )


