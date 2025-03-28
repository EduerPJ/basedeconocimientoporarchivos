"""Main module for OpenAI-powered knowledge bank application."""

# File type regex patterns
DOCUMENT_PATTERN = (
    r"^(application\/pdf|application\/vnd\.google-apps\.document|"
    r"application\/vnd\.openxmlformats-officedocument\.wordprocessingml\.document|"
    r"text\/plain|application\/msword)$"
)
SPREADSHEET_PATTERN = (
    r"^(application\/vnd\.google-apps\.spreadsheet|"
    r"application\/vnd\.openxmlformats-officedocument\.spreadsheetml\.sheet|"
    r"application\/vnd\.ms-excel)$"
)
IMAGE_PATTERN = r"^(image\/.*)$"


def main() -> None:
    """Main application entry point."""
    print("OpenAI-powered knowledge bank initialized.")


if __name__ == "__main__":
    main()
