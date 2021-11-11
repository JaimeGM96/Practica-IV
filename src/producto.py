"""
Estructura de datos para almacenar los productos con los que tratará la aplicación
"""

from precio import Precio

class Producto:
    """
    Clase Producto
    """
    def __init__(self, iden, nombre, valor):
        """
        Constructor del objeto Producto

        Parameters:
            iden: entero
                Identificador único del producto
            nombre: cadena de caracteres
                Nombre del producto
            precio: objeto tipo precio
                Precio por kilo del producto
                Fecha en la que se da ese precio
        """
        self._iden = iden
        self._nombre = nombre
        self._precio = Precio(valor)

    @property
    def iden(self):
        """
        Getter de id

        Returns:
            iden: entero
                Identificador único del producto
        """
        return self._iden

    @property
    def nombre(self):
        """
        Getter de nombre

        Returns:
            nombre: cadena de caracteres
                Nombre del producto
        """
        return self._nombre

    @property
    def precio(self):
        """
        Getter de precio

        Returns:
            precio: punto flotante
                Precio del producto
        """
        return self._precio.valor

    @property
    def fecha(self):
        """
        Getter de fecha

        Returns:
            fecha: datetime
                Fecha del precio del producto
        """
        return self._precio.fecha
        