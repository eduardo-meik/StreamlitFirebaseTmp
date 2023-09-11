import streamlit as st
from google.cloud import firestore

# Establish a connection to Firestore
db = firestore.Client()

def display_users():
    # Query to list all users
    users_ref = db.collection('Users')
    
    for user in users_ref.stream():
        st.write(user.to_dict())

# ... more functions for your Streamlit pages
