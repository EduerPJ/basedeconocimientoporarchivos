"""Tests for Supabase client."""

import os
from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pytest
from supabase import Client

# We're importing the module, not the variable, to avoid initializing the client
# during tests
import supabase_client


@pytest.fixture
def mock_env_vars() -> Generator[None, None, None]:
    """Set mock environment variables for testing."""
    with patch.dict(
        os.environ,
        {
            "SUPABASE_URL": "https://test.supabase.co",
            "SUPABASE_KEY": (
                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
                "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRlc3QiLCJyb2xlIjoiYW5vbiIsImlh"
                "dCI6MTYxNjk2OTgyMSwiZXhwIjoxOTMyNTQ1ODIxfQ.j-fQOygAhigZ9_nGiPA7"
                "JgQRCcLPXZPIHAToH7VfKp0"
            ),
        },
    ):
        yield


@pytest.fixture
def mock_create_client() -> Generator[tuple[MagicMock, MagicMock], None, None]:
    """Mock the create_client function."""
    # Use 'supabase' instead of 'supabase_client' because we're importing from
    # supabase module
    with patch("supabase.create_client") as mock:
        mock_client = MagicMock(spec=Client)
        mock.return_value = mock_client
        yield mock, mock_client


def test_supabase_client_initialization(
    mock_env_vars: Generator[None, None, None],
    mock_create_client: tuple[MagicMock, MagicMock],
) -> None:
    """Test that Supabase client is initialized with correct parameters."""
    mock_create, _ = mock_create_client

    # Re-import to trigger the initialization with our mocks
    import importlib

    importlib.reload(supabase_client)

    # Check that create_client was called with correct args
    mock_create.assert_called_once()
    args, kwargs = mock_create.call_args
    assert args[0] == "https://test.supabase.co"
    assert args[1] == (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRlc3QiLCJyb2xlIjoiYW5vbiIsImlh"
        "dCI6MTYxNjk2OTgyMSwiZXhwIjoxOTMyNTQ1ODIxfQ.j-fQOygAhigZ9_nGiPA7"
        "JgQRCcLPXZPIHAToH7VfKp0"
    )
    assert kwargs["options"].postgrest_client_timeout == 10
    assert kwargs["options"].storage_client_timeout == 10
    assert kwargs["options"].schema == "public"
