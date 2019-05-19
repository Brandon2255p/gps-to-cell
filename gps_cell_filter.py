import math
class hexagonal_cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "cell-{}-{}".format(self.x, self.y)

class gps_cell_filter:
    def __init__(self, radius_km):
        self.radius_km = radius_km

    def convert_radius_to_hexagon(self):
        return self.radius_km * math.sqrt(3) / 2

    def get_hexagon_code(self, x, y):
        hex_y = math.floor(y / self.convert_radius_to_hexagon())
        hex_x = math.floor(x / self.radius_km)
        cell = hexagonal_cell(hex_x, hex_y)
        return cell
        