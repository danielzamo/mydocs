# Estructura recomendada para mydocs (en Mkdocs + theme Material)

## 1. Estructura de directorios final

```
mydocs/
├── docs/                           # Contenido markdown
├── my_theme/                       # ← Cambiar nombre (más genérico)
│   ├── partials/                   # Material theme específico
│   │   ├── announce.html
│   │   ├── header.html
│   │   └── footer.html
│   ├── assets/
│   │   ├── stylesheets/
│   │   │   └── custom.css
│   │   └── javascripts/
│   │       └── custom.js
│   ├── 404.html                    # Páginas de error personalizadas
│   ├── base.html                   # Template base (si necesitas override completo)
│   └── main.html                   # Template principal para blocks
├── mkdocs.yml
└── requirements.txt
```

## 2. Configuración en mkdocs.yml

```yaml
theme:
  name: material
  custom_dir: my_theme              # ← Directorio raíz de customización
  features:
    - announce.dismiss
    # otras features...
```

## 3. Buenas prácticas recomendadas

### Usar nombres descriptivos para directorios
- `my_theme/` en lugar de `my_material/overrides/`
- `customizations/` o `theme_overrides/` son también opciones válidas

### Organización por tipo de customización
- `partials/` - Para componentes específicos del tema Material
- `assets/` - Para CSS, JS, imágenes, fonts
- Templates directos (404.html, base.html) en la raíz del custom_dir

### Seguir la estructura del tema padre
Los contenidos del custom_dir deben reflejar la estructura del directorio del tema padre. Para Material theme, esto significa usar `partials/` para componentes modulares.

## 4. Cómo migrar tu estructura actual

### Paso 1: Reorganizar directorios
```bash
# Crear nueva estructura
mkdir -p my_theme/partials
mkdir -p my_theme/assets/stylesheets
mkdir -p my_theme/assets/javascripts

# Mover archivo actual
mv my_material/overrides/partials/announce.html my_theme/partials/announce.html

# Mover assets si los tienes
mv my_material/assets/* my_theme/assets/
```

### Paso 2: Actualizar mkdocs.yml
```yaml
theme:
  name: material
  custom_dir: my_theme  # ← Cambiar aquí
```

### Paso 3: Limpiar estructura antigua
```bash
# Opcional: remover directorio antiguo
rm -rf my_material/
```

## 5. Ventajas de esta estructura

- **Claridad**: Separación clara entre customizaciones y tema base
- **Mantenibilidad**: Fácil de entender y mantener
- **Escalabilidad**: Permite agregar más customizaciones organizadamente
- **Estándar**: Sigue las convenciones tanto de MkDocs como de Material theme

## 6. Próximos pasos

1. Implementar la nueva estructura
2. Probar que tu `announce.html` funciona correctamente
3. Agregar más customizaciones según necesites:
   - CSS personalizado en `assets/stylesheets/`
   - JavaScript personalizado en `assets/javascripts/`
   - Otros partials de Material theme