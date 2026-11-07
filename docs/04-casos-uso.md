# 04. Casos de uso — Barber Studio API

## 1. Introducción

Este documento describe los principales casos de uso del MVP de Barber Studio API, identificando los actores, las operaciones y las reglas que intervienen en cada proceso.

Los casos de uso servirán como referencia para desarrollar los endpoints, la lógica de negocio y las pruebas automatizadas.

## 2. Actores del sistema

| Actor | Descripción |
|---|---|
| Cliente | Persona que consulta disponibilidad y solicita una reservación pública sin iniciar sesión. |
| Barbero | Usuario autenticado que administra su propia agenda, horarios y reservaciones. |
| Administrador | Usuario autenticado con permisos para gestionar la información de la barbería y las agendas de todos los barberos. |

## 3. CU-01 — Consultar disponibilidad

**Actor principal:** Cliente.

**Objetivo:** Consultar los horarios disponibles de un barbero para un servicio y fecha determinados.

**Precondiciones:**
- El barbero y el servicio deben estar disponibles para nuevas reservaciones.
- El sistema debe contar con los horarios de trabajo correspondientes.

**Flujo principal:**
1. El cliente consulta el catálogo de barberos y servicios.
2. Selecciona un barbero, un servicio y una fecha.
3. El sistema obtiene el horario habitual y los bloqueos del barbero.
4. El sistema consulta las reservaciones confirmadas y las retenciones temporales activas.
5. Calcula los horarios disponibles considerando la duración del servicio.
6. Devuelve las opciones disponibles.

**Flujos alternativos:**
- Si no existen horarios disponibles, el sistema devuelve una lista vacía.
- Si los datos son inválidos, devuelve un error de validación.

**Requisitos relacionados:** RF-01, RF-02, RN-02, RN-08, RN-13, RN-26 y RNF-03.

## 4. CU-02 — Solicitar y confirmar reservación pública

**Actor principal:** Cliente.

**Objetivo:** Reservar un horario mediante verificación por correo electrónico.

**Precondiciones:**
- El barbero y el servicio deben estar disponibles.
- El horario solicitado debe cumplir las reglas de disponibilidad.

**Flujo principal:**
1. El cliente selecciona barbero, servicio, fecha y horario.
2. Proporciona su correo electrónico.
3. El sistema valida los datos y comprueba la disponibilidad.
4. Crea una reservación pendiente y retiene temporal