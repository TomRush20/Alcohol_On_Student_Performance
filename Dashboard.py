#import subprocess
# Install a package using pip
#package_name = "streamlit_option_menu"
#subprocess.run(["pip", "install", package_name])


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import requests
import queries


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
    st.header('Student Alcohol Consumption')
    st.write('We decided to explore data related to alcohol consumption by students in secondary school.')
    st.write('This data contains personal information about the student, family information about the student, and educational information about the student.')
    
    st.subheader('Questions')
    st.write('1. Does alcohol consumption affect student performance?')
    st.write('2. Is alcohol consumption a significant predictor of academic success?')
    st.write('3. Does studying less or drinking more have more of an effect on academic performance?')
    st.write('4. What are the common traits among the students who consume alcohol frequently?')
    st.write('5. What influences academic performance the most?')
    st.write('6. Should students abstain from alcohol in order to do better in school?')
    st.write('7. Do students in relationships tend to drink more?')
    st.write('8. How does alcohol consumption vary among genders?')
    st.write('9. Does going out tend to get in the way of studying?')
    st.write('10. Do students who only drink on weekends tend to perform better in school?')


def data():
    st.title('Data Overview')
    

def analysis():
    st.title('Study Time vs Going Out Relationship')
    # Reshape the DataFrame to a long format
    figplt = queries.byGrade.melt(id_vars="Final Grade", var_name="Ranking Type", value_name="Average")

    # Create a grouped bar chart
    fig = px.bar(
        figplt,
        x="Final Grade",
        y="Average",
        color="Ranking Type",
        barmode="group",
        title="Average Study and Party Ranking by Final Grade",
        labels={"final_grade": "Final Grade", "Average": "Average Ranking"}
    )
    st.plotly_chart(fig)


######  Q8  #######
    st.title('How does alcohol consumption vary among genders?')
    #st.dataframe(queries.Q8, hide_index=True)
    Q8_plot = queries.Q8.melt(id_vars="Gender", var_name="Consumption Type", value_name="Average Consumption")
    # Create a bar chart using Plotly Express
    fig = px.bar(
        Q8_plot,
        x="Gender",
        y="Average Consumption",
        color="Consumption Type",
        barmode="group",
        title="Alcohol Consumption by Gender",
        labels={"Gender": "Gender", "Average Consumption": "Average Consumption Ranking (1-5)"}
    )
    st.plotly_chart(fig)


######  Q9  #######



def team():    
    # Placeholder images (replace these with actual image paths or URLs)
    charlie = "https://pbs.twimg.com/profile_images/1308737414622523392/0sp7hZnl_400x400.jpg"
    patrick = "https://media.licdn.com/dms/image/v2/D4E03AQFkZU80mmlO_Q/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1728603648025?e=1738195200&v=beta&t=NF73htQsHJUOPydU0iM3JtYkBcX6QtUqPm7nadJg9Z8"
    herman = "https://media.licdn.com/dms/image/v2/D4D03AQEmix5C_NCUmw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1722878460687?e=1738195200&v=beta&t=Lq3S0aGCQDa1SFfeRE_4nKMQWLfECBRVAkXdBmRZq5w"
    groupie = "https://media.licdn.com/dms/image/v2/D4E03AQH9fAFmyOeKqg/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1689583863282?e=1738195200&v=beta&t=X5TX8UYRiHAyu5OJwHaXTicXj161zI5QKLqS_gmj_C8"
    tom = "https://media.licdn.com/dms/image/v2/D5603AQF1V-lIwfF1cQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1731794459905?e=1738195200&v=beta&t=2qviQU4GF4GclGxVW9GrbnOyBpP8UqzmhK0xnllCxRk"

    # Team members' data
    team = [
        {"name": "Charlie Shirazi", "title": "Team Lead",  "image": charlie},
        {"name": "Patrick Sweeney", "title": "Data Analyst",  "image": patrick},
        {"name": "Tom Rush", "title": "Design Lead", "image": tom},
        {"name": "Herman Hesby", "title": "Organizer", "image": herman},
        {"name": "Christian Agreda", "title": "Model Developer/Test Subject/Groupie",  "image": groupie},
    ]

    # Create columns for team members
    st.title("Meet the Team")
    st.write("### Get to know the people behind the magic!")

    cols = st.columns(len(team))

    for col, member in zip(cols, team):
        with col:
            # Display team member image
            image = Image.open(requests.get(member["image"], stream=True).raw)

            # Set the desired height
            desired_height = 200
            # Calculate the new width to maintain the aspect ratio
            aspect_ratio = image.width / image.height
            new_width = int(desired_height * aspect_ratio)
            # Resize the image
            resized_image = image.resize((new_width, desired_height))

            st.image(resized_image, use_container_width=False)

            # Display team member details
            st.subheader(f"**{member['name']}**", divider="red")
            st.write(member["title"])

    st.image('shame-game-of-thrones.gif')


#st.balloons()


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

print("hello")