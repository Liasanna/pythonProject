from ctypes.wintypes import LONG
from hw4.ticket import Ticket


class user:
    identificator: LONG
    name: str
    tickets: list[Ticket]
    login: str
    password_hash_code: LONG
    account_id: LONG

def __init__(self, identificator, name, tickets, login, password_hash_code, account_id) -> None:
    self.identificator = identificator
    self. name = name
    self. tickets = tickets
    self. login = login
    self. password_hash_code = password_hash_code
    self. account_id = account_id

def get_identificator(self):
    return  self.identificator 

def get_name(self):
     return  self.name

def get_tickets(self):
    return  self.tickets

def get_login(self):
    return self.login
    
