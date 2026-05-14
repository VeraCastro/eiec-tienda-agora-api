# Sesión Tema 6: Calidad, cobertura y revisión de código

## Objetivo

Evolucionar el pipeline para que no solo ejecute pruebas, sino que también entregue señales de calidad.

## Enfoque práctico

- Análisis estático.
- Cobertura.
- Revisión de Pull Requests.
- Comentarios y aprobación.
- Quality gates iniciales.

## Cambios previstos al repo

```text
.coveragerc
coverage.xml
quality-gate.md
```

Pipeline esperado:

```text
lint → tests → coverage
```

## Ramas demo sugeridas

```text
demo/t6-coverage-verde
demo/t6-coverage-roja
```

## Actividad estudiante

Agregar una función o endpoint pequeño y su prueba asociada, manteniendo cobertura.

## Cierre

> La calidad no aparece al final. Se cultiva en cada commit.
