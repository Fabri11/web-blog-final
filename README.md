# Blog

.-Proyecto de página web programado con Python y utilizando framework django

Iniciamos el proyecto creando un entorno virtual e instalando Django en nuestro proyecto mediante la CMD de Windows
---------------------
#Documentos: Creación de proyecto Django (python -m django startproject "nombre del proyecto")

Creación de app Django (python -m django startapp App)

Se linkea los estilos de bootstrap mediante la etiqueta en nuestro template layout.html el cual lanza los estilos para el proyecto.

Se realiza herencias padre a hijo renderizando las vistas a la plantilla utilizada.

Dependencias Instaladas:
---------------------
.- Django-Import-Export: para guardar nuestros objetos en formato json o el archivo que deseemos en caso de perderlos.
		$pip install django-import-export

.-Django-ckeditor: para la personalizacion en nuestro apartado admin, como usuario editar nuestras publicaciones de una forma
			 mas sencilla.
		$pip install django-ckeditor
.- Django Humanize : Para la personalizacion mas legible a la hora de visualizar la fecha exacta del posteo.
		(en nuestro archivo settings.py) 'django.contrib.humanize'

#Templates:
---------------------
Organizamos los templates de manera ordenada que sea fácil de leer, mediante carpeta principal " Templates "

y una secundaria para código HTML de menor importancia llamado " Partials "

#Archivos.py:
---------------------
Encontraremos algunos de los siguientes documentos.

models.py Aquí encontramos el modelado de los datos que se utilizaron para el proyecto y base de datos

forms.py Se crearon los formularios necesarios para poder cargar datos en nuestra base de datos desde la página web.

views.py Son las vistas creadas a partir de nuestros modelos y formularios para navegar por la web

urls.py Ubicación de las rutas utilizadas en el proyecto

#Buscar y cargar

Podremos subir nuevos posts, como tambien podremos subir nuestros proyectos y buscarlos mediante nuetro " Search "
