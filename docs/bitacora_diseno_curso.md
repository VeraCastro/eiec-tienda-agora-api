# Bitácora de diseño del curso

## Curso

**Asignatura:** Entornos de Integración y Entrega Continua  
**Programa:** Maestría en Desarrollo y Operaciones de Software  
**Docente:** Dr. Rodolfo Rafael Medina Ramírez  
**Sesiones futuras:** jueves a las 20:00 h  

## Contexto general

El curso tiene una duración de 17 semanas. Inició la semana del 20 de abril y concluye la semana del 10 de agosto.

El docente fue asignado la semana del 4 de mayo. En esa semana impartió dos sesiones. En adelante, las sesiones síncronas serán los jueves a las 20:00 h, pero no todas las semanas tienen sesión interactiva.

## Repositorios del curso

### 1. eiec-tema4-pipeline

Repositorio usado para la sesión del Tema 4.

Propósito:

- Explicar qué es un pipeline.
- Mostrar la fase de commit.
- Usar GitHub Actions.
- Trabajar con ramas demo verde y roja.
- Leer logs de un pipeline fallido.
- Practicar Pull Requests.

Uso principal:

```text
main                 -> estado estable
demo/pipeline-verde  -> cambio correcto, pipeline verde
demo/pipeline-rojo   -> cambio defectuoso, pipeline rojo
feature/*            -> ramas de estudiantes
```

### 2. eiec-tienda-agora-api

Repositorio transversal para el resto del curso.

Propósito:

- Servir como proyecto vertebral desde Tema 5 hasta el repaso final.
- Representar una API de tienda en línea.
- Practicar pruebas, calidad, pipelines, artefactos, despliegue, rollback y observabilidad.
- Mantener una ruta Plan A con AWS y una ruta Plan B sin AWS.

URL esperada:

```text
https://github.com/prof-rodolfo-medina/eiec-tienda-agora-api
```

## Proyecto transversal: Tienda Ágora API

Tienda Ágora API es una API mínima de tienda en línea que evolucionará gradualmente durante el curso.

### Contexto del proyecto

Una organización requiere una tienda en línea con catálogo, carrito, pedidos y un cliente mobile/empresarial consumidor de la API.

El proyecto se usará como laboratorio de CI/CD. No busca desarrollar una tienda completa, sino ofrecer un escenario realista para practicar entrega continua.

### Stack inicial

```text
Python
FastAPI
pytest
httpx
flake8
GitHub Actions
Docker, más adelante
AWS, si el convenio lo permite
GitHub Container Registry, como Plan B
```

### Endpoints iniciales

```text
GET /health
GET /version
GET /products
GET /products/{product_id}
```

## Calendario de sesiones futuras

| Semana | Tema | Enfoque práctico |
|---|---|---|
| Semana 18 mayo | Tema 5 | Pruebas en Tienda Ágora API |
| Semana 01 junio | Tema 6 | Calidad, cobertura y revisión de código |
| Semana 08 junio | Tema 6, 6.6 en adelante | Calidad avanzada y deuda técnica |
| Semana 15 junio | Tema 7 | Pipeline externo / Jenkinsfile |
| Semana 29 junio | Tema 8 continuación | GitLab CI/CD |
| Semana 06 julio | Tema 9 | Ecosistema DevOps |
| Semana 13 julio | Tema 9, 9.5 en adelante | Artefactos y repositorios |
| Semana 27 julio | Tema 10 continuación | Modelos de despliegue, feature flags y rollback |
| Semana 03 agosto | Repaso | Simulación final del flujo completo |

## Plan A: con AWS

AWS se usará si el convenio institucional lo permite.

Ruta tentativa:

```text
GitHub Actions
→ pruebas
→ build Docker
→ push a ECR o GHCR
→ despliegue en AWS App Runner / EC2 / ECS
→ smoke test
```

Preguntas pendientes:

- ¿El convenio habilita AWS Academy Learner Lab, AWS Educate, créditos o una cuenta institucional?
- ¿Qué servicios están permitidos?
- ¿Los estudiantes tendrán cuentas individuales?
- ¿Se puede conectar GitHub Actions con AWS?
- ¿Se permiten IAM roles, OIDC o credenciales temporales?
- ¿Hay límite de gasto, región o duración?
- ¿Quién apagará recursos persistentes?

## Plan B: sin AWS

Si AWS no está disponible, el curso seguirá con:

```text
GitHub Actions
→ pruebas
→ build Docker
→ GitHub Container Registry
→ Docker Compose local o entorno alternativo
→ smoke test
```

Principio didáctico:

> AWS es un destino de despliegue, no la columna vertebral del aprendizaje.

## Decisiones pedagógicas

- El repo del Tema 4 se conserva como laboratorio compacto.
- El repo Tienda Ágora API será la columna vertebral del resto del curso.
- La app mobile empresarial se tratará como consumidor de API, no como proyecto mobile completo.
- El foco se mantiene en CI/CD, calidad, artefactos y despliegue.
- Cada sesión debe dejar una evolución visible en el repositorio.
- Cada práctica debe cerrarse con un Pull Request o evidencia de pipeline.

## Pendientes próximos

- Preparar sesión Tema 5.
- Crear ramas demo del Tema 5.
- Crear milestones y labels en GitHub.
- Confirmar condiciones del convenio AWS.
- Preparar Plan B operativo con Docker/GHCR.
