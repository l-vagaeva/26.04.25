import math
class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x:{self.x} y:{self.y}"
    def distance_to(self, other_point: "Point2D") -> float:
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)
if __name__ == '__main__':

    point1 = Point2D(1, 2)
    point2 = Point2D(4, 6)
    print(point1)
    print(point2)
    distance = point1.distance_to(point2)
    print(f"Расстояние между точками: {distance}") #
