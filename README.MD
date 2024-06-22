Proyecto Final Francisco Contartese, Curso Python Coderhouse

ProyectoFinal es una aplicación web desarrollada en Django que permite a los usuarios registrarse y crear, ver, editar y eliminar carreras universitarias con su respectiva descripción,  . El sistema de autenticación y autorización restringe el acceso a ciertas funciones a usuarios no registrados. Incluye también un sistema de edición de perfil y manejo de los avatars, como también un apartado de admin donde se puede manejar toda la pagina, por ultimo tambien incluye un sistema de inicio y de salido de sesion.

Funcionalidades:

A continuación se detallan las funcionalidades de ProyectoFinal:

Registro y autenticación:

Los usuarios pueden registrarse haciendo click en "CREAR USUARIO".
Los usuarios pueden iniciar sesión en "LOGIN".
Los usuarios pueden cerrar sesión en la aplicación en cualquier momento en "LOGOUT".
Explicar
Explicar
carreras universitarias: Los usuarios pueden agregar sus carreras universitarias haciendo click en "agregar", una vez agregado lo pueden "editar","eliminar" y "detallar". 

Búsqueda de carreras: Los usuarios pueden buscar carreras guardadas en la base de datos 


Administración: Los usuarios con permisos de administrador pueden ver, editar, eliminar y agregar todo.

AboutMe Cualquiera que entre a la página puede ver el AboutMe sobre el creador de la página.

Requerimientos: Antes de poder utilizar ProyectoFinal, debe tener instalado lo siguiente: Python 3.12.3

Instalación Para instalar ProyectoFinal, siga estos pasos:

Clonar el repositorio de ProyectoFinal en su máquina local utilizando el siguiente comando: git clone 

Navegue hasta el directorio ProyectoFinal utilizando el comando cd ProyectoFinal.
Cree un entorno virtual utilizando el comando python3 -m venv venv.
Active el entorno virtual utilizando el comando source venv/bin/activate.
Instale los paquetes necesarios utilizando el comando pip install -r requirements.txt.
Configure la base de datos utilizando el comando python manage.py migrate.
Ejecute la aplicación utilizando el comando python manage.py runserver.


