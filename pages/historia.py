from fasthtml.common import *
from models.database import RecGenerationHistory
from typing import List
from datetime import datetime


def format_datetime(dt: datetime) -> str:
    """Format a datetime for display.
    
    Args:
        dt: The datetime to format
        
    Returns:
        Formatted datetime string
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def historia(
    generations: List[RecGenerationHistory]
):
    """
    Defines the rec generation history page.
    
    Args:
        generations: List of RecGenerationHistory records
        
    Returns:
        Components representing the history page
    """
    # Create list items for each generation record
    history_items = []
    
    for record in generations:
        # Create title list
        #rec_items = [Li(rec, cls="ml-4 py-1") for rec in record.rec]
        
        # Format generation time
        generation_time = f"{record.generation_time_ms:.1f}ms" if record.generation_time_ms else "N/A"
        
        # Create history card
        history_items.append(
            Div(
                Div(
                    H3(f"Topic: {record.topic}", cls="text-lg font-semibold mb-1"),
                    P(
                        Span(f"Ritual: {record.ritual}", cls="mr-3"),
                        Span(f"Instrumento: {record.instrumento}", cls="mr-3"),
                        Span(f"Generated: {format_datetime(record.created_at)}"),
                        cls="text-sm text-gray-600 mb-2"
                    ),
                    Div(
                        P("Rec:", cls="font-medium mb-1"),
                        Ul(record.rec, cls="list-decimal mb-3"),
                        cls="mt-2"
                    ),
                    Div(
                        Small(f"Generation time: {generation_time}", cls="text-gray-500"),
                        cls="text-right"
                    ),
                    cls="p-4"
                ),
                cls="bg-white rounded-lg shadow-md mb-4 hover:shadow-lg transition-shadow"
            )
        )
    
    # Empty state if no records
    if not history_items:
        history_items.append(
            Div(
                P("No hay registros aún.", cls="text-center text-gray-500 py-8"),
                cls="bg-white rounded-lg shadow-md"
            )
        )
    
    return Div(
        # Page header
        H1("Registros", cls="text-3xl font-bold text-gray-800 mb-6"),
        
        # Stats summary card (could be expanded with more analytics)
        Div(
            H2("Resumen", cls="text-xl font-semibold mb-2"),
            P(f"Total de recetas: {len(generations)}", cls="mb-1"),
            P(f"Recientes: {format_datetime(generations[0].created_at) if generations else 'N/A'}", cls="mb-1"),
            cls="bg-black text-white p-4 rounded-md mb-6"
        ),
        
        # History list
        Div(
            H2("Recientes", cls="text-xl font-semibold mb-4"),
            *history_items,
            cls=""
        ),
        
        # Navigation
        Div(
            A("Invoca una idea",
              href="/invoca-una-idea",
              cls="bg-gray-900 hover:bg-gray-800 text-white py-2 px-4 rounded mr-3"),
            A("Regresa",
              href="/",
              cls="bg-gray-200 hover:bg-gray-300 text-gray-800 py-2 px-4 rounded"),
            cls="mt-6"
        ),
        
        cls="max-w-4xl mx-auto"
    )
