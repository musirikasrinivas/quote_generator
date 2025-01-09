from anthropic import Anthropic
import random
import os
from typing import Optional, List

class QuoteGenerator:
    def __init__(self, api_key=None):
        """
        Initialize the QuoteGenerator with Anthropic API credentials.
        
        Args:
            api_key (str): Anthropic API key. If not provided, will look for ANTHROPIC_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("API key must be provided or set as ANTHROPIC_API_KEY environment variable")
        
        self.client = Anthropic(api_key=self.api_key)
        self.themes = ["inspirational", "motivational", "life", "success", "happiness"]
        
        # Using the latest Claude model
        self.model = "claude-3-sonnet-20240229"

    def generate_quote(self, theme: Optional[str] = None) -> str:
        """
        Generate a quote based on the given theme using Claude API.

        Args:
            theme (str, optional): Theme for the quote. If None, a random theme will be chosen.

        Returns:
            str: Generated quote

        Raises:
            Exception: If there's an error generating the quote
        """
        if not theme:
            theme = random.choice(self.themes)

        # Add variety to prompts
        prompts = [
            f"Create an original, inspiring quote about {theme}.",
            f"Write a unique and thoughtful quote related to {theme}.",
            f"Generate a fresh perspective in a quote about {theme}.",
            f"Compose a meaningful quote that explores {theme}.",
            f"Create a profound statement about {theme}."
        ]

        system_prompt = """You are a creative quote generator. Each time you're asked, 
        generate a completely unique and original quote. Never repeat previous quotes. 
        Return only the quote text without attribution or additional context."""

        message = random.choice(prompts)

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=50,
                temperature=0.9,  # Increased temperature for more randomness
                system=system_prompt,
                messages=[
                    {"role": "user", "content": message}
                ]
            )

            return response.content[0].text.strip()

        except Exception as e:
            raise Exception(f"Error generating quote: {str(e)}")

    def add_theme(self, theme):
        """
        Add a new theme to the available themes list.
        
        Args:
            theme (str): New theme to add
        """
        if theme not in self.themes:
            self.themes.append(theme)

    def remove_theme(self, theme):
        """
        Remove a theme from the available themes list.
        
        Args:
            theme (str): Theme to remove
        """
        if theme in self.themes:
            self.themes.remove(theme)

    def list_themes(self):
        """
        Get the list of available themes.
        
        Returns:
            list: List of available themes
        """
        return self.themes