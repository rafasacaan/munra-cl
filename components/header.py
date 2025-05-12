from fasthtml.common import *
import config

def header(current_page="/"):
    """
    Creates a consistent header with navigation.

    Args:
        current_page: The current page path

    Returns:
        A Header component with navigation
    """
    nav_items = [
        ("home", "/"),
        ("invoca una idea", "/invoca-una-idea"),
        ("registros", "/registros"),
        ("historia", "/historia"),
        ("contacto", "/contacto"),
    ]

    nav_links = []

    # Subrayar pestaña seleccionada
    for title, path in nav_items:
        is_current = current_page == path
        link_class = "text-black hover:text-gray-300 px-3 py-2"
        if is_current:
            link_class += " line-through"

        nav_links.append(
            Li(
                A(title, href=path, cls=link_class)
            )
        )

    return Header(
        Div(
            A(config.APP_NAME, href="/", cls="text-xl font-bold text-black"),
            Nav(
                Ul(
                    *nav_links,
                    cls="flex space-x-2"
                ),
                cls="ml-auto"
            ),
            cls="container mx-auto flex items-center justify-between px-4 py-12"
        ),
        cls="bg-white"
    )