from fasthtml.common import *
import config

def footer():
    """
    Creates a consistent footer.
    """
    return Footer(
        Div(
            P(f"© {config.APP_NAME} 2025   |   Creado por rafasacaan",
              cls="text-center text-gray-500"),
            cls="container mx-auto px-4 py-6"
        ),
        cls="bg-white mt-auto"
    )