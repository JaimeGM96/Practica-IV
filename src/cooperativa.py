#---------------------------------------------------------------------------------
# Estructura de datos para almacenar las cooperativas registradas en la aplicación
#---------------------------------------------------------------------------------

from producto import *

class Cooperativa:
    '''
    Constructor del objeto Cooperativa

    Parameters
    ----------
    id : entero
        Identificador único de la cooperativa
    nombre : cadena de caracteres
        Nombre de la cooperativa
    productos : lista de productos
        Lista donde se almacenan los productos de la cooperativa
    '''
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre
        self._productos = list()

    '''
    Getter de id

    Returns
    -------
    id
        id de la cooperativa
    '''
    @property
    def id(self):
        return self._id

    '''
    Getter de nombre

    Returns
    -------
    nombre
        Nombre de la cooperativa
    '''
    @property
    def nombre(self):
        return self._nombre
    
    '''
    Getter de productos

    Returns
    -------
    productos
        Productos de la cooperativa
    '''
    @property
    def productos(self):
        return self._productos