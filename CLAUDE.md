# Guidelines for Claude Code

## Project Overview
OpenAI-powered knowledge bank using Google Drive files shared via Google Picker with semantic search capabilities.

## IMPORTANT NOTE
Always use `python3` instead of `python` for all commands in this project, as it ensures compatibility with Ubuntu and other systems that maintain separation between Python versions.

## Development Commands
- Run application: `python3 main.py`
- Lint code: `python3 -m flake8 .`
- Type check: `python3 -m mypy .`
- Run tests: `python3 -m pytest`
- Run single test: `python3 -m pytest path/to/test_file.py::test_function_name`

## Code Style Guidelines
- **Formatting**: Use Black with default settings
- **Imports**: Group imports: standard library, third-party, local; sort alphabetically within groups
- **Types**: Use type hints for all function parameters and return values
- **Naming**:
  - Variables/functions: snake_case
  - Classes: PascalCase
  - Constants: UPPER_SNAKE_CASE
- **Documentation**: Docstrings for all modules, classes, functions (Google style)
- **Error Handling**: Use specific exceptions, handle errors at appropriate levels, log errors with context

## Development Workflow
- Create feature branches from main
- Write tests before implementing features
- Ensure all linting and type checks pass before committing