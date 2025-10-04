class Cliente:
    var_Contador = 0
    var_MontoTotal = 0
    def __init__(self,numero_pedido: int, fecha: str, total_a_pagar: float):
        self.__numero_pedido = numero_pedido
        self.__fecha = fecha
        self.__total_a_pagar = total_a_pagar
        Cliente.var_Contador += 1
        Cliente.var_MontoTotal = Cliente.var_MontoTotal + self.__total_a_pagar

    @staticmethod
    def obtenerDetalle():
        return "La cantidad de pedidos creados son: " + str(Cliente.var_Contador) + "\nEl monto total es de $"+ str(Cliente.var_MontoTotal)

class Pedido_en_local(Cliente):
    def __init__(self, numero_pedido, fecha, total_a_pagar, numero_de_mesa: int, cantidad_de_personas: int):
        super().__init__(numero_pedido, fecha, total_a_pagar)
        self.__numero_de_mesa = numero_de_mesa
        self.__cantidad_de_personas = cantidad_de_personas

class Pedido_para_llevar(Cliente):
    def __init__(self, numero_pedido, fecha, total_a_pagar, tiempo_estimado: int):
        super().__init__(numero_pedido, fecha, total_a_pagar)
        self.__tiempo_estimado = tiempo_estimado

class Pedido_a_domicilio(Cliente):
    def __init__(self, numero_pedido, fecha, total_a_pagar, direccion: str, nombre_del_repartidor: str):
        super().__init__(numero_pedido, fecha, total_a_pagar)
        self.__direccion = direccion
        self.__nombre_del_repartidor = nombre_del_repartidor

clienteManuel = Cliente(1001,"04/10/2025",5000.0)
clienteNicolas = Cliente(1002,"04/10/2025",1000.0)
print(f"{Cliente.obtenerDetalle()}")