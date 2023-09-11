#app.py
import streamlit as st
from streamlit_option_menu import option_menu
import firebase_admin
from firebase_admin import credentials
from utils.timeline import display_timeline
from utils.games import display_games
from utils.timeline import display_timeline
from utils.analysis import display_analysis
import requests

# Initialize Firebase SDK
def initialize_firebase():
    key_dict = json.loads(st.secrets["textkey"])
    creds = credentials.Certificate(key_dict)

    if not firebase_admin._apps:
        firebase_admin.initialize_app(creds)
        
# Define main app function
def main():
    initialize_firebase()
    
# Navigation bar Menu
selected = option_menu(
        menu_title=None, # menu title
        options=["Home", "Games","Timeline", "Analysis", 'Settings'], # menu options
        icons=['house', 'chat-right-text','boxes', 'pie-chart', 'gear'], # menu icons
        menu_icon="cast", # menu icon
        default_index=0,  # default selected index
        orientation="horizontal" #sidebar or navigation bar
        )

if selected == "Inicio":
    st.title("Plataforma de Analisis Futbolistico")

elif selected == "Games":
    st.title("Juegos")
    display_games()
    
elif selected == "Timeline":
    st.title("Timeline")
    display_timeline()

elif selected == "Analysis":
    st.title("Analysis")
    display_analysis()
        
elif selected == "Settings":
    st.title("Setting")