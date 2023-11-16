from ctypes.wintypes import LONG
import datetime
from decimal import Decimal


class Ticket:
    identificator: LONG
    departure_zone: int
    arrival_zone: int
    route_number: int:
    departure_time: datetime
    arrival_time: datetime
    buyer_id: LONG
    is_used: bool
    price: Decimal
    price: str

def __init__

