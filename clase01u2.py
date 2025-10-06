class Pedido:
    def __init__ (self, numero_pedido: int, fecha: str, total_a_pagar: float):
        self.__numero_pedido = numero_pedido
        self.__fecha = fecha
        self.__total_a_pagar = total_a_pagar

    def procesar(self):
        return "Procesando su pedido :)"

class PedidoEnLocal(Pedido):

    def procesar(self):
        return "Procesando su pedido en el local"

class PedidoParaLlevar(Pedido):

    def procesar(self):
        return "Procesando su pedido para llevar"

class PedidoADomicilio(Pedido):

    def procesar(self):
        return "Procesando su pedido a domicilio"
    
pedido_1 = PedidoParaLlevar(1,"05/10/2025",1000.0)
print(f"{pedido_1.procesar()}")