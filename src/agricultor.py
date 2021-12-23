"""
Estructura de datos para almacenar los agricultores registrados en la aplicación
"""

from cooperativa import Cooperativa

class Agricultor:
    """
    Clase Agricultor
    """
    def __init__(self, id_agri, nombre):
        """
        Constructor del objeto Agricultor

        Parameters:
            id_agri: entero
                Identificador único del agricultor
            nombre: cadena de caracteres
                Nombre del agricultor
            cooperativas: lista de enteros
                Lista donde se almacenan los IDs de las cooperativas a las que pertenece el agricultor
        """
        self._id_agri = id_agri
        self._nombre = nombre
        self._cooperativas = list()

    @property
    def id_agri(self):
        """
        Getter de id_agri

        Returns:
            id_agri: entero
                Identificador único del agricultor
        """
        return self._id_agri

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
            cooperativas: lista de enteros
                Lista donde se almacenan los IDs de las cooperativas a las que pertenece el agricultor
        """
        return self._cooperativas
