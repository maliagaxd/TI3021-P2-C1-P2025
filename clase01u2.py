class Cliente:
    def __init__(self,numero_pedido: int, fecha: str, total_a_pagar: float):
        self.__numero_pedido = numero_pedido
        self.__fecha = fecha
        self.__total_a_pagar = total_a_pagar
    @staticmethod
    def procesar(procesar):
        print(procesar)

class Pedido_en_local(Cliente):
    pass

class Pedido_para_llevar(Cliente):
    pass

class Pedido_a_domicilio(Cliente):
    pass