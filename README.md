# OpenAI Basic Chatbot

## Overview
This is a simple Python script that interacts with OpenAI's GPT-3.5 Turbo model to generate responses based on user input. It prompts the user for input, sends it to OpenAI's API, and returns the generated response.

## Features
- Utilizes OpenAI's `gpt-3.5-turbo` model for text generation.
- Interactive command-line interface.
- Simple and easy-to-use implementation.

## Prerequisites
Before running the script, ensure you have the following:
- Python 3.x installed
- An OpenAI API key
- `openai` Python package installed

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```
2. Install the required dependencies:
   ```sh
   pip install openai
   ```

## Usage
1. Replace the placeholder `openai.api_key` with your actual OpenAI API key.
2. Run the script:
   ```sh
   python script.py
   ```
3. Enter your prompt when prompted.
4. The script will return the AI-generated response.

## Security Notice
🚨 **DO NOT** expose your OpenAI API key in public repositories! To keep your API key secure:
- Use environment variables instead of hardcoding it in the script.
- Store the API key in a `.env` file and load it using `python-dotenv`.
- Use GitHub Secrets if deploying on GitHub.

Example of loading the API key from an environment variable:
```python
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
```

## Contributing
Feel free to submit issues or pull requests if you find ways to improve this script.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
This script is for educational and experimental purposes only. Ensure compliance with OpenAI's usage policies when deploying AI-powered applications.

