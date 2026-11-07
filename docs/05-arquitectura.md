# 05. Arquitectura del sistema — Barber Studio API

## 1. Introducción

Este documento describe la arquitectura inicial de Barber Studio API, un backend desarrollado con Python y FastAPI para gestionar las reservaciones de una barbería.

La arquitectura busca mantener el código organizado, facilitar las pruebas y permitir que el sistema incorpore nuevas funcionalidades conforme avance el desarrollo.

## 2. Arquitectura seleccionada

Se utilizará una **arquitectura monolítica modular por capas**.

Esto significa que el backend funcionará como una sola aplicación, pero sus componentes estarán organizados de acuerdo con sus responsabilidades.

La arquitectura permitirá separar la recepción de solicitudes HTTP, la lógica de negocio y las operaciones de acceso a datos.

No se utilizarán microservicios durante el MVP, ya que agregarían complejidad que no resulta necesaria para el alcance inicial.

## 3. Capas principales

### 3.1 Capa de API

**Directorio previsto:** `app/api/`

Responsabilidades:

- Definir los endpoints HTTP.
- Recibir las solicitudes de los clientes.
- Utilizar esquemas para validar los datos.
- Invocar los servicios correspondientes.
- Devolver respuestas HTTP.

Esta capa no deberá concentrar la lógica de negocio ni las consultas directas a la base de datos.

### 3.2 Esquemas de datos

**Directorio previsto:** `app/schemas/`

Responsabilidades:

- Definir las estructuras de entrada y salida.
- Validar tipos y formatos de datos.
- Utilizar modelos Pydantic.
- Evitar exponer información innecesaria en las respuestas.

Los esquemas no sustituyen las reglas de negocio ni los modelos de persistencia.

### 3.3 Capa de servicios

**Directorio previsto:** `app/services/`

Responsabilidades:

- Implementar las reglas de negocio.
- Coordinar los procesos de reservación.
- Comprobar disponibilidad.
- Gestionar confirmaciones y verificaciones.
- Aplicar las políticas de permisos correspondientes.
- Coordinar las operaciones que requieren acceso a datos.

Por ejemplo, esta capa determinará si una reservación puede confirmarse según las reglas establecidas.

### 3.4 Capa de acceso a datos

**Directorio previsto:** `app/repositories/`

Responsabilidades:

- Consultar información almacenada.
- Registrar y actualizar entidades.
- Encapsular las operaciones de persistencia.
- Facilitar la separación entre la lógica de negocio y la base de datos.

### 3.5 Modelos de persistencia

**Directorio previsto:** `app/models/`

Responsabilidades:

- Representar las entidades almacenadas.
- Definir las relaciones entre entidades.
- Utilizar SQLAlchemy para el mapeo objeto-relacional.

Los modelos de persistencia serán diferentes de los esquemas utilizados para las solicitudes y respuestas HTTP.

## 4. Componentes adicionales

| Directorio o archivo | Responsabilidad |
|---|---|
| `app/main.py` | Inicializar FastAPI y registrar las rutas. |
| `app/core/` | Centralizar configuración y funciones de seguridad compartidas. |
| `app/db/` | Configurar la conexión y las sesiones de base de datos. |
| `tests/` | Organizar las pruebas automatizadas. |
| `docs/` | Almacenar documentación técnica del proyecto. |
| `README.md` | Presentar el proyecto e indicar cómo ejecutarlo. |
| `.gitignore` | Excluir archivos innecesarios o sensibles del seguimiento de Git. |

## 5. Estructura prevista

```text
barber-studio-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── models/
│   ├── core/
│   └── db/
├── tests/
├── docs/
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

Esta estructura es una propuesta inicial. Los directorios se crearán progresivamente cuando sean necesarios.

## 6. Flujo general de una solicitud

El funcionamiento esperado seguirá este proceso:

1. Un cliente realiza una solicitud HTTP.
2. FastAPI recibe la solicitud mediante un endpoint.
3. Los esquemas validan la estructura de los datos.
4. La capa de servicios aplica las reglas de negocio.
5. Los repositorios realizan las operaciones necesarias sobre los datos.
6. PostgreSQL almacena o proporciona la información.
7. El sistema devuelve una respuesta HTTP al cliente.

En los procesos de reservación pública, el backend también coordinará el envío y la validación de códigos por correo electrónico.

Las operaciones críticas de disponibilidad y confirmación deberán protegerse contra condiciones de carrera mediante mecanismos adecuados de persistencia y concurrencia.

## 7. Tecnologías

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal del backend. |
| FastAPI | Desarrollo de la API REST. |
| Uvicorn | Servidor ASGI. |
| Pydantic | Validación y serialización de datos. |
| PostgreSQL | Base de datos relacional prevista. |
| SQLAlchemy | Acceso y mapeo de datos. |
| Alembic | Migraciones de base de datos. |
| Pytest | Pruebas automatizadas. |
| Git y GitHub | Control de versiones y colaboración. |
| Docker | Contenedorización del backend. |
| GitHub Actions | Automatización de pruebas y procesos de integración continua. |
| AWS | Posible entorno de despliegue en la nube. |

Las tecnologías que todavía no se han incorporado se integrarán progresivamente.

## 8. Seguridad

La arquitectura deberá considerar:

- Almacenamiento seguro de contraseñas mediante hashing.
- Autenticación y autorización de usuarios.
- Validación de datos de entrada.
- Protección de secretos mediante variables de entorno.
- Control de acceso a agendas y operaciones administrativas.
- Protección contra abuso de los endpoints públicos.
- Integridad de las reservaciones ante solicitudes simultáneas.
- Registro de eventos sin exponer información sensible.

Las credenciales, claves privadas y datos personales reales no deberán incluirse en el repositorio.

## 9. Decisiones arquitectónicas

**DA-01 — Aplicación monolítica modular**

Se selecciona una sola aplicación backend organizada por responsabilidades, en lugar de microservicios.

**DA-02 — Separación por capas**

Las rutas HTTP, la lógica de negocio y las operaciones de persistencia tendrán responsabilidades diferenciadas.

**DA-03 — API REST con FastAPI**

Fast