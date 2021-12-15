"""
Estructura de datos para almacenar los agricultores registrados en la aplicación
"""

from cooperativa import Cooperativa

class Agricultor:
    """
    Clase Agricultor
    """
    def __init__(self, nombre):
        """
        Constructor del objeto Agricultor

        Parameters:
            nombre: cadena de caracteres
                Nombre del agricultor
            cooperativas: lista de cooperativas
                Lista donde se almacenan las cooperativas a las que pertenece el agricultor
        """
        self._nombre = nombre
        self._cooperativas = list()

    @property
    def nombre(self):
        """
        Getter de nombre

        Returns:
            nombre: cadena de caracteres
                Nombre del agricultor
        """
        return self._nombre

    @property
    def cooperativas(self):
        """
        Getter de cooperativas

        Returns:
            cooperativas: lista de cooperativas
                Lista donde se almacenan las cooperativas a las que pertenece el agricultor
        """
        return self._cooperativas
