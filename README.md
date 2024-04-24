# IPL Win Predictor

The IPL Win Predictor is an interactive web application designed to predict the outcomes of Indian Premier League (IPL) cricket matches. Users can input match details and receive real-time predictions on the probabilities of win and loss for the participating teams.

## Features

- **User-Friendly Interface**: Intuitive input fields allow users to specify match conditions, including team selections, host city, target score, current score, overs completed, and wickets out.

- **Real-Time Predictions**: Leveraging machine learning models, the application provides instant predictions on win and loss probabilities based on the input match details.

- **Multiple Models**: The application offers predictions from both Random Forest and Logistic Regression models, providing users with diverse insights into match outcomes.

## Models

### Random Forest Classifier

- The Random Forest Classifier model is trained on historical IPL match data, considering various factors such as batting and bowling teams, host city, target score, current score, overs completed, and wickets out.

### Logistic Regression

- The Logistic Regression model also utilizes historical IPL data to predict match outcomes. It analyzes the same set of factors as the Random Forest model but employs a different algorithm for prediction.

## Technologies Used

- Python
- Streamlit
- scikit-learn
- pandas
