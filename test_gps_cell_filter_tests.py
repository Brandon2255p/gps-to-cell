import pytest
import gps_cell_filter

def test_convert_radius_to_hexagon():
    filter = gps_cell_filter.gps_cell_filter(5)
    hex = filter.convert_radius_to_hexagon()
    assert hex == 4.330127018922193

def test_get_hexagon_code_1():
    test_x = 4
    test_y = 4
    filter = gps_cell_filter.gps_cell_filter(5)
    hexagon = filter.get_hexagon_code(test_x, test_y)
    expected = gps_cell_filter.hexagonal_cell(0, 0)
    assert hexagon == expected

def test_get_hexagon_code_2():
    test_x = 4
    test_y = 5
    filter = gps_cell_filter.gps_cell_filter(5)
    hexagon = filter.get_hexagon_code(test_x, test_y)
    expected = gps_cell_filter.hexagonal_cell(0, 1)
    assert hexagon == expected


def test_get_hexagon_code_3():
    test_x = 6
    test_y = 2
    filter = gps_cell_filter.gps_cell_filter(5)
    hexagon = filter.get_hexagon_code(test_x, test_y)
    expected = gps_cell_filter.hexagonal_cell(1, 0)
    assert hexagon == expected

def test_get_hexagon_code_4():
    test_x = 6
    test_y = -2
    filter = gps_cell_filter.gps_cell_filter(5)
    hexagon = filter.get_hexagon_code(test_x, test_y)
    expected = gps_cell_filter.hexagonal_cell(1, -1)
    assert hexagon == expected

def test_get_hexagon_code_5():
    test_x = 10
    test_y = 10
    filter = gps_cell_filter.gps_cell_filter(5)
    hexagon = filter.get_hexagon_code(test_x, test_y)
    expected = gps_cell_filter.hexagonal_cell(2, 2)
    assert hexagon == expected