import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu


st.set_page_config(layout='wide',initial_sidebar_state="collapsed")


def home():
    st.title('Home')


def data():
    st.title('Data Overview')

def analysis():
    st.title('Analysis')

def team():
    st.title('Meet the Team')

    st.write('Charlie: Leader')
    st.write('Herman: Organizer')
    st.write('Tom: Design Lead')
    st.write('Patrick: Data Analyst')
    st.write('Christian: Model Developer/Test Subject/Groupie')

    st.image('shame-game-of-thrones.gif')


st.balloons()


def streamlit_menu():
    selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Data Overview", "Analysis", "Meet the Team"],  # required
            icons=["house", "database", "bar-chart", "people"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#727372"},
                "icon": {"color": "orange", "font-size": "30px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#58a6f5",
                },
                "nav-link-selected": {"background-color": "#045fba"},
            },
        )
    return selected

selected = streamlit_menu()

if selected == "Home":
    home()
if selected == "Data Overview":
    data()
if selected == "Analysis":
    analysis()
if selected == "Meet the Team":
    team()
