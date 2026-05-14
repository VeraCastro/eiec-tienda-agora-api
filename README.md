# EIEC Tienda Ágora API

Proyecto transversal del curso **Entornos de Integración y Entrega Continua**.

Tienda Ágora API será la columna vertebral práctica del curso: una API mínima de tienda en línea que evolucionará por sesiones para trabajar pruebas, pipelines, calidad, artefactos, despliegue, modelos de liberación, rollback y observabilidad.

## Propósito didáctico

Este repositorio permitirá practicar:

- Control de versiones con Git y GitHub.
- Pull Requests como mecanismo de revisión.
- Pruebas automatizadas.
- GitHub Actions como pipeline inicial.
- Calidad de código y cobertura.
- Docker y artefactos.
- Despliegue en AWS, si el convenio institucional lo permite.
- Plan B sin AWS usando GitHub Container Registry y ejecución local.

## Stack inicial

- Python 3.11+
- FastAPI
- pytest
- httpx
- flake8
- GitHub Actions

## Endpoints iniciales

```text
GET /health
GET /version
GET /products
GET /products/{product_id}
```

## Preparación local

```bash
python -m venv .venv
source .venv/Scripts/activate  # Git Bash en Windows
# En macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python -m pytest -q
flake8 app tests
```

## Ejecutar la API localmente

```bash
uvicorn app.main:app --reload
```

Abrir:

```text
http://127.0.0.1:8000/docs
```

## Flujo de trabajo para estudiantes

```bash
git checkout main
git pull origin main
git checkout -b feature/nombre-apellido

# hacer cambios y pruebas

python -m pytest -q
flake8 app tests

git add .
git commit -m "Describe el cambio"
git push -u origin feature/nombre-apellido
```

Luego abrir un Pull Request hacia `main`.

## Ruta del curso

La API crecerá gradualmente:

1. Tema 5: pruebas unitarias y pruebas de API.
2. Tema 6: calidad, cobertura y revisión de código.
3. Tema 7: comparación con Jenkinsfile.
4. Tema 8: comparación con GitLab CI/CD.
5. Tema 9: artefactos y repositorios.
6. Tema 10: despliegue, feature flags y rollback.
7. Repaso: flujo completo de entrega continua.

## Plan A y Plan B

### Plan A: con AWS disponible

```text
GitHub Actions → pruebas → build Docker → despliegue en AWS → smoke test
```

### Plan B: sin AWS disponible

```text
GitHub Actions → pruebas → build Docker → GitHub Container Registry → Docker Compose/local → smoke test
```

AWS será un destino de despliegue, no una dependencia obligatoria del aprendizaje.
