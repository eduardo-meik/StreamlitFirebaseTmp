# timeline.py
import streamlit as st
from firebase_admin import firestore

@st.cache_resource
def get_db():
    db = firestore.client()
    return db

def get_games(db, search_term=""):
    games = db.collection("games").where("location", "==", search_term).stream()
    return games

def post_timeline_event(db, gameID, timeline_data):
    game_ref = db.collection("games").document(gameID)
    game_ref.update({"timeline": timeline_data})

def display_timeline():
    st.title("Timeline Updater")

    db = get_db()

    search_term = st.text_input("Search for a game by location:")
    games = list(get_games(db, search_term))  # Convert to list to avoid iteration issues

    selected_game = st.selectbox("Select a game:", [game.id for game in games])

    with st.form(key="timeline_form"):
        num_events = st.number_input("Number of events", 1, 10, 1)

        timeline_data = []
        for i in range(num_events):
            st.write(f"Event {i+1}")
            minuto = st.number_input(f"Minute (Event {i+1})", 0, 90, 0)
            evento = st.selectbox(f"Event Description (Event {i+1})", ["Faltas", "Goles", "Corners", "Sustitucion Entra", "Sustitucion Sale", "Tiros a Puerta", "Tarjeta Amarilla", "Tarjeta Roja"])
            jugador = st.text_input(f"Player (Event {i+1})")
            equipo = st.text_input(f"Team (Event {i+1})")

            timeline_data.append({
                "minuto": minuto,
                "evento": evento,
                "jugador": jugador,
                "equipo": equipo
            })

        if st.form_submit_button("Submit Timeline"):
            post_timeline_event(db, selected_game, timeline_data)
            st.success("Timeline updated!")
