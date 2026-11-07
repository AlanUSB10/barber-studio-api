# 01. Definición del problema

## 1. Contexto

Barber Studio API es un proyecto de desarrollo backend orientado a mejorar la gestión de reservaciones de una barbería.

El escenario contempla una barbería con dos barberos que tienen horarios de trabajo independientes.

Actualmente, gran parte de las reservaciones se realiza mediante WhatsApp, por lo que los barberos deben revisar mensajes, consultar su disponibilidad y confirmar manualmente cada cita.

## 2. Problemas identificados

El proceso actual presenta las siguientes dificultades:

- **Interrupciones durante el servicio:** los barberos deben atender mensajes mientras trabajan con otros clientes.
- **Gestión manual de horarios:** es necesario comprobar la disponibilidad antes de confirmar cada reservación.
- **Riesgo de conflictos:** pueden producirse errores al registrar citas o asignar horarios.
- **Cancelaciones y ausencias:** los retrasos y las inasistencias generan espacios de trabajo desaprovechados.
- **Dependencia de WhatsApp:** los clientes necesitan comunicarse directamente con el barbero para solicitar una cita.

## 3. Solución propuesta

Desarrollar una API REST que permita gestionar las reservaciones de manera centralizada.

El sistema permitirá que los clientes consulten la disponibilidad y soliciten citas, mientras que los barberos podrán administrar sus agendas y registrar manualmente las reservaciones recibidas por otros medios.

También se contemplará un administrador con permisos para supervisar y gestionar la operación general de la barbería.

## 4. Beneficios esperados

- Facilitar el proceso de reservación para los clientes.
- Reducir el tiempo dedicado a confirmar citas manualmente.
- Evitar reservaciones superpuestas.
- Centralizar la información de las agendas.
- Permitir que cada barbero administre sus horarios.
- Mejorar la organización de las actividades de la barbería.

## 5. Alcance de este documento

Este documento describe el problema que buscamos resolver y la solución general propuesta.

Los requisitos funcionales, las reglas de negocio, los casos de uso y las decisiones técnicas se documentarán por separado.