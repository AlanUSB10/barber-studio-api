# Barber Studio API

Backend de un sistema de gestión de reservaciones para una barbería, desarrollado con Python y FastAPI.

## Objetivo

Desarrollar una API REST que permita gestionar reservaciones, horarios de trabajo, disponibilidad de barberos y servicios de una barbería.

El proyecto busca facilitar la administración de citas, reducir los conflictos de horarios y permitir que los clientes soliciten reservaciones sin depender exclusivamente de WhatsApp.

## Funcionalidades previstas

- Consultar barberos, servicios y horarios disponibles.
- Solicitar reservaciones con verificación por correo electrónico.
- Registrar manualmente citas recibidas por WhatsApp.
- Consultar, modificar y cancelar reservaciones.
- Administrar horarios de trabajo y bloqueos.
- Gestionar permisos de barberos y administradores.

## Tecnologías

- Python 3.14
- FastAPI
- Uvicorn
- Git y GitHub
- PostgreSQL (previsto)
- Docker (previsto)

## Estado del proyecto

**En desarrollo.**

Actualmente se encuentra implementado un endpoint inicial de bienvenida. Las funcionalidades de reservaciones y administración se desarrollarán progresivamente.

## Ejecución local

Desde la carpeta raíz del proyecto, crear un entorno virtual:

```powershell
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias iniciales:

```powershell
python -m pip install "fastapi[standard]"
```

Iniciar el servidor:

```powershell
python -m uvicorn app.main:app --reload
```

La API estará disponible en:

`http://127.0.0.1:8000/`

Documentación interactiva:

`http://127.0.0.1:8000/docs`

## Arquitectura

El proyecto seguirá una arquitectura monolítica modular por capas, separando las rutas HTTP, la lógica de negocio y el acceso a datos.

## Documentación

Los requisitos, casos de uso y decisiones de arquitectura se organizarán en el directorio `docs/` conforme avance el desarrollo.