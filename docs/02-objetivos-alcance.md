# 02. Objetivos y alcance del proyecto

## 1. Objetivo general

Desarrollar una API REST utilizando Python y FastAPI para administrar las reservaciones de una barbería, permitiendo consultar disponibilidad, gestionar agendas y organizar las citas de manera centralizada.

## 2. Objetivos específicos

- Permitir que los clientes consulten los servicios, barberos y horarios disponibles.
- Implementar un sistema de reservaciones con verificación por correo electrónico.
- Evitar que se registren citas superpuestas para un mismo barbero.
- Permitir que cada barbero gestione su propia agenda y sus horarios de trabajo.
- Facilitar el registro manual de reservaciones recibidas mediante WhatsApp.
- Incorporar un administrador con permisos para gestionar la operación general.
- Aplicar buenas prácticas de desarrollo, seguridad, documentación y pruebas.

## 3. Alcance del MVP

La primera versión del sistema contemplará las siguientes funcionalidades:

### 3.1 Reservaciones públicas

Los clientes podrán seleccionar un servicio, un barbero y un horario disponible.

Para confirmar una reservación deberán verificar su correo electrónico mediante un código temporal.

El sistema mantendrá el horario reservado provisionalmente durante un máximo de cinco minutos mientras se realiza la verificación.

### 3.2 Gestión de agendas

Cada barbero podrá:

- Consultar sus reservaciones.
- Registrar citas manualmente.
- Reprogramar y cancelar citas.
- Bloquear periodos de su agenda.
- Modificar sus horarios habituales de trabajo.

Las citas manuales se confirmarán inmediatamente cuando cumplan las reglas de disponibilidad, sin requerir verificación por correo electrónico.

### 3.3 Administración

El administrador podrá:

- Consultar y modificar las agendas de todos los barberos.
- Gestionar los servicios de la barbería.
- Administrar la información de los barberos.
- Modificar los horarios de trabajo.
- Supervisar las reservaciones.

### 3.4 Seguridad y validaciones

El sistema deberá incluir:

- Autenticación para las funciones privadas.
- Autorización según el rol del usuario.
- Validación de datos recibidos.
- Protección básica contra solicitudes abusivas.
- Prevención de conflictos de reservaciones, incluso ante solicitudes simultáneas.
- Manejo adecuado de errores.

### 3.5 Calidad técnica

El proyecto incorporará progresivamente:

- Documentación de endpoints mediante OpenAPI.
- Pruebas automatizadas de funcionalidades críticas.
- Registro de eventos relevantes.
- Control de versiones mediante Git.
- Organización del código mediante una arquitectura monolítica modular por capas.

## 4. Funcionalidades fuera del MVP

Las siguientes características podrán desarrollarse en versiones posteriores:

- Pagos electrónicos y anticipos.
- Notificaciones automáticas por WhatsApp.
- Aplicación móvil.
- Panel avanzado de estadísticas.
- Integración de inteligencia artificial.
- Funcionalidades avanzadas de automatización.

Estas características no son necesarias para considerar funcional la primera versión del backend.

## 5. Criterios generales de éxito

El MVP se considerará funcional cuando:

1. Un cliente pueda consultar disponibilidad y confirmar una reservación mediante verificación por correo.
2. El sistema impida conflictos de horarios entre reservaciones.
3. Cada barbero pueda consultar y administrar su propia agenda.
4. Las reservaciones manuales y públicas compartan la misma disponibilidad.
5. El administrador pueda gestionar las agendas y la información básica de la barbería.
6. Las operaciones privadas estén protegidas mediante autenticación y autorización.
7. Las funcionalidades principales cuenten con pruebas y documentación.

## 6. Evolución del proyecto

El desarrollo se realizará por etapas, comenzando con los fundamentos del backend y los endpoints básicos.

Posteriormente se incorporarán PostgreSQL, seguridad, pruebas automatizadas, contenedores y despliegue en la nube.

Las funcionalidades futuras se evaluarán una vez que el MVP esté implementado y probado.