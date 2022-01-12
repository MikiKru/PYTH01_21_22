class Point2D:
    def __init__(self, x, y):
        print("init z klasy P2D")
        self.x = x
        self.y = y
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def __str__(self):
        return f"x={self.x} y={self.y}"

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)         # wywołuje __init klasy nadrzędnej
        print("init z klasy P3D")
        self.z = z
    def set_z(self, z):
        self.z = z
    def __str__(self):
        return super().__str__() + f" z={self.z}"
p2d = Point2D(2, 3)
print(p2d)

p3d = Point3D(1, 2, 3)
print(p3d)