# games.py
import streamlit as st
import json
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

@st.cache_resource
def get_db():
    db = firestore.client()
    return db

def post_game(db, seasonID, date, location, team1, team2):
    full_datetime = datetime.combine(date, datetime.min.time())
    payload = {
        'seasonID': seasonID,
        'date': full_datetime,
        'location': location,
        'team1': team1,
        'team2': team2
    }
    doc_ref = db.collection("games").document()
    doc_ref.set(payload)
    return

def display_games():
    st.title("Game Updater")
    db = get_db()

    with st.form(key="game_form"):
        seasonID = st.text_input("Season ID")
        date = st.date_input("Date")
        location = st.text_input("Location")
        team1 = st.text_input("Team 1 ID")
        team2 = st.text_input("Team 2 ID")

        if st.form_submit_button("Submit Game"):
            post_game(db, seasonID, date, location, team1, team2)
            st.success("Game details saved successfully!")

