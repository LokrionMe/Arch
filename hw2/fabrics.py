from abc import ABC, abstractmethod
from items import Gem, Gold, Silver, Bronze, Iron


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()


class BronzeGenerator(ItemFabric):
    def create_item(self):
        return Bronze()


class IronGenerator(ItemFabric):
    def create_item(self):
        return Iron()
