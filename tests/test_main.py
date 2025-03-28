"""Tests for main module."""
import pytest

from main import main


def test_main(capsys):
    """Test main function execution."""
    main()
    captured = capsys.readouterr()
    assert "OpenAI-powered knowledge bank initialized" in captured.out