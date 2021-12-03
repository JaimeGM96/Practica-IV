# Gestor de tareas
## Introducción
Es importante que ejecutemos test en nuestra aplicación para comprobar que el código funciona correctamente. Además de ejecutarlos, necesitaremos automatizarlos. Para ello se han tenido en cuenta varias herramientas que se encargan de esta función. Invoke y pypyr.

## Elección del gestor de tareas
Ambos son gestores de tareas que se utilizan, por ejemplo, para la automatización de test que es lo que vamos a necesitar. Invoke nos proporciona una API de alto nivel que nos permite definir y organizar tareas desde un archivo task.py. Por otro lado, pypyr nos permite automatizar tareas a través de un archivo yaml.

Finalmente he elegido invoke ya que me parece simple e intuitivo además de más sencillo que pypyr al tener que implementar solo las funciones que necesitemos en el archivo task.py además de cubrir todas las necesidades del proyecto.