# Star Wars API REST - CRUD Endpoints

Este proyecto consiste en la construcción de una **API REST** con **Python** y **Flask**, utilizando **SQLAlchemy** como ORM y **PostgreSQL** como base de datos.

El objetivo principal es practicar la creación de endpoints y operaciones CRUD (**GET, POST, PUT y DELETE**) para diferentes recursos dentro de una base de datos inspirada en el universo de **Star Wars**.

## Tecnologías utilizadas
- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- PostgreSQL
- Flask-CORS

## Recursos disponibles
La API permite gestionar los siguientes recursos:

- **User**
- **Character**
- **Planet**

## Endpoints CRUD implementados

### User
- `GET /user` → obtener todos los usuarios
- `GET /user/<id>` → obtener un usuario específico
- `POST /user` → crear un usuario
- `PUT /user/<id>` → actualizar un usuario
- `DELETE /user/<id>` → eliminar un usuario

### Character
- `GET /character` → obtener todos los personajes
- `GET /character/<id>` → obtener un personaje específico
- `POST /character` → crear un personaje
- `PUT /character/<id>` → actualizar un personaje
- `DELETE /character/<id>` → eliminar un personaje

### Planet
- `GET /planet` → obtener todos los planetas
- `GET /planet/<id>` → obtener un planeta específico
- `POST /planet` → crear un planeta
- `PUT /planet/<id>` → actualizar un planeta
- `DELETE /planet/<id>` → eliminar un planeta

## Objetivo del proyecto
Este proyecto fue creado como práctica para:
- construir endpoints REST desde cero
- aprender el flujo completo de creación/modificación/borrado en una base de datos
- mejorar la organización y estructura de una API con Flask

---
Proyecto desarrollado por Cristian.
