# Sesión Tema 5: Pruebas en Tienda Ágora API

## Objetivo

Conectar el concepto de pruebas automatizadas con un proyecto de tienda en línea. El estudiante debe comprender cómo las pruebas unitarias y de API protegen el comportamiento del sistema antes de avanzar en el pipeline.

## Contexto dentro del proyecto

A partir del Tema 5, el repo `eiec-tienda-agora-api` reemplaza al repo del Tema 4 como columna vertebral práctica.

La API inicial ya contiene:

```text
GET /health
GET /version
GET /products
GET /products/{product_id}
```

## Conceptos a trabajar

- Pruebas unitarias.
- Pruebas de API.
- Smoke test.
- Contrato básico de API.
- Pull Request como punto de revisión.
- Pipeline como verificador automático.

## Ramas demo sugeridas

```text
demo/t5-api-verde
demo/t5-api-roja
```

### Rama verde

Cambio correcto: agregar una prueba que valida un producto existente o un producto inexistente.

### Rama roja

Cambio defectuoso: romper el contrato del endpoint `/products`, por ejemplo cambiar `price` por `amount`.

## Guion práctico resumido

1. Mostrar el repo `eiec-tienda-agora-api`.
2. Mostrar pipeline inicial verde.
3. Explicar estructura:
   - `app/main.py`
   - `app/products.py`
   - `tests/test_products_unit.py`
   - `tests/test_products_api.py`
4. Abrir PR verde.
5. Revisar Actions.
6. Abrir PR rojo.
7. Leer log fallido.
8. Preguntar qué rompió el contrato.
9. Pedir a estudiantes crear una prueba nueva en rama `feature/nombre-apellido`.

## Actividad estudiante

Agregar una prueba para validar que un producto inexistente devuelve `404`.

Rama:

```text
feature/t5-nombre-apellido
```

Pasos:

```bash
git checkout main
git pull origin main
git checkout -b feature/t5-nombre-apellido
python -m pytest -q
```

Agregar o modificar prueba en:

```text
tests/test_products_api.py
```

Subir:

```bash
git add .
git commit -m "Agrega prueba para producto inexistente"
git push -u origin feature/t5-nombre-apellido
```

Abrir Pull Request hacia `main`.

## Entregable

- Enlace al Pull Request.
- Captura del pipeline.
- Una frase: ¿qué protegió la prueba?

## Plan B

Si GitHub Actions tarda, usar una ejecución previa.

Si no pueden clonar, pueden revisar los archivos desde GitHub y crear PR desde la interfaz web.

Si el entorno local falla, el estudiante puede hacer el cambio en GitHub web, pero debe interpretar el resultado del pipeline.

## Cierre conceptual

> Una prueba no es un adorno. Es una cerradura automática que protege el contrato del sistema.
