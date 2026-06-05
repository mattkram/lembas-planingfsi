"""Lembas plugin for planingfsi hydrodynamic simulations."""

from lembas_planingfsi.flat_plate import PlaningPlateCase

__all__ = ["PlaningPlateCase", "Plugin"]


class Plugin:
    """Lembas plugin registration."""

    name = "lembas-planingfsi"
    version = "0.1.0"
    case_handlers = [PlaningPlateCase]
