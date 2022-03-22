# Proyecto de entrega parcial para el curso de Python | CoderHouse

_Entrega para el curso de python con Django, desarrollado en Coderhouse_

## Descripción del proyecto

_Blog informativo que cuenta con diferentes funcionalidades para gestionar. Inicialmente lo que se puede hacer por medio de este blog es cargar Categorias, post o publicaciones y comentarios. Tambien se encuentra habilitada la funcionalidad para buscar diferentes post o publicaciones ya existentes_

### Lo que se incluye en esta entrega parcial

* Armado y maquetado de template en base a la funcionalida de un blog
* Herencia de templates para el maquetado
* Modelado de datos: Categories, post, comments
* Primeros pasos de un crud para la gestion de datos: Actualmente esta realizado el proceso de crear datos para los diferentes modelos. 
### Como funciona el blog en esta entrega

* Dentro del blog podemos encontrar las secciones de Home o Inicio, About me, Search Posts, Create Data y Contact.
* Las secciones de Home, About me y Contact tienen informacion ficticia, mas que nada a modo de tener la maqueta ajustada.
* Las secciones de Search Posts y Create Data se encuentran funcionales: Se pueden buscar posts existentes en nuestra base de datos (actualmente con sqlite3) y se pueden dar de alta categorias, publicaciones y comentarios, desde la seccion de Create Data.

### Project setup

* `Clone the repo`
* `python3 -m venv venv`
* `. venv/bin/activate`
* `python -m pip install -r requirements.txt`
* `python3 manage.py migrate`
* `python3 manage.py runserver`

### Create superuser to access admin panel

* `python3 manage.py createsuperuser`
* Enter /admin directory in the web app


### some preview:
![BANNER](https://srojasweb.dev/2022/coderhouse/django/preview-blog-django.jpg)



