import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import requests


st.set_page_config(layout='wide',initial_sidebar_state="collapsed")

# Add a logo in the top left corner
logo_url = "https://png.pngtree.com/png-vector/20240204/ourmid/pngtree-cute-cartoon-beer-mug-png-file-png-image_11604961.png"
st.logo(logo_url, size="large")

# Custom HTML for logo and title
html_header = f"""
    <div style="display: flex; align-items: center; justify-content: center;">
        <img src="{logo_url}" alt="Logo" style="width: 100px; margin-right: 20px;">
        <h1 style="flex-grow: 1; text-align: center;">Shame of Thrones</h1>
    </div>
"""
st.markdown(html_header, unsafe_allow_html=True)


def home():
    st.title('Home')


def data():
    st.title('Data Overview')

def analysis():
    st.title('Analysis')

def team():    
    # Placeholder images (replace these with actual image paths or URLs)
    placeholder_image = "https://www.freshbooks.com/wp-content/uploads/2021/10/what-is-teamwork.jpg"

    # Team members' data
    team = [
        {"name": "Charlie Shirazi", "title": "Team Lead",  "image": placeholder_image},
        {"name": "Patrick Sweeney", "title": "Data Analyst",  "image": placeholder_image},
        {"name": "Tom Rush", "title": "Design Lead", "image": placeholder_image},
        {"name": "Herman Hesby", "title": "Organizer", "image": placeholder_image},
        {"name": "Christian Agreda", "title": "Model Developer/Test Subject/Groupie",  "image": placeholder_image},
    ]

    # Create columns for team members
    st.title("Meet the Team")
    st.write("### Get to know the people behind the magic!")

    cols = st.columns(len(team))

    for col, member in zip(cols, team):
        with col:
            # Display team member image
            image = Image.open(requests.get(member["image"], stream=True).raw)
            st.image(image, use_container_width=True)

            # Display team member details
            st.subheader(f"**{member['name']}**", divider="red")
            st.write(member["title"])

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
                    "--hover-color": "#6fa3f7",
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
