class Cliente:
    var_Contador = 0
    def __init__(self,numero_pedido: int, fecha: str, total_a_pagar: float):
        self.__numero_pedido = numero_pedido
        self.__fecha = fecha
        self.__total_a_pagar = total_a_pagar
        Cliente.var_Contador += 1
    def obtenerDetalle(self):
        return "Numero de pedido:" + str(self.__numero_pedido) + " creado con exito!" + "\nEres el pedido n°" + str(Cliente.var_Contador) + "\nCon un total a pagar de $" + str(self.__total_a_pagar)

class Pedido_en_local(Cliente):
    def __init__(self, numero_pedido, fecha, total_a_pagar, numero_de_mesa: int, cantidad_de_personas: int):
        super().__init__(numero_pedido, fecha, total_a_pagar)
        self.__numero_de_mesa = numero_de_mesa
        self.__cantidad_de_personas = cantidad_de_personas
    def obtenerDetalle(self):
        pass

class Pedido_para_llevar(Cliente):
    def __init__(self, numero_pedido, fecha, total_a_pagar, tiempo_estimado: int):
        super().__init__(numero_pedido, fecha, total_a_pagar)
        self.__tiempo_estimado = tiempo_estimado

class Pedido_a_domicilio(Cliente):
    def __init__(self, numero_pedido, fecha, total_a_pagar, direccion: str, nombre_del_repartidor: str):
        super().__init__(numero_pedido, fecha, total_a_pagar)
        self.__direccion = direccion
        self.__nombre_del_repartidor = nombre_del_repartidor
    def obtenerDetalle(self):
        return super().obtenerDetalle() + "\nTu repartidor es: " + str(self.__nombre_del_repartidor) + "\nVa en direccion hacia: " + str(self.__direccion)

clienteManuel = Pedido_a_domicilio(1001,"05/10/2025",1500.0,"Mi casa #123","Chamo")
print(f"{clienteManuel.obtenerDetalle()}")