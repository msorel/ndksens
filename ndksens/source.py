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



    

