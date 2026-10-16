import streamlit as st
import pandas as pd
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

st.set_page_config(page_title="Second Serve - Admin", layout="wide")
st.title("Second Serve: Operations & Impact")

if not url or not key:
    st.error("Missing Supabase credentials in .env file.")
    st.stop()

supabase = create_client(url, key)

# Test insert button
if st.button("Insert Test Donation from Local"):
    res = supabase.table("food_listings").insert({
        "food_type": "Pipeline Test Food",
        "quantity_kg": 5.0,
        "cooked_time": "12:00 PM",
        "location": "Local Host Test",
        "status": "available"
    }).execute()
    st.success("Inserted row successfully!")
    st.rerun()

# Fetch & display live rows
data = supabase.table("food_listings").select("*").order("created_at", desc=True).execute().data
if data:
    df = pd.DataFrame(data)
    st.dataframe(df[["food_type", "quantity_kg", "cooked_time", "location", "status", "created_at"]], use_container_width=True)
else:
    st.info("No listings found.")