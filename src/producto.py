#-----------------------------------------------------------------------------------
# Estructura de datos para almacenar los productos con los que tratará la aplicación
#-----------------------------------------------------------------------------------

from enum import Enum

class Temporada(Enum):
    PRIMAVERA = "primavera"
    VERANO = "verano"
    OTONO = "otono"
    INVIERNO = "invierno"

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
    '''
    def __init__(self, id, nombre, precio, temporadas, cooperativa):
        self._id = id
        self._nombre = nombre
        self._precio = precio
        self._temporadas = temporadas
        self._cooperativa = cooperativa

    '''
    Getter de id

    Returns
    -------
    nombre
        id del producto
    '''
    @property
    def id(self):
        return self._id

    '''
    Getter de nombre

    Returns
    -------
    nombre
        Nombre del producto
    '''
    @property
    def nombre(self):
        return self._nombre

    '''
    Getter de precio

    Returns
    -------
    precio
        Precio del producto
    '''
    @property
    def precio(self):
        return self._precio

    '''
    Getter de temporadas

    Returns
    -------
    estaciones
        Vector de string con las estaciones en las que el producto está disponible
    '''
    @property
    def temporadas(self):
        estaciones = []
        for temporada in self._temporadas:
            estaciones.append(temporada.value)
        
        return estaciones

    '''
    Getter de cooperativa

    Returns
    -------
    cooperativa
        Nombre de la cooperativa
    '''
    @property
    def cooperativa(self):
        return self._cooperativa