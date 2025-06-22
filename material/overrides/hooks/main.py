# Fichero: material/overrides/hooks/main.py

from mkdocs.utils import get_markdown_title
import markdown as md_lib

# Almacenamos la instancia de Markdown globalmente para no recrearla.
_md = None

def on_config(config):
    """
    Inicializa una instancia de Markdown al principio del todo, 
    usando la misma configuración que usará MkDocs.
    """
    global _md
    # Crea una instancia de Markdown con las extensiones definidas en mkdocs.yml
    _md = md_lib.Markdown(
        extensions=config.get('markdown_extensions', []),
        extension_configs=config.get('mdx_configs', {})
    )
    return config

def on_env(env, config, files):
    """
    Inyecta la instancia de Markdown previamente creada en el entorno de Jinja2
    como un filtro llamado 'markdown'.
    """
    global _md
    if _md:
        env.filters['markdown'] = _md.convert
    return env

def on_page_markdown(markdown, page, config, files):
    """
    Reemplaza marcadores como ::pages con una lista de archivos.
    """
    import os

    # Si no hay '::pages' en la página, no hacemos nada
    if '::pages' not in markdown:
        return markdown

    # Obtenemos la ruta del directorio de la página actual
    page_dir = os.path.dirname(page.file.src_path)

    # Generamos la lista de enlaces
    links = []
    for file in sorted(os.listdir(os.path.join(config['docs_dir'], page_dir))):
        if file.endswith('.md') and file != 'index.md':
            # Obtenemos el título de la página del 'frontmatter' si existe
            title = file.replace('.md', '') # Título por defecto

            # Enlace en formato Markdown
            links.append(f"- [{title}]({file})")

    # Unimos los enlaces en una lista de Markdown
    link_list = "\n".join(links)

    # Reemplazamos '::pages' con nuestra lista generada
    return markdown.replace('::pages', link_list)
