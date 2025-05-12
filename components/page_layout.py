from fasthtml.common import *
from .header import header
from .footer import footer

def page_layout(title, content, current_page="/"):
    """
    Creates a consistent page layout with header and footer.

    Args:
        title: The page title
        content: The main content components
        current_page: The current page path

    Returns:
        A complete HTML page
    """
    return Html(
        Head(
            Title(title),
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
     
            # Include Tailwind CSS for styling
            Script(src="https://cdn.tailwindcss.com"),
     
            # Add additional CSS for loading animations
            Style("""
                @keyframes spin {
                    to { transform: rotate(360deg); }
                }
                .animate-spin {
                    animation: spin 1s linear infinite;
                }
            """),
        ),
        Body(
            Div(
                header(current_page),
                Main(
                    Div(
                        content,
                        cls="container mx-auto px-4 py-8"
                    ),
                    cls="flex-grow"
                ),
                footer(),
                cls="flex flex-col min-h-screen"
            )
        )
    )