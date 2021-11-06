#-----------------------------------------------------------------------------------------------------------
# Estructura de datos para almacenar los precios de los productos y la fecha en la que se dan dichos valores
#-----------------------------------------------------------------------------------------------------------

import datetime

class Precio:
    '''
    Constructor del objeto Precio

    Parameters
    ----------
    valor : punto flotante
        Precio por kilo del producto
    fecha : date
        Fecha en la que se da ese precio
    '''
    def __init__(self, valor):
        self._valor = valor
        self._fecha = datetime.date.today()

    '''
    Getter de valor

    Returns
    -------
    valor
        valor del producto
    '''
    @property
    def valor(self):
        return self._valor

    '''
    Getter de fecha

    Returns
    -------
    fecha
        fecha del producto
    '''
    @property
    def fecha(self):
        return self._fecha