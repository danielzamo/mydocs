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
