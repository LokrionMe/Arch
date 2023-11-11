from ctypes.wintypes import LONG
import datetime
from decimal import Decimal


class Ticket:
    identificator: LONG
    departure_zone: int
    arrival_zone: int
    route_number: int
    departure_time: datetime
    arrival_time: datetime
    buyer_id: LONG
    is_used: bool
    price: Decimal
    place: str

    def __init__(self, identificator, departure_zone, arrival_zone, route_number, departure_time, arrival_time, buyer_id, price, place) -> None:
        self.identificator = identificator
        self.departure_zone = departure_zone
        self.arrival_zone = arrival_zone
        self.route_number = route_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.buyer_id = buyer_id
        self.is_used = False
        self.price = price
        self.place = place

    def set_is_used(self):
        self.is_used = True

    def get_buyer_id(self):
        return self.buyer_id

    def get_identificator(self):
        return self.identificator

    def get_price(self):
        return self.price

    def set_price(self, new_price: Decimal):
        self.price = new_price
