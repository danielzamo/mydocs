---
title: Sugerencias de config.
---

## Configuración edición de Markdown

### Limpieza de código

- Crea/modifica `.vscode/settings.json` en tu proyecto:

```json
{
  "editor.trimAutoWhitespace": true,
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "editor.renderWhitespace": "none",
  "python.linting.pylintArgs": [
    "--disable=W0611,C0114,C0116"
  ],
  "[markdown]": {
    "editor.quickSuggestions": false,
    "editor.autoClosingBrackets": false,
    "editor.formatOnSave": true
  }
}
```

## Desactivación de extensiones y/o personalizando warning

!!! info "Para desactivar extensiones problemáticas (o no)"

    Abre la paleta de comandos (`Ctrl+Shift+P`)

    - Ejecuta Extensions: `Show Enabled Extensions`
    - Busca y deshabilita extensiones como:
        - Trailing Spaces (si la tienes)
        - Cualquier linter de Markdown que esté siendo agresivo

!!! info "Prevenir warning... ejemplo el `MD047` (trailing newline)"

    Añade esto en `.markdownlint.json`:

    ```json
    {
      "MD047": false
    }
    ```
