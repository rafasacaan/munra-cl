from fasthtml.common import *
from models.database import RecGenerationResponse
import config

def invoca_una_idea():
    """
    Defines the home page content.

    Returns:
        Components representing the home page content
    """
    return Div(
        Div(
            #<-- Column Left -->
            Div(
                Img(
                    src="/assets/rayos-left.png", 
                    alt="", 
                    cls=""
                ),
                cls="bg-white p-6 rounded-lg"
            ),
            #<--/ Column Left -->
            
            #<-- Column Center -->
            Div(
                # Generator form
                Div(
                    # Header
                    H1("invoca una idea", cls="text-3xl font-bold text-gray-800 mb-6"),
                    
                    # Formulario
                    Form(
                        # Topic field
                        Div(
                            Label("Qué estás pensando ahora?", For="topic",
                                cls="block text-gray-700 mb-2"),
                            Textarea(
                                id="topic",
                                name="topic",
                                placeholder="Describe tu idea con detalles para mejores obtener mejores resultados...",
                                rows=3,
                                required=True,
                                cls="w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-500"
                            ),
                            cls="mb-4"
                        ),

                        # Ritual selection
                        Div(
                            Label("Escoge tu ritual:", For="ritual", cls="block text-gray-700 mb-2"),
                            Select(
                                Option("Restricciones", value="Restricciones", selected=True),
                                Option("Sensorial", value="Sensorial"),
                                Option("Narrativo", value="Narrativo"),
                                id="ritual",
                                name="ritual",
                                cls="w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-500"
                            ),
                            cls="mb-4"
                        ),

                        # Instrumento selection
                        Div(
                            Label("Escoge un canal:", For="instrumento", cls="block text-gray-700 mb-2"),
                            Select(
                                Option("Ambiental", value="Ambiental", selected=True),
                                Option("Cuerdas", value="Cuerdas"),
                                Option("Teclado", value="Teclado"),
                                Option("Rítmico", value="Rítmico"),
                                id="instrumento",
                                name="instrumento",
                                cls="w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-500"
                            ),
                            cls="mb-4"
                        ),

        
                        # Submit button with loading state
                        Div(
                            Button(
                                Span("Invoca a munra", id="button-text"),
                                Span(
                                    Span(cls="animate-spin inline-block w-4 h-4 border-2 border-white border-t-transparent rounded-full ml-2"),
                                    id="loading-spinner",
                                    cls="hidden"
                                ),
                                type="submit",
                                id="submit-button",
                                cls="bg-gray-800 hover:bg-gray-900 text-white py-2 px-4 rounded flex items-center justify-center"
                            ),
                            Script("""
                            document.addEventListener('DOMContentLoaded', function() {
                                const form = document.querySelector('form');
                                const submitButton = document.getElementById('submit-button');
                                const buttonText = document.getElementById('button-text');
                                const loadingSpinner = document.getElementById('loading-spinner');
                                
                                form.addEventListener('submit', function() {
                                    // Disable the button
                                    submitButton.disabled = true;
                                    submitButton.classList.add('opacity-75');
                                    
                                    // Show loading spinner
                                    loadingSpinner.classList.remove('hidden');
                                    
                                    // Change button text
                                    buttonText.textContent = 'Generating...';
                                });
                            });
                            """),
                            cls="mb-0"
                        ),

                        action="/invoca-una-idea/generate",
                        method="post",
                        cls="bg-white p-6 rounded-lg shadow-md mb-8"
                    ),

                    # Tips section
                    Div(
                        H3("Tips para comunicarte con munra", cls="text-white text-xl font-semibold mb-2"),
                        Ul(
                            Li("Especifica un tempo y un mood", cls="mb-1"),
                            Li("Imagina para quien podría estar dedicado", cls="mb-1"),
                            Li("Menciona aspectos claves que quieres que sean considerados", cls="mb-1"),
                            Li("Entrégate a los lugares donde munra te pueda llevar", cls="mb-1"),
                            cls="list-disc pl-5 text-white"
                        ),
                        cls="bg-gray-900 p-4 rounded-lg mt-6"
                    ),

                    cls="max-w-2xl mx-auto"
                ),
            ),
            #<--/ Column center -->
            
            #<-- Column right -->
            Div(
                Img(
                    src="/assets/rayos-right.png", 
                    alt="", 
                    cls=""
                ),
                cls="bg-white p-6 rounded-lg"
            ),
            #<--/ Column right -->
            cls="grid grid-cols-3 md:grid-cols-3"
        ),
        cls="py-8"
    )


def invoca_una_idea_output(
    topic: str, 
    ritual: str, 
    instrumento: str, 
    rec_response: RecGenerationResponse,
    ):
    """
    Defines the receta outputs page.

    Args:
        topic: The topic that was entered
        ritual: The ritual that was selected
        instrumento: The instrumento that was selected
        receta_response: TitleGenerationResponse containing the list of generated recetas

    Returns:
        Components representing the outputs page
    """
    # Extract titles from the response
    #recs = rec_response.recs

    return Div(rec_response)
    
    # # Create list items for each title
    # rec_items = []

    # for i, rec in enumerate(recs):
    #     rec_items.append(
    #         Li(
    #             Div(
    #                 P(rec, cls="font-medium"),
    #                 Button(
    #                     "Copy",
    #                     type="button",
    #                     onclick=f"navigator.clipboard.writeText(`{rec}`); this.textContent = 'Copied!'; setTimeout(() => this.textContent = 'Copy', 2000);",
    #                     cls="ml-auto text-sm bg-gray-200 hover:bg-gray-300 px-2 py-1 rounded"
    #                 ),
    #                 cls="flex justify-between items-center"
    #             ),
    #             cls="p-3 border-b last:border-b-0"
    #         )
    #     )

    # return Div(
    #     # Page header
    #     H1("Generated recetas", cls="text-3xl font-bold text-gray-800 mb-6"),

    #     # Results container
    #     Div(
    #         # Query summary
    #         Div(
    #             H2("Your Request", cls="text-xl font-semibold mb-2"),
    #             P(
    #                 Strong("Idea: "), Span(topic), Br(),
    #                 Strong("Ritual: "), Span(ritual), Br(),
    #                 Strong("Instrumento: "), Span(instrumento),
    #                 cls="text-gray-600 mb-4"
    #             ),
    #             cls="mb-6"
    #         ),

    #         # Titles list
    #         Div(
    #             H2("Title Options", cls="text-xl font-semibold mb-2"),
    #             P("Click 'Copy' to copy any title to your clipboard.", cls="text-gray-600 mb-3"),
    #             Ul(
    #                 *rec_items,
    #                 cls="border rounded divide-y"
    #             ),
    #             cls="mb-6"
    #         ),

    #         # Action buttons
    #         Div(
    #             A("Generate More",
    #               href="/invoca-uns-idea",
    #               cls="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-3"),
    #             A("Back to Home",
    #               href="/",
    #               cls="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded"),
    #             cls="flex"
    #         ),

    #         cls="bg-white p-6 rounded-lg shadow-md mb-8 max-w-2xl mx-auto"
    #     )
    # )