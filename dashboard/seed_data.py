import os
from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import datetime, timedelta

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# New fake data matching your exact requested features
fake_data = [
    {
        "food_type": "Rice and Lentil Curry",
        "quantity_kg": 15.0,
        "cooked_time": (datetime.now() - timedelta(hours=2)).isoformat(),
        "location": "Banjara Hills, Hyderabad",
        "status": "completed",
        "volunteer_name": "Rahul T.",
        "proof_photo_url": "https://example.com/distribution_proof.jpg",
        "donor_rating": 5,
        "volunteer_rating": 4
    },
    {
        "food_type": "20 Veg Biryani Packets",
        "quantity_kg": 8.5,
        "cooked_time": (datetime.now() - timedelta(minutes=45)).isoformat(),
        "location": "Ameerpet, Hyderabad",
        "status": "available",
    }
]

supabase.table("food_listings").insert(fake_data).execute()
print("✅ New feature data successfully added!")