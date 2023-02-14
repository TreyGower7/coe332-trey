from analyze_water import calc_turb, calc_time_to_fall
import pytest

data = {"turbidity_data":[{"calibration_constant": 3,"detector_current": 3}, {"calibration_constant": 1,"detector_current": 1}]}


def test_calc_turb():
    assert calc_turb(data, 'turbidity_data', 2) == 5 

def test_calc_time_to_fall():
    assert calc_time_to_fall(1.1992) == 8.992
