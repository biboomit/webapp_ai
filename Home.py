import streamlit as st
#import functions
from requests_oauthlib import OAuth2Session
from datetime import datetime, timedelta, date
import smtplib
import numpy as np
from google.cloud import bigquery
from google.oauth2 import service_account
import os
from pandas_gbq import to_gbq
import google.auth
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


st.title("Boomit-One Prompt Analytics")
#uploaded_file = functions.get_data() si quiero pegarle a la base
uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
    prompt = st.text_area("Enter your prompt:")

    # Generate output
    if st.button("Generate"):
        if prompt:
            # call pandas_ai.run(), passing dataframe and prompt
            #with st.spinner("Generating response..."):
            st.write(pandas_ai.run(df, prompt))
        else:
            st.warning("Please enter a prompt.")