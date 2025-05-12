from fasthtml.common import *
import config

def invoca_una_idea():
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
                    "Invoca una idea",
                    cls="text-gray-600"
                ),
                cls="bg-white p-6 rounded-lg"
            ),
            cls="grid grid-cols-1 md:grid-cols-2 gap-6"
        ),
        cls="py-8"
    )