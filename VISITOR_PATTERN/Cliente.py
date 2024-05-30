from datetime import date
from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nombre, fecha_nacimiento, direccion):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion

    @abstractmethod
    def accept(self, visitor):
        pass

class ClienteRegular(Cliente):
    def accept(self, visitor):
        visitor.visit_cliente_regular(self)

class ClienteVIP(Cliente):
    def accept(self, visitor):
        visitor.visit_cliente_vip(self)

class ClienteCorporativo(Cliente):
    def accept(self, visitor):
        visitor.visit_cliente_corporativo(self)    