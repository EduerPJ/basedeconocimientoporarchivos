# OpenAI Knowledge Bank

A knowledge bank system powered by OpenAI using Google Drive files shared via Google Picker with semantic search capabilities.

## Features

- Supabase integration for data storage
- Google Drive file picker integration
- Semantic search using OpenAI embeddings
- Support for various file types (documents, spreadsheets, images)

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
4. Create a `.env` file with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ```
5. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Development

- Run the application: `python3 main.py`
- Run tests: `python3 -m pytest`
- Run linting: `python3 -m ruff check .`
- Run type checks: `python3 -m mypy .`

## License

MIT
