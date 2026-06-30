"""Definitions of nucleon decay modes."""

from dataclasses import dataclass

from . import units


@dataclass(frozen=True)
class Mode:
    """Description of a nucleon decay mode.

    Attributes
    ----------
    symbol
        Short identifier (e.g. "p1", "n34").
    name
        Human-readable decay mode name.
    pdgnumber
        PDG decay-mode identifier.
    nucleontype
        Nucleon type:
            0 = proton
            1 = neutron
    pdglimit
        Current experimental lower limit on the partial lifetime.
    """

    symbol: str
    name: str
    pdgnumber: int
    nucleontype: int
    pdglimit: float


############################################################
# NUCLEON DECAY MODES --- DATABASE
#
# The decay-mode numbering follows the Particle Data Group
# convention. Lifetime limits are taken from the PDG review.
############################################################

#
# Antilepton + single meson
#

p1 = Mode(
    symbol="p1",
    name="p2epluspizero",
    pdgnumber=1,
    nucleontype=0,
    pdglimit=24000e30 * units.year,
)

n1 = Mode(
    symbol="n1",
    name="n2epluspiminus",
    pdgnumber=1,
    nucleontype=1,
    pdglimit=5300e30 * units.year,
)

p16 = Mode(
    symbol="p16",
    name="p2mupluskzero",
    pdgnumber=16,
    nucleontype=0,
    pdglimit=4500e30 * units.year,
)

p19 = Mode(
    symbol="p19",
    name="p2nubarkplus",
    pdgnumber=19,
    nucleontype=0,
    pdglimit=5900e30 * units.year,
)

#
# Lepton + multiple mesons
#

n34 = Mode(
    symbol="n34",
    name="n2eminuskplus",
    pdgnumber=34,
    nucleontype=1,
    pdglimit=32e30 * units.year,
)

p41 = Mode(
    symbol="p41",
    name="p2muminuspipluskplus",
    pdgnumber=41,
    nucleontype=0,
    pdglimit=245e30 * units.year,
)

############################################################
# DICTIONARY
############################################################

modes = {
    mode.symbol: mode
    for mode in (
        p1,
        n1,
        p16,
        p19,
        n34,
        p41,
    )
}

__all__ = [
    "Mode",
    "p1",
    "n1",
    "p16",
    "p19",
    "n34",
    "p41",
    "modes",
]

############################################################

if __name__ == "__main__":
    print("mode.py executed directly")
    


