from fasthtml.common import *
import time
import config

from components.page_layout import page_layout
from pages.home import home as home_page
from pages.invoca_una_idea import invoca_una_idea as invoca_una_idea_page
from pages.invoca_una_idea import invoca_una_idea_output as invoca_una_idea_output_page
from pages.historia import historia as historia_page
from pages.registros import registros as registros_page
from pages.contacto import contacto as contacto_page

#from models.database import RecGenerationRequest
from models.db import create_db_and_tables,  get_session
from models.database import RecGenerationRequest
from tools.rec_generator import RecGenerator
from services.db_service import DBService

# Initialize the FastHTML app
app = FastHTML()  # Creates the application instance
rt = app.route    # Creates a convinience shortcut to the route method

# Set up static files manually
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")

# Initialize database - will use existing DB or create new one
create_db_and_tables()

# Initialize AI services
rec_generator = RecGenerator()


# Render pages
@rt("/")
def get():
    """
    Handler for the home page route.
    """
    return page_layout(
        title=f"{config.APP_NAME}",
        content=home_page(),
        current_page="/"
    )

@rt("/invoca-una-idea")
def get():
    """
    Handler for the home page route.
    """
    return page_layout(
        title=f"{config.APP_NAME}",
        content=invoca_una_idea_page(),
        current_page="/invoca-una-idea"
    )

@rt("/historia")
def get():
    """
    Handler for the home page route.
    """
    # Create a database session
    session = get_session()
    db_service = DBService(session)

    # Get recent generations
    generations = db_service.get_recent_generations(limit=20)
    
    return page_layout(
        title=f"{config.APP_NAME}",
        content=historia_page(generations),
        current_page="/historia"
    )

@rt("/contacto")
def get():
    """
    Handler for the home page route.
    """
    return page_layout(
        title=f"{config.APP_NAME}",
        content=contacto_page(),
        current_page="/contacto"
    )

@rt("/invoca-una-idea/generate")
async def post(
    topic: str, 
    ritual: str, 
    instrumento: str):
    """
    Handler for processing receta generation requests.

    Args:
        topic: The content topic
        ritual: The ritual type eg. restrictivo, narrativo, sensorial
        instrumento: teclado, cuerdas, ambiental, rítmico
    """
    # Create a database session
    session = get_session()
    db_service = DBService(session)
    
    try:
        # Validate inputs
        if not topic:
            error_message = Div(
                H1("Error", cls="text-3xl font-bold text-red-600 mb-4"),
                P("Por favor ingresa una idea.", cls="mb-4"),
                A(
                    "Intenta de nuevo", href="/invoca-una-idea",
                    cls="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                ),
                cls="max-w-2xl mx-auto bg-white p-6 rounded-lg shadow-md"
            )

            return page_layout(
                title=f"Error - {config.APP_NAME}",
                content=error_message,
                current_page="/invoca-una-idea"
            )

        # Create request object
        request = RecGenerationRequest(
            topic=topic,
            ritual=ritual,
            instrumento=instrumento,
        )
        
        # Record start time for performance tracking
        start_time = time.time()
        
        # Generate titles
        rec_response = await rec_generator.generate_recs(request=request)
        
        # We're not collecting IP addresses in this implementation
        ip_address = None
        
        # Record the generation in the database
        await db_service.record_rec_generation(
            request=request,
            response=rec_response,
            start_time=start_time,
            ip_address=ip_address
        )

        # Return the results page
        return page_layout(
            title=f"Generated recs - {config.APP_NAME}",
            content=invoca_una_idea_output_page(
                topic=topic,
                ritual=ritual,
                instrumento=instrumento,
                rec_response=rec_response,
            ),
            current_page="/invoca-una-idea"
        )
    except Exception as e:
        # Handle errors
        error_message = Div(
            H1("Error", cls="text-3xl font-bold text-red-600 mb-4"),
            P(f"An error occurred while generating recs: {str(e)}", cls="mb-4"),
            A("Try Again", href="/invoca-una-idea",
              cls="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"),
            cls="max-w-2xl mx-auto bg-white p-6 rounded-lg shadow-md"
        )

        return page_layout(
            title=f"Error - {config.APP_NAME}",
            content=error_message,
            current_page="/invoca-una-idea"
        )



# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)