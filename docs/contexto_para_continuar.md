# Contexto para continuar el diseño del curso

Estoy diseñando el curso **Entornos de Integración y Entrega Continua**.

## Datos clave

- El curso dura 17 semanas.
- Inició la semana del 20 de abril.
- Concluye la semana del 10 de agosto.
- Me asignaron el curso la semana del 4 de mayo.
- En esa semana impartí dos sesiones.
- En adelante, mis sesiones síncronas serán los jueves a las 20:00 h.
- No todas las semanas hay sesión interactiva.

## Repositorios

### eiec-tema4-pipeline

Repositorio para la sesión del Tema 4.

Uso:

- Pipeline base.
- GitHub Actions.
- Rama `main` estable.
- Rama `demo/pipeline-verde`.
- Rama `demo/pipeline-rojo`.
- Pull Requests.
- Lectura de logs.

### eiec-tienda-agora-api

Repositorio nuevo para el resto del curso.

Uso:

- Proyecto transversal.
- API de tienda en línea.
- Stack inicial: Python, FastAPI, pytest, httpx, flake8, GitHub Actions.
- Evolucionará con Docker, artefactos, despliegue, rollback y observabilidad.

## Proyecto transversal

Nombre: **Tienda Ágora API**

Idea:

Una API mínima de tienda en línea que servirá como columna vertebral para practicar CI/CD durante el curso.

Endpoints iniciales:

```text
GET /health
GET /version
GET /products
GET /products/{product_id}
```

## Plan A

Usar AWS si el convenio institucional lo permite.

Ruta:

```text
GitHub Actions → pruebas → Docker → AWS → smoke test
```

## Plan B

Si AWS no está disponible:

```text
GitHub Actions → pruebas → Docker → GitHub Container Registry → Docker Compose/local → smoke test
```

## Calendario futuro

| Semana | Tema |
|---|---|
| Semana 18 mayo | Tema 5 |
| Semana 01 junio | Tema 6 |
| Semana 08 junio | Tema 6, 6.6 en adelante |
| Semana 15 junio | Tema 7 |
| Semana 29 junio | Tema 8 continuación |
| Semana 06 julio | Tema 9 |
| Semana 13 julio | Tema 9, 9.5 en adelante |
| Semana 27 julio | Tema 10 continuación |
| Semana 03 agosto | Repaso |

## Próximo trabajo

Preparar la sesión de Tema 5:

- Pruebas unitarias.
- Pruebas de API.
- Ramas demo `demo/t5-api-verde` y `demo/t5-api-roja`.
- Actividad de estudiantes mediante Pull Request.
- Conectar la API con el cliente web/mobile como consumidor de contrato.
