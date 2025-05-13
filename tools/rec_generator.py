from typing import List, Dict, Any, Optional
from services.ai_service import AIService
from .prompts import user_prompt as prompt
from .prompts import system_prompt as role_prompt
from models.database import RecGenerationRequest, RecGenerationResponse
import re

from .config import TEMPERATURE

class RecGenerator:
    """
    Tool for generating rec for various platforms.
    """

    def __init__(self):
        """
        Initialize the recommender generator tool.
        """
        self.name = "AI Rec Generator"
        self.description = "Generate engaging recipes to make music."
        self.ai_service = AIService()


    async def generate_recs(
        self,
        request: RecGenerationRequest = None,
        topic: str = None,
        ritual: str = "Restricciones",
        instrumento: str = "Ambiental",
    ) -> RecGenerationResponse:
        """
        Generate recs based on the given parameters.

        Args:
            topic: The subject to generate recs about
            ritual: The methodology: recipes, narrative, etc
            instrumentos: Strings, keys, rythmic, etc

        Returns:
            A RecGenerationResponse containing the list of generated recs
        """

        # Use request object if provided, otherwise use individual parameters
        if request is not None:
            topic = request.topic
            ritual = request.ritual
            instrumento = request.instrumento

        elif topic is None:
            raise ValueError("Introduce un tópico o una idea.")

        # Create system prompt
        system_prompt = role_prompt()

        # Create user prompt
        user_prompt = prompt(
            topic, 
            ritual, 
            instrumento
        )
        
        # Get raw response from AI
        raw_response = await self.ai_service.chat_completion(
            user_message=user_prompt,
            system_prompt=system_prompt,
            temperature=TEMPERATURE
        )

        # Process response to extract titles
        #rec = self._extract_rec_from_response(raw_response)

        # Return a TitleGenerationResponse object
        #return RecGenerationResponse(rec=rec)
        return raw_response


    def _extract_rec_from_response(
        self, 
        response: str
    ) -> List[str]:
        """
        Extract rec from the AI response.

        Args:
            response: The raw AI response text

        Returns:
            Extracted rec
        """
        # Remove any markdown or extra formatting
        clean_response = response.strip()

        # Try to extract numbered list items (e.g., "1. Title here")
        numbered_pattern = r"^\s*\d+\.?\s*(.+)$"
        rec = []

        # Process line by line
        for line in clean_response.split('\n'):
            line = line.strip()
            if not line:
                continue

            # Try to match numbered pattern
            match = re.match(numbered_pattern, line)
            if match:
                title = match.group(1).strip()
                if title:
                    titles.append(title)
            elif not line.startswith('#') and len(line) > 15:
                # If not a numbered item but looks like a title
                # (not a heading and reasonably long)
                titles.append(line)

        # If we couldn't extract properly, just split by newlines and take non-empty lines
        if not titles:
            titles = [line.strip() for line in clean_response.split('\n')
                     if line.strip() and len(line.strip()) > 10]

        # Return up to the expected count
        return rec