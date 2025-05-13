from fasthtml.common import *
import config

def contacto():
    """
    Defines the home page content.

    Returns:
        Components representing the home page content
    """
    return Div(
        #H1("Contacto", cls="text-3xl font-bold text-gray-800 mb-6"),
        "hola, mi nombre es rafa",
        Br(),
        "me puedes escribir a",
        Br(),
        P("rafasacaan at gmail", cls="text-green-400")
    )