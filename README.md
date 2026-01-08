#  -- FinalModulo2_SantiagoCastro --
## SISTEMA DE GESTIÓN DE TRANSPORTE SEGURO S.A.
---

## AUTORÍA Y SELLO PERSONAL
Este código es una implementación de planificación y desarrollo diseñad por **Santiago Castro**. Incluye un **Decorador de Autoría** único (`@firma_santiago`) que audita cada proceso crítico del sistema en tiempo real.

```text
    _____             _   _                 
   / ____|           | | (_)                
  | (___   __ _ _ __ | |_ _  __ _  __ _  ___  
   \___ \ / _` | '_ \| __| |/ _` |/ _` |/ _ \ 
   ____) | (_| | | | | |_| | (_| | (_| | (_) |
  |_____/ \__,_|_| |_|\__|_|\__,_|\__, |\___/ 
                                   |___/
```

>### "Escribe código, cambia el mundo"
> — *Santiago Castro*

# DESCRIPCIÓN
**Este proyecto es una solución integral para la digitalización de la flota de vehículos y conductores de la empresa Transporte Seguro S.A. Implementa un modelo robusto de Programación Orientada a Objetos (POO) en Python, garantizando la seguridad operativa mediante reglas de negocio automatizadas.**

# Conceptos Aplicados:
- Abstracción: Estructura base mediante ABC (Abstract Base Classes).

- Herencia: Modelado especializado de flota (Moto, Carro, Camion).

- Polimorfismo: Validaciones de seguridad diferenciadas según el tipo de unidad.

- Composición: El Motor nace y muere con el Vehiculo.

- Agregación: Relación dinámica con el Conductor.


## REGLAS DE SEGURIDAD Y SEGURIDAD
```text
| Vehículo | Protocolo de Validación | Requisito Crítico |
| :---: | :--- | :--- | :--- |
| **MOTO** | Verificación de Casco de Seguridad | **Obligatorio** para iniciar jornada. |
| **CARRO** | Análisis de Revisión Técnico-Mecánica | **Vigencia** comprobada vs Fecha Actual. |
| **CAMIÓN** | Auditoría de Planilla de Carga | **Estado Legal** y documentación activa. |
```
---
