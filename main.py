class Asiento:

    coloresPermitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]

    def __init__(self, color:str, precio:int, registro:int):
        self.color = color
        self.precio = precio
        self.registro = registro

    

    def cambiarColor(self, color_:str):
        if color_ in Asiento.coloresPermitidos:
            self.color = color_



class Motor:

    motoresPermitidos = ["electrico", "gasolina"]

    def __init__(self, numerCilindros: int, tipo:str, registro:str):
         self.numeroCilindros = numerCilindros
         self.tipo = tipo
         self.registro = registro

    def cambiarRegistro(self, registro:int):

        self.registro = registro


    def asignarTipo(self, tipo:str):
        if tipo in Motor.motoresPermitidos:
            self.tipo = tipo

class Auto:

    cantidadCreados = 0

    def __init__(self, modelo:str, precio:int, asientos:list,marca:str, motor:Motor, registro: int):

        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        

    def cantidadAsientos(self):

        totalAsiento = 0
        for i in self.asientos:
            if isinstance(i,Asiento):
                totalAsiento += 1
        return totalAsiento
    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asientoActual in self.asientos:
                if asientoActual != None and asientoActual.registro != self.registro:
                    return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"
            



