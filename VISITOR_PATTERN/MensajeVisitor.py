from Visitor import Visitor

class MensajeVisitor(Visitor):
    def visit_cliente_regular(self, cliente):
        print(f"Hola {cliente.nombre}, gracias por ser nuestro cliente regular. ¡Te esperamos pronto!")

    def visit_cliente_vip(self, cliente):
        print(f"Hola {cliente.nombre}, gracias por ser nuestro cliente VIP. ¡Disfruta de nuestros servicios exclusivos!")

    def visit_cliente_corporativo(self, cliente):
        print(f"Hola {cliente.nombre}, gracias por representar a {cliente.direccion}. ¡Nos enorgullece tenerlos como clientes corporativos!")

if __name__ == "__main__":
    from Cliente import ClienteRegular
    from Cliente import ClienteVIP
    from Cliente import ClienteCorporativo
    from datetime import date
    clientes = [
        ClienteRegular("Juan Camilo", date(1985, 6, 15), "Avenida Bolívar Calle 4N"),
        ClienteVIP("Maria Angélica", date(1979, 12, 22), "Edificio Nogal, Calle 6N"),
        ClienteCorporativo("Santiago", date(1990, 3, 8), "Empresa COLTECH, Calle 3N #456")
    ]

    visitor = MensajeVisitor()

    for cliente in clientes:
        cliente.accept(visitor)        