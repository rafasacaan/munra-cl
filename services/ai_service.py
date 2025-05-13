from anthropic import AsyncAnthropic
#from pydantic_ai import Agent
#from pydantic_ai.models.anthropic import AnthropicModel
#from pydantic_ai.providers.anthropic import Anthropic
import config
from typing import Optional, List, Dict, Any

class AIService:
    """Service for interacting with AI models via Anthropic."""

    def __init__(
        self, 
        model_name: Optional[str] = None
    ):
        """
        Initialize the AI service.

        Args:
            model_name: Name of the model to use, defaults to config.DEFAULT_MODEL
        """
        
        # Initialize LLM
        self.model_name = model_name or config.DEFAULT_MODEL
        self.client = AsyncAnthropic(
            api_key=config.ANTHROPIC_API_KEY,
        )

        # Initialize the Pydantic AI agent
        #self.model = AnthropicModel(model_name=self.model_name, provider=self.client)
        #self.agent = Agent(self.model)


    async def chat_completion(
        self,
        user_message: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7
    ) -> str:
        """
        Get a chat completion from the AI model.

        Args:
            user_message: The user's message/query
            system_prompt: Optional system instructions
            temperature: Controls randomness (0.0-1.0)

        Returns:
            The AI's response as a string
        """
        # Call the Anthropic API directly for more control
        response = await self.client.messages.create(
            model=self.model_name,
            max_tokens=1024,
            messages=[{"role": "user", "content": user_message}],
            system=system_prompt,
            temperature=temperature,
        )

        # Extract and return the response text
        return response.content[0].text


    async def structured_completion(
        self,
        user_message: str,
        output_schema: Any,
        system_prompt: Optional[str] = None
    ) -> Any:
        """
        Get a structured completion using Pydantic AI.

        Args:
            user_message: The user's message/query
            output_schema: Pydantic model defining the output structure
            system_prompt: Optional system instructions

        Returns:
            An instance of the output_schema Pydantic model
        """
        # Create a prompt dictionary
        prompt = {"query": user_message}

        # Set system prompt if provided
        if system_prompt:
            self.agent.system_prompt = system_prompt

        # Get structured response using Pydantic AI
        result = await self.agent.run(
            input=prompt,
            output_schema=output_schema
        )

        return result