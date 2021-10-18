#-----------------------------------------------------------------------------------
# Estructura de datos para almacenar los productos con los que tratará la aplicación
#-----------------------------------------------------------------------------------

from enum import Enum

class Temporada(Enum):
    PRIMAVERA = "primavera"
    VERANO = "verano"
    OTONO = "otono"
    INVIERNO = "invierno"

class Tipo(Enum):
    FRUTA = "fruta"
    VERDURA = "verdura"
    LEGUMBRE = "legumbre"
    CEREAL = "cereal"

class Producto:
    '''
    Constructor del objeto Producto

    Parameters
    ----------
    id : entero
        Identificador único del producto
    nombre : cadena de caracteres
        Nombre del producto
    precio : entero de coma flotante
        Precio por kilo del producto
    temporadas : vector de Temporada
        Estaciones en las cuales está disponible el producto
    cooperativa : cadena de caracteres
        Cooperativa a la cual pertenece el producto
    tipo : enum de Tipo
        Tipo de producto
    '''
    def __init__(self, id, nombre, precio, temporadas, cooperativa, tipo):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.temporadas = temporadas
        self.cooperativa = cooperativa
        self.tipo = tipo

    '''
    Getter de temporadas

    Returns
    -------
    estaciones
        Vector de string con las estaciones en las que el producto está disponible
    '''
    def getTemporadas(self):
        estaciones = []
        for temporada in self.temporadas:
            estaciones.append(temporada.value)
        
        return estaciones

    '''
    Getter de tipo
    
    Returns
    -------
    tipo.value
        Valor del enumerado tipo
    '''
    def getTipo(self):
        return self.tipo.value