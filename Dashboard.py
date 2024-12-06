# Uncomment the following lines to install the required packages

#import subprocess
#st_nav = "streamlit_option_menu"
#subprocess.run(["pip", "install", st_nav])
#st_extras = "streamlit_extras"
#subprocess.run(["pip", "install", st_extras])


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu
from streamlit_extras.let_it_rain import rain
from PIL import Image
import requests
import queries


st.set_page_config(layout='wide',initial_sidebar_state="collapsed")

# Add a logo in the top left corner
title_url = 'https://cdn-icons-png.freepik.com/256/2734/2734166.png?semt=ais_hybrid'
logo_url = "https://seeklogo.com/images/W/wake-forest-university-athletic-logo-3CDC546B33-seeklogo.com.png"
st.logo(logo_url, size="large")

# Custom HTML for logo and title
html_header = f"""
    <div style="display: flex; align-items: center; justify-content: center;">
        <img src="{title_url}" alt="Logo" style="width: 100px; margin-right: 20px;">
        <h1 style="flex-grow: 1; text-align: center;">Student Alcohol Consumption</h1>
    </div>
"""
st.markdown(html_header, unsafe_allow_html=True)
st.write('')


def home():
    home_icon = 'https://icons.veryicon.com/png/o/miscellaneous/two-color-webpage-small-icon/home-page-161.png'
    home_header = f"""
        <div style="display: flex; align-items: center; justify-content: center;">
            <img src="{home_icon}" alt="Logo" style="width: 50px; margin-right: 20px;">
            <h1 style="flex-grow: 1; text-align: center;">Home</h1>
        </div>
    """
    st.markdown(home_header, unsafe_allow_html=True)
    st.write('')
    st.write('')

    st.header('Student Alcohol Consumption')
    st.write('Our analysis explores the relationship between alcohol consumption and academic performance. The data consists of personal, family, and educational information about the students.')
    st.write('')
    
    st.subheader('Analysis Questions')
    st.write('1. Does alcohol consumption affect student performance?')
    st.write('2. Is alcohol consumption a significant predictor of academic success?')
    st.write('3. Does study time or alcohol consumption have more of an impact on academic performance?')
    st.write('4. What are the common traits among the students who consume alcohol frequently?')
    st.write('5. What influences academic performance the most?')
    st.write('6. Should students abstain from alcohol in order to do better in school?')
    st.write('7. Do students in relationships tend to drink more?')
    st.write('8. How does alcohol consumption vary among genders?')
    st.write('9. Does going out tend to get in the way of studying?')
    st.write('10. Do students who only drink on weekends tend to perform better in school?')


def data():
    data_icon = 'https://cdn-icons-png.flaticon.com/512/5135/5135755.png'
    data_header = f"""
        <div style="display: flex; align-items: center; justify-content: center;">
            <img src="{data_icon}" alt="Logo" style="width: 50px; margin-right: 20px;">
            <h1 style="flex-grow: 1; text-align: center;">Data Overview</h1>
        </div>
    """
    st.markdown(data_header, unsafe_allow_html=True)
    st.write('')
    st.write('')

    overview_df = pd.DataFrame(queries.overview_sql)
    st.dataframe(overview_df, use_container_width=True)
    st.divider()
    
    st.markdown("### Key Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Records", overview_df.shape[0])
    
    with col2:
        st.metric("Total Features", overview_df.shape[1])
    
    st.divider()

    #Data Dictionary
    st.markdown("### Data Dictionary")
    
    data_df = pd.read_csv('Data_Dictionary.csv')
    attributes = ["All"] + data_df["Attribute"].tolist()
    data_options = st.multiselect("Select Attribute(s)", attributes, default="All")
    if "All" in data_options:
        selected_attribute = data_df
    else:
        selected_attribute = data_df[data_df["Attribute"].isin(data_options)]
    st.dataframe(selected_attribute, use_container_width=True, hide_index=True)

def analysis():
    analysis_icon = 'https://www.iconpacks.net/icons/1/free-analysis-icon-691-thumb.png'
    analysis_header = f"""
        <div style="display: flex; align-items: center; justify-content: center;">
            <img src="{analysis_icon}" alt="Logo" style="width: 50px; margin-right: 20px;">
            <h1 style="flex-grow: 1; text-align: center;">Analysis</h1>
        </div>
    """
    st.markdown(analysis_header, unsafe_allow_html=True)

######  Q1  #######
    with st.expander("Does alcohol consumption affect student performance?"):
        st.title('Does alcohol consumption affect student performance?')
        grade_order = ['A+', 'A', 'B', 'C', 'F']
        question_1 = pd.DataFrame(queries.Q1)
        question_1["Final Grade"] = pd.Categorical(question_1["Final Grade"], categories=grade_order, ordered=True)
        question_1 = question_1.sort_values("Final Grade") 
        Q1_chart = px.line(question_1, x='Final Grade', y='Average Daily Consumption', title='Average Daily Consumption by Final Grade')
        st.plotly_chart(Q1_chart)
        st.caption("The graph shows a clear inverse relationship between daily alcohol consumption and final grade. Alcohol does affect student performance; in a negative way. ")
    
######  Q2  #######
    with st.expander("Is alcohol consumption a significant predictor of academic performance?"):
        st.title('Is alcohol consumption a significant predictor of academic performance?')
        st.subheader('Stepwise Linear Regression Model')
        st.write('After the including the selected features in the model, we added the three "drinking variables" to see how they compared to significant variables.')
        q2_df = pd.read_excel('q2.xlsx')
        st.dataframe(q2_df, hide_index=True)
        st.caption('The only "drinking variable" that was shown to be significant is the Going Out variable. This model would predict that students who go out often tend to do worse on their Final Exam.')

######  Q3  #######
    with st.expander("Does study time or alcohol consumption have more of an impact on academic performance?"):
        st.title('Does study time or alcohol consumption have more of an impact on academic performance?')
        st.write("**REGRESSION MODEL**")
        q3_df = pd.read_excel('Regression Model Data Management.xlsx')
        st.dataframe(q3_df, hide_index=True)
        st.caption("Based on the coefficients, studying less has a bigger effect on academic performance. The bigger coefficient indicates a bigger impact on Final Grade")

######  Q5  #######
    with st.expander("What influences academic performance the most?"):
        st.title('What influences academic performance the most?')
        st.subheader('Coefficients from Full Regression Model')
        q5_df = pd.read_excel('q5.xlsx')
        choice = st.pills('Choose an Option', options=['All']+['Top 5'])
        if choice == 'All':
            st.bar_chart(q5_df, x = 'Variable', y = 'Coefficient', color='Coefficient', horizontal=True)
        if choice == 'Top 5':
            q5_df_5 = q5_df[q5_df['Abs']>=0.6109]
            st.bar_chart(q5_df_5, x = 'Variable', y = 'Coefficient', color='Coefficient', horizontal=True)
        st.caption('Looking at the Top 5 variables in terms of coefficient magnitude, the most important variable was fittingly past failures. If a student has a past history of failing classes, it makes sense that he/she would fail in the current class. An interesting variable that was found to be important was Relationship Status, which was shown to hinder academic performance.')

######  Q6  #######
    with st.expander("Should students abstain from alcohol in order to do better in school?"):
        st.title('Should students abstain from alcohol in order to do better in school?')
        question_6 = pd.DataFrame(queries.Q6)
        Q6_chart = px.bar(question_6, x='Final_Grade', y='Alcohol_Consumption', title='Alcohol Consumption by Final Grade')
        st.plotly_chart(Q6_chart)
        st.caption("Students would do better in school if they abstain from alchol. However, there are a good amount of students who drink and get good grades, so abstaining could be too drastic.")

######  Q7  #######
    with st.expander("Do students in relationships tend to drink more?"):
        st.title('Do students in relationships tend to drink more?')
        q7_df = pd.DataFrame(queries.Q7)
        q7_df["Percent of Total"] = q7_df["Percent of Total"].str.rstrip("%").astype(float)
        # Create the stacked bar chart
        fig = px.bar(
            q7_df,
            x="Workday Alcohol Consumption",
            y="Percent of Total",
            color="Currently Dating",
            text="Percent of Total",
            title="Percent Distribution of Workday Alcohol Consumption by Dating Status",
            labels={
                "Workday Alcohol Consumption": "Workday Alcohol Consumption Level",
                "Percent of Total": "Percent of Total (%)"
            },
            barmode="group"
        )
        # Customize hover information
        fig.update_traces(
            texttemplate='%{text}%',
            hovertemplate=(
                "Workday Alcohol Consumption Level: %{x}<br>"
                "Percent of Total: %{y}%<br>"
                "Currently Dating: %{customdata}"
            ),
            customdata=q7_df["Currently Dating"]
        )
        st.plotly_chart(fig)
        st.caption("From the graph, there is no clear relationship between being in a relationship and drinking habits. The percentage of students in each drinking category is about the same for both groups.")


######  Q8  #######
    with st.expander("How does alcohol consumption vary among genders?"):
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
        st.caption("Males are on average drinking more alcohol than females. Males drink more on workdays and weekends. Males drink about the same during workdays than females do during weekends.")

######  Q9  #######
    with st.expander("Does going out tend to get in the way of studying?"):
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
        
        st.caption("Going out to parties and study time has an inverse relationship. The more parties students go to, the less time they spend studying. Students who do well tend to spend more time styding and less time going to parties. ")


def team():    
    team_icon = 'https://cdn-icons-png.flaticon.com/512/10190/10190563.png'
    team_header = f"""
        <div style="display: flex; align-items: center; justify-content: center;">
            <img src="{team_icon}" alt="Logo" style="width: 50px; margin-right: 20px;">
            <h1 style="flex-grow: 1; text-align: center;">Meet the Team</h1>
        </div>
    """
    st.markdown(team_header, unsafe_allow_html=True)
    st.write('')
    st.write("### Get to know the people behind the magic!")
    st.write('')

    def beer():
        rain(
            emoji="🍺",
            font_size=40,
            falling_speed=2,
            animation_length=1,
        )
    beer()

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

    #st.image('shame-game-of-thrones.gif')

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