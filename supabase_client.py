"""Supabase client module for database interactions."""

import os

from dotenv import load_dotenv
from supabase import Client, create_client
from supabase.client import ClientOptions

# Load environment variables
load_dotenv()

# Supabase client setup
url: str = os.environ.get("SUPABASE_URL") or ""
key: str = os.environ.get("SUPABASE_KEY") or ""

# Only create the client if the URL and key are provided
supabase: Client | None = None
if url and key:
    supabase = create_client(
        url,
        key,
        options=ClientOptions(
            postgrest_client_timeout=10,
            storage_client_timeout=10,
            schema="public",
        ),
    )
