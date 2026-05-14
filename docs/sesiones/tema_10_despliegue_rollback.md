# Sesión Tema 10: Despliegue, feature flags y rollback

## Objetivo

Distinguir entre desplegar software y activar funcionalidad.

## Enfoque práctico

- Feature flags.
- Version endpoint.
- Healthcheck.
- Simulación de blue/green.
- Simulación de canary.
- Rollback.

## Cambios previstos

```text
app/feature_flags.py
docs/modelos_despliegue.md
docs/rollback.md
```

## Plan A

Despliegue en AWS si está disponible.

## Plan B

Docker Compose local o GitHub Container Registry.

## Mensaje clave

> El despliegue lleva código a un entorno. La liberación decide cuándo una funcionalidad queda visible.
