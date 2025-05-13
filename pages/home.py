from fasthtml.common import *
import config

def home():
    """
    Defines the home page content.

    Returns:
        Components representing the home page content
    """
    return Div(
        Div(
            # Column Left
            Div(
                Img(
                    src="/assets/munra-logo.png", 
                    alt="munra logo", 
                    cls="w-full h-auto rounded-lg"
                ),
                cls="bg-white p-6 rounded-lg"
            ),
            # Column Right
            Div(
                P(  
                    Br(),
                    "Ideas para empezar a grabar tu musica sin excusas.",
                    Br(),Br(),
                    "Munra te ayudará a ensuciarte las manos entregándote ideas para empezar a grabar tus ritmos paso a paso, dándote un empujón hacia el lado oscuro. Siéntete cómodo en la incomodidad de lo imperfecto, y cree en los resultados cuando las cosas se salen de control.",
                    Br(),Br(),
                    "Lo que importa al final es encontrar algo para decir, y dejar un registro para poder compartir.  ",
                    cls="text-gray-600"
                ),
                cls="bg-white p-6 rounded-lg"
            ),
            cls="grid grid-cols-1 md:grid-cols-2 gap-6"
        ),
        cls="py-8 md:py-52"
    )
