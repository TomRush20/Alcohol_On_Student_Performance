import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide',initial_sidebar_state="collapsed")

def intro():
    st.title('Meet the Team')

    st.write('Charlie: Leader')
    st.write('Herman: Organizer')
    st.write('Tom: Design Lead')
    st.write('Patrick: Data Analyst')
    st.write('Christian: Model Developer/Test Subject/Groupie')

    st.image('shame-game-of-thrones.gif')



def data():
    st.title('Data Overview')



st.balloons()

nav = st.navigation([st.Page(intro,title='Meet the Team'), st.Page(data,title='Data Overview')])
nav.run()