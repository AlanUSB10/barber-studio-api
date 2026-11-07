# 03. Requisitos del sistema

## 1. Introducción

Este documento establece los requisitos funcionales, no funcionales y las reglas de negocio de Barber Studio API.

Los requisitos corresponden al Producto Mínimo Viable (MVP) y servirán como referencia durante el desarrollo, las pruebas y el mantenimiento.

## 2. Requisitos funcionales (RF)

| ID | Requisito |
|---|---|
| RF-01 | El sistema deberá permitir consultar el catálogo de barberos y servicios disponibles. |
| RF-02 | El sistema deberá mostrar los horarios disponibles de cada barbero según la fecha seleccionada. |
| RF-03 | Los clientes podrán solicitar reservaciones indicando barbero, servicio, fecha, horario y correo electrónico. |
| RF-04 | El sistema deberá generar y enviar un código de verificación al correo del cliente. |
| RF-05 | El sistema deberá validar el código recibido y confirmar la reservación cuando se cumplan las condiciones establecidas. |
| RF-06 | Los barberos podrán autenticarse y consultar sus propias agendas. |
| RF-07 | Los barberos podrán registrar manualmente reservaciones recibidas por WhatsApp u otros medios. |
| RF-08 | Los barberos podrán bloquear periodos de sus agendas. |
| RF-09 | Los barberos podrán reprogramar y cancelar sus reservaciones. |
| RF-10 | El administrador podrá consultar y supervisar las agendas de todos los barberos. |
| RF-11 | Las reservaciones confirmadas deberán reflejarse en la agenda correspondiente. |
| RF-12 | El administrador podrá gestionar la información básica de barberos, servicios y horarios. |

## 3. Requisitos no funcionales (RNF)

| ID | Requisito |
|---|---|
| RNF-01 | Las contraseñas deberán almacenarse utilizando algoritmos de hashing seguros. |
| RNF-02 | Las operaciones privadas deberán protegerse mediante autenticación y autorización. |
| RNF-03 | El sistema deberá validar los datos recibidos y proporcionar respuestas de error consistentes, sin exponer información sensible. |
| RNF-04 | Se implementarán controles contra solicitudes abusivas, especialmente en reservaciones y verificaciones de correo. |
| RNF-05 | El sistema deberá preservar la integridad de las reservaciones ante solicitudes simultáneas. |
| RNF-06 | Se registrarán eventos relevantes para diagnóstico y seguimiento, evitando almacenar secretos en los registros. |
| RNF-07 | Los endpoints deberán contar con documentación OpenAPI. |
| RNF-08 | Las funcionalidades críticas deberán contar con pruebas automatizadas. |
| RNF-09 | El entorno de ejecución y las dependencias deberán poder reproducirse de manera documentada. |

## 4. Reglas de negocio (RN)

### 4.1 Disponibilidad y reservaciones

| ID | Regla |
|---|---|
| RN-01 | No podrán existir reservaciones confirmadas superpuestas para un mismo barbero. |
| RN-02 | Las reservaciones deberán respetar los horarios de trabajo y bloqueos de cada barbero. |
| RN-03 | Las reservaciones públicas requerirán verificación de correo electrónico antes de confirmarse. |
| RN-04 | El código de verificación tendrá una vigencia máxima de cinco minutos. |
| RN-05 | Una reservación pendiente no podrá bloquear un horario indefinidamente. |
| RN-07 | Las reservaciones manuales deberán cumplir las restricciones de disponibilidad y horarios. |
| RN-08 | La duración del servicio deberá considerarse al calcular los horarios disponibles. |
| RN-09 | Una solicitud pública válida podrá retener temporalmente el horario seleccionado durante la verificación. |
| RN-10 | La retención temporal tendrá una duración máxima de cinco minutos. |
| RN-11 | Una verificación válida y realizada dentro del plazo permitirá confirmar la reservación, siempre que se cumplan las demás condiciones. |
| RN-12 | Cuando expire la retención temporal, el horario deberá volver a estar disponible si no existe otra restricción. |
| RN-13 | No podrán existir retenciones activas ni reservaciones confirmadas que se superpongan para un mismo barbero. |

### 4.2 Permisos y administración de agendas

| ID | Regla |
|---|---|
| RN-06 | Cada barbero podrá consultar y administrar únicamente su propia agenda. |
| RN-14 | El administrador podrá consultar las agendas de todos los barberos. |
| RN-15 | Los usuarios deberán autenticarse para acceder a las agendas privadas. |
| RN-16 | Cada barbero podrá registrar reservaciones manuales únicamente en su propia agenda. |
| RN-17 | Las reservaciones manuales válidas se confirmarán inmediatamente, sin verificación por correo. |
| RN-18 | Las reservaciones manuales y públicas compartirán las mismas restricciones de disponibilidad. |
| RN-19 | El administrador podrá consultar, reprogramar y cancelar reservaciones de cualquier barbero. |
| RN-20 | El administrador podrá crear y eliminar bloqueos en cualquier agenda. |
| RN-21 | Al reprogramar una cita, el nuevo horario deberá cumplir las reglas de disponibilidad. Si no es válido, se conservará la reservación original. |
| RN-22 | Al cancelar una cita, su horario dejará de estar ocupado por esa reservación, salvo que exista otra restricción. |

### 4.3 Administración general

| ID | Regla |
|---|---|
| RN-23 | Cada barbero podrá modificar únicamente sus propios horarios habituales de trabajo. |
| RN-24 | El administrador podrá modificar los horarios habituales de cualquier barbero. |
| RN-25 | Solamente el administrador podrá gestionar el catálogo de servicios y la información administrativa de los barberos. |
| RN-26 | Los horarios de trabajo deberán utilizarse para calcular la disponibilidad de nuevas reservaciones. |

## 5. Decisiones pendientes

### RN-27 — Modificación de horarios con citas existentes

Se deberá definir el comportamiento cuando un cambio en el horario habitual de un barbero entre en conflicto con reservaciones previamente confirmadas.

**Propuesta:** rechazar el cambio hasta que las reservaciones afectadas sean reprogramadas o canceladas.

Esta regla todavía no está aprobada.

## 6. Trazabilidad

Los identificadores RF, RNF y RN permitirán relacionar los requisitos con los casos de uso, la implementación y las pruebas automatizadas.

Por ejemplo:

- **RF-03:** permitir solicitar una reservación.
- **RN-13:** impedir conflictos entre reservaciones y retenciones activas.
- **RNF-05:** garantizar la integridad ante solicitudes simultáneas.

Estos requisitos se implementarán y comprobarán progresivamente durante el desarrollo del backend.