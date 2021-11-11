from invoke import task, run

@task
def install(c, dev=False):
    """
    Tarea encargada de la instalación de las dependencias necesarias para el funcionamiento de la aplicación.

    Si queremos instalar las dependencias de desarrollo, usaremos el flag --dev
    """
    c.run("pip install -r requirements.txt")

    if dev:
        c.run("pip install -r requirements-dev.txt")

@task
def test(c):
    """
    Tarea encargada de ejecutar los test de la aplicación.
    """
    print("No hay test actualmente...")

@task
def check(c):
    """
    Tarea encargada de comprobar la sintaxis de los ficheros de la aplicación.
    """
    c.run("pylint src")