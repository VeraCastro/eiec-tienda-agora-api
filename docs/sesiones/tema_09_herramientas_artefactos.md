# Sesión Tema 9: Herramientas DevOps, artefactos y repositorios

## Objetivo

Comprender el ecosistema DevOps y publicar artefactos generados por el pipeline.

## Enfoque práctico

- GitHub Container Registry.
- Docker image como artefacto.
- GitHub Release como Plan B.
- Comparación con Nexus, CircleCI y Bitbucket.

## Cambios previstos

```text
Dockerfile
docker-compose.yml
.github/workflows/package.yml
```

## Ruta Plan B sin AWS

```text
GitHub Actions → Docker build → GitHub Container Registry
```

## Actividad estudiante

Identificar:

- Commit SHA.
- Tag de imagen.
- Workflow que generó el artefacto.
