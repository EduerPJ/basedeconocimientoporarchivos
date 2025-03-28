import os
import re
from typing import Dict, List, Optional

# File type regex patterns
DOCUMENT_PATTERN = r"^(application\/pdf|application\/vnd\.google-apps\.document|application\/vnd\.openxmlformats-officedocument\.wordprocessingml\.document|text\/plain|application\/msword)$"
SPREADSHEET_PATTERN = r"^(application\/vnd\.google-apps\.spreadsheet|application\/vnd\.openxmlformats-officedocument\.spreadsheetml\.sheet|application\/vnd\.ms-excel)$"
IMAGE_PATTERN = r"^(image\/.*)$"

def main():
    """Main application entry point."""
    print("OpenAI-powered knowledge bank initialized.")

if __name__ == "__main__":
    main()