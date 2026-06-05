"""Tests for the planing plate case handler."""

from lembas_planingfsi import PlaningPlateCase


def test_case_instantiation() -> None:
    """Test that we can create a case with valid parameters."""
    case = PlaningPlateCase(froude_num=1.0, angle_of_attack=5.0)
    assert case.froude_num == 1.0
    assert case.angle_of_attack == 5.0


def test_case_dir_naming() -> None:
    """Test that case directory is named correctly."""
    case = PlaningPlateCase(froude_num=1.5, angle_of_attack=10.0)
    assert "Fr=1.50_AOA=10.00" in str(case.case_dir)
