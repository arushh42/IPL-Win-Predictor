import streamlit as st
import pickle
import pandas as pd

# Teams and cities lists
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
         'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai',
          'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur',
          'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

# Load the pre-trained pipeline
pipe = pickle.load(open('pipe2.pkl', 'rb'))

# Streamlit frontend
st.title('IPL Win Predictor')

# User input fields
with st.columns(2):
    batting_team = st.selectbox('Select the batting team', sorted(teams))
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))
    selected_city = st.selectbox('Select host city', sorted(cities))

# Additional input fields
target = st.number_input('Target')
score = st.number_input('Score')
overs = st.number_input('Overs completed')
wickets = st.number_input('Wickets out')

# Prediction button
if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    # Create input dataframe
    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
                             'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets': [wickets],
                             'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})

    # Make prediction
    result = pipe2.predict_proba(input_df)
    win_probability = result[0][1]
    loss_probability = result[0][0]

    # Display results
    st.header(batting_team + " Win Probability: " + str(round(win_probability * 100)) + "%")
    st.header(bowling_team + " Loss Probability: " + str(round(loss_probability * 100)) + "%")
