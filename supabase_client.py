import os
from supabase import create_client, Client
from supabase.client import ClientOptions
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase client setup
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(
    url, 
    key,
    options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public",
    )
)