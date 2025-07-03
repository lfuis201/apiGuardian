# apiGuardian

API REST para autenticación y protección de accesos, basada en Django y JWT. Incluye documentación Swagger, auditoría de peticiones y seguridad contra ataques de fuerza bruta.

## Repositorio

[https://github.com/lfuis201/apiGuardian](https://github.com/lfuis201/apiGuardian)

## Entorno de Producción

* **API Base:**
  [https://apiguardian.bashuabrand.com/api](https://apiguardian.bashuabrand.com/api)
* **Documentación Swagger (OpenAPI 3):**
  [https://apiguardian.bashuabrand.com/api/docs/](https://apiguardian.bashuabrand.com/api/docs/)

## Infraestructura

* VPS en **DigitalOcean**
* Sistema operativo: **Ubuntu Linux**
* Base de datos: **PostgreSQL**
* Proxy reverso con HTTPS: **Caddy v2**
* Servidor de aplicaciones: **Gunicorn**

## Frameworks y Librerías Principales


| Herramienta                   | Propósito                                             |
| ----------------------------- | ------------------------------------------------------ |
| Django 5.2.3                  | Framework principal para backend                       |
| Django REST Framework         | API RESTful                                            |
| dj-rest-auth                  | Autenticación lista para usar (login, registro, etc.) |
| djangorestframework-simplejwt | Tokens JWT con refresh y blacklist                     |
| django-allauth                | Gestión de usuarios y login social                    |
| drf-spectacular               | Documentación Swagger/OpenAPI 3                       |
| django-axes                   | Protección contra ataques de fuerza bruta             |
| python-decouple               | Manejo de variables de entorno (`.env`)                |

## Middleware Personalizado

**AuditLogMiddleware**
Registra cada petición HTTP con método, usuario, IP, cuerpo y respuesta, excepto rutas `/admin` y `/static`.

Ruta: `api_guardian_auditoria.middleware.AuditLogMiddleware`

## Base de Datos

* Motor: **PostgreSQL**
* Gestión de variables sensibles: **`.env` + python-decouple**
* Ubicación: VPS en producción (DigitalOcean)

## Despliegue

Producción mediante:

* **Gunicorn** como servidor WSGI
* **Caddy** como proxy reverso con certificados SSL automáticos

## Documentación Técnica

Los siguientes documentos se incluyen en formato PDF:

* **Manual de Usuario:**`_Manual_usuario_apiGuardian.pdf`
* **Memoria Técnica Descriptiva:**`memoria_tecnica_apiGuardian.pdf`
