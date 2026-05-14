# Plan B: continuidad sin AWS

Este plan permite mantener el aprendizaje aunque AWS no esté disponible.

## Ruta principal

```text
GitHub Actions
→ pruebas
→ build Docker
→ GitHub Container Registry
→ Docker Compose local
→ smoke test
```

## Alternativas

- GitHub Release con artefacto ZIP.
- Render, Railway o Fly.io si la institución lo autoriza.
- Ejecución local en máquina docente con Docker Compose.

## Principio didáctico

AWS es un destino posible de despliegue. El concepto central es construir, probar, empaquetar, publicar y validar un artefacto trazable.
