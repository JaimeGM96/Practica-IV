# Practica-IV
## Descripción
El problema a tratar es la dificultad que tienen los agricultores para saber cuál es el precio de compra de cada producto, frutas y verduras, en las diferentes cooperativas agricolas. Cada cooperativa establece diariamente un precio de cada producto que es la cantidad por kilo que pagará al agricultor. Actualmente si se desea conocer el precio debes acudir personalmente a cada una de ellas. El objetivo de la aplicación es comparar los precios que cada cooperativa pone a cada producto y teniendo en cuenta la distancia a la que se encuentra el agricultor de cada cooperativa, calcular a qué cooperativa le conviene ir. Con esta aplicación conseguiriamos ahorrar tiempo y dinero.

Además de esto, si el agricultor decide vender más de un producto a la vez, se creará la ruta óptima la cuál indicará a qué cooperativas tiene que ir y en cual vender cada producto.

## Instalación y uso
Para usar el proyecto, primero hay que descargar el código. Para ello podemos descargarlo como un zip o clonando el repositorio desde una terminal de esta forma:

```shell
git clone https://github.com/JaimeGM96/Practica-IV.git
```
 
Una vez descargado, iremos a la carpeta del proyecto, abriremos una terminal y ejecutaremos el comando:

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

con esto instalaremos Poetry. Podemos instalarlo usando pip, pero de esta manera, nos puede dar problemas de conflictos de dependencias.
Para comprobar que se ha instalado correctamente, ejecutaremos el comando

```shell
poetry --version
```

Una vez instalado, podremos añadir dependencias de manera muy simple. En nuestro caso necesitamos instalar Poethepoet y lo agregaremos de esta forma:

```shell
poetry add --dev poethepoet
```

con esto lo añadiremos a las dependencias de desarrollo de nuestro repositorio.
Por último nos queda instalar todas las dependencias

```shell
poe installdeps
```

de esta forma, todas las dependencias que aparecen en el archivo pyproject.toml se instalarán.
Para comprobar que el código compila usaremos el comando

```shell
poe check
```

## Documentación
- Para consultar la documentación del proyecto, pulse en este [enlace](docs/documentacion.md).
- Para consultar la justificación de elección del lenguaje, pulse en este [enlace](docs/lenguaje.md).
- Para consultar la elección del gestor de tareas, pulse en este [enlace](docs/gestor_tareas.md).
- Para consultar la elección del gestor de dependencias, pulse en este [enlace](docs/gestor_dependencias.md).