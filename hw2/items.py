from abc import ABC, abstractmethod


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class Gem(IGameItem):
    def open(self):
        print('Gem!')


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class Silver(IGameItem):
    def open(self):
        print('Silver!')


class Bronze(IGameItem):
    def open(self):
        print('Bronze!')


class Iron(IGameItem):
    def open(self):
        print('Iron!')
