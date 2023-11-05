from model_store import Flash, Camera, Scene, PoligonalModel
from abc import ABCMeta, abstractmethod


class IModelChangedObserver(ABCMeta):
    @abstractmethod
    def apply_update_model(self):
        """обноволение модели"""


class IModelChanger(ABCMeta):
    @abstractmethod
    def notify_change(self, sender: IModelChanger):
        """оповещение(?)"""


class ModelStore(IModelChanger):

    def __init__(self, changed_observer: list[IModelChangedObserver]) -> None:
        self.models: list[PoligonalModel] = []
        self.scenes: list[Scene] = []
        self.flashes: list[Flash] = []
        self.cameras: list[Camera] = []
        self.change_observers = changed_observer

        textures = []
        self.models.append(PoligonalModel(textures))
        self.cameras.append(Camera())
        self.flashes.append(Flash())
        self.scenes.append(Scene(0, self.models, self.flashes, self.cameras))

    def get_scene(self, ident: int):
        for scene in self.scenes:
            if scene.identificator == ident:
                return scene

    def notify_change(self, sender: IModelChanger):
        pass
