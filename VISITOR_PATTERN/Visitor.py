from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_cliente_regular(self, cliente):
        pass

    @abstractmethod
    def visit_cliente_vip(self, cliente):
        pass

    @abstractmethod
    def visit_cliente_corporativo(self, cliente):
        pass