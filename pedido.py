class Pedido:
    def __init__ (self, numero_pedido: int, fecha: str, total_a_pagar: float, cliente):
        self.__numero_pedido = numero_pedido
        self.__fecha = fecha
        self.__total_a_pagar = total_a_pagar
        self.cliente = cliente

    def procesar(self):
        return "Procesando su pedido :)"
    
    def obtener_informacion(self):
        return f"Numero Pedido: {self.__numero_pedido}\nNombre del Cliente: {self.cliente.obtener_nombre()}"

class PedidoEnLocal(Pedido):
    def __init__(self, numero_pedido, fecha, total_a_pagar,cliente,numero_de_mesa: int, cantidad_persona: int):
        super().__init__(numero_pedido, fecha, total_a_pagar,cliente)
        self.__numero_de_mesa = numero_de_mesa
        self.__cantidad_persona = cantidad_persona
    def procesar(self):
        return super().obtener_informacion() + "\nNumero de mesa: " + str(self.__numero_de_mesa) + "\nCantidad de personas: " + str(self.__cantidad_persona)

class PedidoParaLlevar(Pedido):
    def __init__(self, numero_pedido, fecha, total_a_pagar,cliente,tiempo_estimado: int):
        super().__init__(numero_pedido, fecha, total_a_pagar,cliente)
        self.__tiempo_estimado = tiempo_estimado

    def procesar(self):
        return super().obtener_informacion() + "\nTiempo estimado: "+ str(self.__tiempo_estimado)

class PedidoADomicilio(Pedido):
    def __init__(self, numero_pedido, fecha, total_a_pagar,cliente,direccion: str, nombre_repartidor: str):
        super().__init__(numero_pedido, fecha, total_a_pagar,cliente)
        self.__direccion = direccion
        self.__nombre_repartidor = nombre_repartidor
    def procesar(self):
        return super().obtener_informacion() + "\nDireccion: " + self.__direccion + "\nNombre del Repartidor: " + self.__nombre_repartidor    
class Cliente:
    def __init__(self, nombre: str, rut: str):
        self.__nombre = nombre
        self.__rut = rut
    def obtener_nombre(self):
        return self.__nombre
    def obtener_rut(self):
        return self.__rut
    
cliente_1 = Cliente("Manuel Aliaga","12345678-9")
pedido_1 = PedidoEnLocal(1001,"07/10/2025",5000.0,cliente_1,54,4)
print(pedido_1.procesar())