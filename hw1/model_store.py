from service import Point3D, Angle3D, Color


class Texture:
    pass


class Poligon:
    def __init__(self, point: Point3D):
        self.points: list[Point3D] = [point]


class PoligonalModel:
    def __init__(self, textures: Texture):
        self.Poligons = []
        self.Textures: list[Texture] = textures
        self.Poligons.append(Poligon(Point3D()))


class Flash:
    def __init__(self):
        self.Location: Point3D = None
        self.Angle: Angle3D = None
        self.Color: Color = None
        self.Power: float = None

    def Rotate(self, angleAction: Angle3D):
        pass

    def Move(self, pointAction: Point3D):
        pass


class Camera:
    def __init__(self):
        self.Location: Point3D = None
        self.Angle: Angle3D = None

    def Rotate(self, angleAction: Angle3D):
        pass

    def Move(self, pointAction: Point3D):
        pass


class Scene:
    def __init__(self, identificator, models, flashes, cameras):
        self.identificator: int = identificator

        if len(models) > 0:
            self.Models: list[PoligonalModel] = models
        else:
            raise Exception("Должна быть хотя бы одна модель")

        self.Flashes: list[Flash] = flashes

        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise Exception("Должна быть хотя бы одна камера")

    def method1(self, type):
        return None

    def method2(self, type1, type2):
        return None
