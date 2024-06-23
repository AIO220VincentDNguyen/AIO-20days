import math
# define class point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self, origin):
        return math.sqrt((self.x**2 + origin.x**2) + (self.y**2 + origin.y**2))


point_O = Point(0, 0)

# distance form poitn a(1, 2) to O(0, 0)
point_a = Point(1, 2)
distance_a = point_a.distance_to(point_O)
print(distance_a)

# distance form poitn b(4, 5) to O(0, 0)
point_b = Point(4, 5)
distance_b = point_b.distance_to(point_O)
print(distance_b)