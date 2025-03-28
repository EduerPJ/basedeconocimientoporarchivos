"""Tests for Supabase client."""
import os
from unittest.mock import patch, MagicMock

import pytest
from supabase import Client

# We're importing the module, not the variable, to avoid initializing the client during tests
import supabase_client


@pytest.fixture
def mock_env_vars():
    """Set mock environment variables for testing."""
    with patch.dict(os.environ, {"SUPABASE_URL": "https://test.supabase.co", "SUPABASE_KEY": "test_key"}):
        yield


@pytest.fixture
def mock_create_client():
    """Mock the create_client function."""
    with patch("supabase_client.create_client") as mock:
        mock_client = MagicMock(spec=Client)
        mock.return_value = mock_client
        yield mock, mock_client


def test_supabase_client_initialization(mock_env_vars, mock_create_client):
    """Test that Supabase client is initialized with correct parameters."""
    mock_create, _ = mock_create_client
    
    # Re-import to trigger the initialization with our mocks
    import importlib
    importlib.reload(supabase_client)
    
    # Check that create_client was called with correct args
    mock_create.assert_called_once()
    args, kwargs = mock_create.call_args
    assert args[0] == "https://test.supabase.co"
    assert args[1] == "test_key"
    assert kwargs["options"].postgrest_client_timeout == 10
    assert kwargs["options"].storage_client_timeout == 10
    assert kwargs["options"].schema == "public"