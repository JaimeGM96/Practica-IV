"""
Estructura de datos para almacenar las cooperativas registradas en la aplicación
"""

from agricultor import Agricultor

class Cooperativa:
    """
    Clase Cooperativa
    """
    def __init__(self, id_coop, nombre):
        """
        Constructor del objeto Cooperativa

        Parameters:
            id_coop: entero
                Identificador único de la cooperativa
            nombre: cadena de caracteres
                Nombre de la cooperativa
            productos: lista de productos
                Lista donde se almacenan los productos de la cooperativa
            agricultores: lista de enteros
                Lista donde se almacenan los ids de los agricultores que son socios de la cooperativa
        """
        self._id_coop = id_coop
        self._nombre = nombre
        self._productos = list()
        self._agricultores = list()

    @property
    def id_coop(self):
        """
        Getter de id_coop

        Returns:
            id_coop: entero
                Identificador único de la cooperativa
        """
        return self._id_coop

    @property
    def nombre(self):
        """
        Getter de nombre

        Returns:
            nombre: cadena de caracteres
                Nombre de la cooperativa
        """
        return self._nombre

    @property
    def productos(self):
        """
        Getter de productos

        Returns:
            productos: lista de productos
                Productos de la cooperativa
        """
        return self._productos

    @property
    def agricultores(self):
        """
        Getter de agricultores

        Returns:
            agricultores: lista de enteros
                IDs de los agricultores que son socios de la cooperativa
        """
        return self._agricultores
