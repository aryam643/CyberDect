import streamlit as st
from PIL import Image
from ctypes import alignment
from urllib import response
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import pandas as pd
import numpy as np
import re
import string
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, WordNetLemmatizer
from functions import *
import pickle
import streamlit as st
from PIL import Image

# Page title and styling
st.markdown(
    """
    <style>
    .header {
        display: flex;
        align-items: center;
        padding-bottom: 20px;
        border-bottom: 1px solid #ccc;
        margin-bottom: 30px;
        
    }
    .header h1 {
        font-size: 36px;
        font-weight: bold;
        color: white;
        margin: 0;
    }

    .container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 0 20px;
    }

    .section {
        margin-bottom: 30px;
    }

    .section h2 {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }

    .section p {
        font-size: 18px;
        color: #555;
        margin-bottom: 20px;
    }

    .tweet-input {
        height: 150px;
        padding: 10px;
        font-size: 18px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    .prediction-image {
        width: 100%;
        max-width: 600px;
        height: auto;
        margin-top: 20px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

image = Image.open('images/logo.png')

st.markdown(
    """
    <div class="header">
        <h1>CyberDect (Cyberbullying Tweet Recognition App)</h1>
    </div>
    """.format(image),
    unsafe_allow_html=True
)

# Description
st.markdown(
    """
    <div class="container">
        <div class="section">
            <h2>Description</h2>
            <p>
            This app predicts the nature of a tweet into 6 categories:
            </p>
            <ul>
                <li>Age</li>
                <li>Ethnicity</li>
                <li>Gender</li>
                <li>Religion</li>
                <li>Other Cyberbullying</li>
                <li>Not Cyberbullying</li>
            </ul>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Text Box
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<h2>Enter Tweet</h2>", unsafe_allow_html=True)
tweet_input = st.text_area("Tweet Input", height=150, key="tweet_input", value="")

st.markdown("</div>", unsafe_allow_html=True)

# Entered Tweet text
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<h2>Entered Tweet Text</h2>", unsafe_allow_html=True)
if tweet_input:
    st.markdown("<p>{}</p>".format(tweet_input), unsafe_allow_html=True)
else:
    st.markdown("<p>No Tweet Text Entered!</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
# Prediction
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<h2>Prediction</h2>", unsafe_allow_html=True)
if tweet_input:
    prediction = custom_input_prediction(tweet_input)
    if prediction == "Age":
        st.image("images/age_cyberbullying.png", use_column_width=True, caption="Age Cyberbullying")
    elif prediction == "Ethnicity":
        st.image("images/ethnicity_cyberbullying.png", use_column_width=True, caption="Ethnicity Cyberbullying")
    elif prediction == "Gender":
        st.image("images/gender_cyberbullying.png", use_column_width=True, caption="Gender Cyberbullying")
    elif prediction == "Not Cyberbullying":
        st.image("images/not_cyberbullying.png", use_column_width=True, caption="Not Cyberbullying")
    elif prediction == "Other Cyberbullying":
        st.image("images/other_cyberbullying.png", use_column_width=True, caption="Other Cyberbullying")
    elif prediction == "Religion":
        st.image("images/religion_cyberbullying.png", use_column_width=True, caption="Religion Cyberbullying")
else:
    st.markdown("<p>No Tweet Text Entered!</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# About section
expand_bar = st.expander("About")
expand_bar.markdown(
    """
    <div class="container">
        <div class="section">
            <h2>About</h2>
            <p>
            This app was developed to predict the nature of tweets and categorize them into different types of cyberbullying. It uses a machine learning model trained on a dataset of cyberbullying tweets.
            </p>
        </div>
        <div class="section">
            <h2>Dataset</h2>
            <p>
            The dataset used for training the model can be found at: <a href="https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification">https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification</a>
            </p>
        </div>
    </div>
    """
    , unsafe_allow_html=True
)
