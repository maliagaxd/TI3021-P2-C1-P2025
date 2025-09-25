class Cliente:
    def __init__(self,nombre: str,rut: str, edad: int):
        self.__nombre = nombre
        self.__rut = rut
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre

cliente1: Cliente = Cliente(
    nombre="Manuel",
    rut="20499483-8",
    edad=25
    )
print(cliente1.nombre)