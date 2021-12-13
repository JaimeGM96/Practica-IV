# Gestor de tareas
## Introducción
Es importante que ejecutemos test en nuestra aplicación para comprobar que el código funciona correctamente. Además de ejecutarlos, necesitaremos automatizarlos. Para ello se han tenido en cuenta varias herramientas que se encargan de esta función.

## Elección del gestor de tareas
En primer lugar tenemos a invoke. Invoke es una herramienta potente y a la vez clara y sencilla que nos proporciona una API de alto nivel para definir y organizar tareas, entre otras cosas, desde un único archivo task.py. Por otro lado, Pypyr nos permite realizar las tareas mediante pipelines y definirlas en un archivo yaml. En tercer lugar tenemos la herramienta Doit. Esta herramienta también funciona con pipelines además de ser fácil de usar y potente. Esta vez se configura en un archivo dodo.py. Por último Poethepoet es un gestor de tareas que funciona bien con Poetry. Esto es algo esencial ya que Poetry es el gestor de dependencias elegido y es necesario que ambas herramientas funcionen bien. Esto por ejemplo no ocurre con invoke, que da algunos fallos con Poetry. 
Todas las opciones tienen una amplia documentación

He elegido Poethepoet ya que como gestor de dependencias voy a usar Poetry y éste es el gestor de tareas que mejor funciona con él, ya que ejecuta las tareas en el entorno virtual de Poetry. La definición de las tareas se hace en el mismo archivo pyproject.toml de Poetry y además es sencillo de entender y usar.

## Bibliografía
[Invoke](https://www.pyinvoke.org/)
[Pypyr](https://pypyr.io/)
[Doit](https://pydoit.org/)
[Poethepoet](https://github.com/nat-n/poethepoet)