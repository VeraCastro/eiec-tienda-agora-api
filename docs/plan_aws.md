# Plan A: despliegue con AWS

Este plan se activará si el convenio institucional permite acceso suficiente a AWS.

## Preguntas pendientes

- ¿El acceso será por AWS Academy Learner Lab, AWS Educate, créditos o cuenta institucional?
- ¿Qué servicios estarán habilitados?
- ¿Habrá cuentas individuales para estudiantes?
- ¿Se podrá conectar GitHub Actions con AWS?
- ¿Se permitirán IAM roles, OIDC o solo credenciales temporales?
- ¿Qué límites de gasto, región y duración aplican?
- ¿Quién apagará recursos persistentes?

## Ruta sugerida

```text
GitHub Actions
→ pruebas
→ build Docker
→ push a ECR o GHCR
→ despliegue en App Runner / ECS / EC2
→ smoke test
```

## Servicios candidatos

- AWS App Runner: recomendado si está disponible por simplicidad.
- EC2: útil para una práctica controlada y visible.
- ECS Fargate: más profesional, pero requiere más configuración.
- CloudWatch: logs y observabilidad básica.
