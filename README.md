# Proyecto de entrega parcial para el curso de Python | CoderHouse

_Entrega para el curso de python con Django, desarrollado en Coderhouse_

## Descripción del proyecto

_Blog informativo que cuenta con diferentes funcionalidades para gestionar. Inicialmente lo que se puede hacer por medio de este blog es cargar Categorias, post o publicaciones y comentarios. Tambien se encuentra habilitada la funcionalidad para buscar diferentes post o publicaciones ya existentes. Se agrega un panel admin para gestionar los contenidos y el perfil de usuario. A dicho panel se accede por un login. Tambien cuenta con la seccion de registro de usurios._

### Lo que se incluye en esta entrega

* Armado y maquetado de template en base a la funcionalida de un blog
* Herencia de templates para el maquetado
* Modelado de datos: categories, post, comments
* Panel admin. Secciones de login, register y edicion de usuario.
### Como funciona el blog en esta entrega

* Dentro del blog podemos encontrar las secciones de Home o Inicio, About me, Search Posts, Create Data y Contact.
* Las secciones de Home, About me y Contact tienen informacion ficticia, mas que nada a modo de tener la maqueta ajustada.
* Las secciones de Search Posts y Create Data se encuentran funcionales: Se pueden buscar posts existentes en nuestra base de datos (actualmente con sqlite3) y se pueden dar de alta categorias, publicaciones y comentarios, desde la seccion de Create Data.

### Como funciona el panel admin

* En primera instancia podremos loguearnos con el superuser que se da de alta cuando clonamos el proyecto.
* Accedemos desde: http://127.0.0.1:8000/accounts/login/
* Dentro de este panel admin, contamos con un _dashboard_ para la gestion de contenidos: Editar nuestro perfil, ver y cargar categorias y posts.

### Project setup

* `Clone the repo`
* `sudo apt install python3.9-venv`
* `python3 -m venv venv`
* `. venv/bin/activate`
* `python -m pip install -r requirements.txt`
* `python3 manage.py migrate`
* `python3 manage.py runserver`

### Create superuser to access admin panel

* `python3 manage.py createsuperuser`
* Enter /admin directory in the web app

## VIDEO DEMO
[![DEMO](https://srojasweb.dev/2022/coderhouse/django/login.png)](https://srojasweb.dev/2022/coderhouse/django/videos/demo-init.mp4)

## some previews

### home:
![BANNER](https://srojasweb.dev/2022/coderhouse/django/preview-blog-django.jpg)

### login:
![ADMIN-PROFILE](https://srojasweb.dev/2022/coderhouse/django/login.png)

### dashboard:
![ADMIN-DASHBOARD](https://srojasweb.dev/2022/coderhouse/django/dashboard.png)
### user profile:
![ADMIN-PROFILE](https://srojasweb.dev/2022/coderhouse/django/profile.png)





