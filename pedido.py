class Pedido:
    def __init__ (self, numero_pedido: int, fecha: str, total_a_pagar: float):
        self.__numero_pedido = numero_pedido
        self.__fecha = fecha
        self.__total_a_pagar = total_a_pagar

    def procesar(self):
        return "Procesando su pedido :)"

class PedidoEnLocal(Pedido):
    def __init__(self, numero_pedido, fecha, total_a_pagar,numero_de_mesa: int, cantidad_persona: int):
        super().__init__(numero_pedido, fecha, total_a_pagar)
        self.__numero_de_mesa = numero_de_mesa
        self.__cantidad_persona = cantidad_persona
    def procesar(self):
        return "Procesando su pedido en el local"

class PedidoParaLlevar(Pedido):
    def __init__(self, numero_pedido, fecha, total_a_pagar,tiempo_estimado: int):
        super().__init__(numero_pedido, fecha, total_a_pagar)
        self.__tiempo_estimado = tiempo_estimado

    def procesar(self):
        return "Procesando su pedido para llevar"

class PedidoADomicilio(Pedido):
    def __init__(self, numero_pedido, fecha, total_a_pagar,direccion: str, nombre_repartidor: str):
        super().__init__(numero_pedido, fecha, total_a_pagar)
        self.__direccion = direccion
        self.__nombre_repartidor = nombre_repartidor
    def procesar(self):
        return "Procesando su pedido a domicilio"