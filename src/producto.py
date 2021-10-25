#-----------------------------------------------------------------------------------
# Estructura de datos para almacenar los productos con los que tratará la aplicación
#-----------------------------------------------------------------------------------

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
    cooperativa : cadena de caracteres
        Cooperativa a la cual pertenece el producto
    '''
    def __init__(self, id, nombre, precio, cooperativa):
        self._id = id
        self._nombre = nombre
        self._precio = precio
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
    Getter de cooperativa

    Returns
    -------
    cooperativa
        Nombre de la cooperativa
    '''
    @property
    def cooperativa(self):
        return self._cooperativa