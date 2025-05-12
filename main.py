from fasthtml.common import *
import time
import config

from components.page_layout import page_layout
from pages.home import home as home_page
from pages.invoca_una_idea import invoca_una_idea as invoca_una_idea_page
from pages.registros import registros as registros_page
from pages.contacto import contacto as contacto_page

# Initialize the FastHTML app
app = FastHTML()  # Creates the application instance
rt = app.route    # Creates a convinience shortcut to the route method

# Set up static files manually
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")


# Render pages
@rt("/")
def home():
    """
    Handler for the home page route.
    """
    return page_layout(
        title=f"{config.APP_NAME}",
        content=home_page(),
        current_page="/"
    )

@rt("/invoca-una-idea")
def invoca_una_idea():
    """
    Handler for the home page route.
    """
    return page_layout(
        title=f"{config.APP_NAME}",
        content=invoca_una_idea_page(),
        current_page="/invoca-una-idea"
    )

@rt("/registros")
def registros():
    """
    Handler for the home page route.
    """
    return page_layout(
        title=f"{config.APP_NAME}",
        content=registros_page(),
        current_page="/registros"
    )


@rt("/historia")
def historia():
    """
    Handler for the home page route.
    """
    return page_layout(
        title=f"{config.APP_NAME}",
        content=home_page(),
        current_page="/historia"
    )

@rt("/contacto")
def contacto():
    """
    Handler for the home page route.
    """
    return page_layout(
        title=f"{config.APP_NAME}",
        content=contacto_page(),
        current_page="/contacto"
    )



# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)