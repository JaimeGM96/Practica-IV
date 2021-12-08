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
pip install invoke
```

Cuando tengamos invoke, pasaremos a instalar las dependencias con el comando:

```shell
invoke install
```

y si queremos instalar también las dependencias de desarrollo, ejecutaremos:

```shell 
invoke install --dev
```

En cuanto a la ejecución de los test, usaremos:

```shell
invoke test
```

Para la comprobación de la sintaxis del código, usaremos:

```shell
invoke check
```

## Documentación
- Para consultar la documentación del proyecto, pulse en este [enlace](docs/documentacion.md).
- Para consultar la justificación de elección del lenguaje, pulse en este [enlace](docs/lenguaje.md).
- Para consultar la elección del gestor de tareas, pulse en este [enlace](docs/gestor_tareas.md).
- Para consultar la elección del gestor de dependencias, pulse en este [enlace](docs/gestor_dependencias.md).