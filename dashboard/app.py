import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client, Client

st.set_page_config(page_title="Second Serve | Dashboard", page_icon="🍲", layout="wide")
st.title("🍲 Second Serve - Live Impact & Verification")

# Connect to Supabase
load_dotenv()
supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# Fetch Data
@st.cache_data(ttl=5)
def get_data():
    response = supabase.table("food_listings").select("*").execute()
    return pd.DataFrame(response.data)

df = get_data()

if df.empty:
    st.warning("No donations logged yet.")
else:
    # Metrics
    completed_df = df[df['status'] == 'completed']
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Food Rescued (kg)", completed_df['quantity_kg'].sum() if not completed_df.empty else 0)
    col2.metric("Active Listings", len(df[df['status'] == 'available']))
    col3.metric("Verified Distributions", len(completed_df[completed_df['proof_photo_url'].notna()]))
    
    st.divider()
    
    # Display Feed
    st.subheader("Live Operations Board")
    display_df = df[['food_type', 'quantity_kg', 'location', 'status', 'volunteer_name', 'donor_rating', 'volunteer_rating']].copy()
    st.dataframe(display_df, use_container_width=True, hide_index=True)