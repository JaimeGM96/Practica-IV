#-----------------------------------------------------------------------------------
# Estructura de datos para almacenar los productos con los que tratará la aplicación
#-----------------------------------------------------------------------------------

from precio import *

class Producto:
    '''
    Constructor del objeto Producto

    Parameters
    ----------
    id : entero
        Identificador único del producto
    nombre : cadena de caracteres
        Nombre del producto
    precio : objeto tipo precio
        Precio por kilo del producto
        Fecha en la que se da ese precio
    '''
    def __init__(self, id, nombre, valor):
        self._id = id
        self._nombre = nombre
        self._precio = Precio(valor)

    '''
    Getter de id

    Returns
    -------
    id
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
        return self._precio.valor
    
    '''
    Getter de fecha

    Returns
    -------
    fecha
        Fecha del precio del producto
    '''
    @property
    def fecha(self):
        return self._precio.fecha