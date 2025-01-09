# Claude Quote Generator

A Python library for generating inspirational quotes using the Claude AI API.

## Installation

```bash
pip install quote-gen
```

## Quick Start

```python
from quote_gen import QuoteGenerator

# Initialize with your API key
generator = QuoteGenerator(api_key="your-api-key-here")

# Generate a random quote
quote = generator.generate_quote()
print(quote)

# Generate a quote with a specific theme
quote = generator.generate_quote(theme="success")
print(quote)
```

## Features

- Generate AI-powered quotes using Claude API
- Support for various themes (inspirational, motivational, life, success, happiness)
- Customizable themes
- Environment variable support for API key
- Error handling and retry mechanisms

## Configuration

You can configure the API key in two ways:

1. Pass it directly to the QuoteGenerator:
```python
generator = QuoteGenerator(api_key="your-api-key-here")
```

2. Set it as an environment variable:
```bash
# Linux/MacOS
export ANTHROPIC_API_KEY='your-api-key'

# Windows (Command Prompt)
set ANTHROPIC_API_KEY=your-api-key

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY = "your-api-key"
```

## Advanced Usage

### Managing Themes

```python
# Add a new theme
generator.add_theme("wisdom")

# Remove a theme
generator.remove_theme("happiness")

# List all available themes
themes = generator.list_themes()
print(themes)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.