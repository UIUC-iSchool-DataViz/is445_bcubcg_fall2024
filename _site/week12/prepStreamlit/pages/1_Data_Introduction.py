import streamlit as st

st.set_page_config(page_title="Introduction to Data", page_icon=":1234:") # not sure what this adds?
st.sidebar.header("Introduction to Data")

st.title('Info about our Dataset')
mobility_url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'

st.write("Here is where we could give some background about our dataset.")
st.write("This would be a good place to include links, references, and images.")

import pandas as pd
df = pd.read_csv(mobility_url)

# There are a few ways to show the dataframe if we want our viewer to see the table:
#df
st.write(df)