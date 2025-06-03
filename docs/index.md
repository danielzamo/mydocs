# Bienvenido al sitio

Este sitio es de documentación personal, aquí se comparten algunos artículos de TI. Inicialmente se publica los que el autor esta utilizando para ciertas certificaciones que intenta pronto rendir.

!!! note "Generación del este sitio"
    Este sitio esta generado con SSG MkDocs, utilizando el theme Material, y publicado en dominio de GitHub, utilizando Git Page + Git Action.

## Despliegue inicial de MkDocs

=== "Entorno virtual Python"

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

=== "Instalación mkdocs-material"

    ```bash
    pip install mkdocs-material
    # El siguiente comando es ejecutarlo en este momento opcional
    pip freeze | grep -E 'mkdocs|mkdocs-material|markdown' > requirements.txt
    ```

=== "Verificación simple/inicial"

    ```bash
    mkdocs serve
    ```

## MkDocs - commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## MkDocs - project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

:books: -- :beers:
