"""
Estructura de datos para almacenar los precios de los productos y la fecha de validez
"""

import datetime

class Precio:
    """
    Clase Precio
    """
    def __init__(self, valor):
        """
        Constructor del objeto Precio

        Parameters:
            valor: punto flotante
                Precio por kilo del producto
        """
        self._valor = valor
        self._fecha = datetime.date.today()

    @property
    def valor(self):
        """
        Getter de valor

        Returns:
            valor: punto flotante
                Precio por kilo del producto
        """
        return self._valor

    @property
    def fecha(self):
        """
        Getter de fecha

        Returns:
            fecha: datetime
                Fecha de vigencia del precio del producto
        """
        return self._fecha
