


# day 2/3 -- "grab bag" of other things
# multi-page apps? ==> maybe day 2? ==> does this work with HF apps??
# Week 12 --  https://docs.streamlit.io/develop/tutorials/databases <- touch on but say we'll be just doing csv files
# Week 12 -- embedding streamlit spaces on other webpages? wait until Jekyll? https://huggingface.co/docs/hub/en/spaces-sdks-streamlit#embed-streamlit-spaces-on-other-webpages


#######################################################
# 1. Getting setup -- using our HF template
#######################################################

# We have a few options for how to proceed.  I'll start by showing the process in 
#   PL and then I'll move to my local installation of my template so that I can make 
#   sure I am pushing code at various intervals so folks can check that out.

# See the class notes on this with some photos for reference!
# **this has to be implemented!**


###################################################################
# 2. Review of where we got to last time, in template app.py file
###################################################################


# Let's start by copying things we did last time
import streamlit as st
import altair as alt

# Let's recall a plot that we made with Altair in Jupyterlab:
#    Make sure we copy the URL as well!
mobility_url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'

st.title('This is my fancy app for HuggingFace!!')

scatters = alt.Chart(mobility_url).mark_point().encode(
    x='Mobility:Q', # "Q for quantiative"
    #y='Population:Q',
    y=alt.Y('Population:Q', scale=alt.Scale(type='log')),
    color=alt.Color('Income:Q', scale=alt.Scale(scheme='sinebow'),bin=alt.Bin(maxbins=5))
)

st.header('More complex Dashboards')

brush = alt.selection_interval(encodings=['x','y'])

chart1 = alt.Chart(mobility_url).mark_rect().encode(
    alt.X("Student_teacher_ratio:Q", bin=alt.Bin(maxbins=10)),
    alt.Y("State:O"),
    alt.Color("count()")
).properties(
   height=400
).add_params(
        brush
)

chart2 = alt.Chart(mobility_url).mark_bar().encode(
    alt.X("Mobility:Q", bin=True,axis=alt.Axis(title='Mobility Score')),
    alt.Y('count()', axis=alt.Axis(title='Mobility Score Distribution'))
).transform_filter(
    brush
)

chart = (chart1.properties(width=300) | chart2.properties(width=300))

tab1, tab2 = st.tabs(["Mobility interactive", "Scatter plot"])

with tab1:
    st.altair_chart(chart, theme=None, use_container_width=True)
with tab2:
    st.altair_chart(scatters, theme=None, use_container_width=True)


################################################
# 3. Adding features, Pushing to HF
################################################

st.header('Requirements, README file, Pushing to HuggingFace')

### 3.1 Make a plot ###

# Let's say we want to add in some matplotlib plots from some data we read
#  in with Pandas.

import pandas as pd
df = pd.read_csv(mobility_url)

# There are a few ways to show the dataframe if we want our viewer to see the table:
#df
st.write(df)

# Now, let's plot with matplotlib:
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df['Seg_income'].plot(kind='hist', ax=ax)
#plt.show() # but wait! this doesn't work!  

# We need to use the streamlit-specific way of showing matplotlib plots: https://docs.streamlit.io/develop/api-reference/charts/st.pyplot
st.pyplot(fig)

### 3.2 Push these changes to HF -- requirements.txt ###
# In order to push these changes to HF and have things actually show up we need to 
#   add the packages we've added to our requirements.txt file.

# NOTE: for any package you want to use in your app.py file, you must include it in 
#   the requirements.txt file!

### 3.3 Push these changes to HF -- README.md ###

# While we're doing this, let's also take a look at the README.md file!

st.header('Build in HF: README.md & requirements.txt files')

st.markdown('''
title: Prep notebook -- My Streamlit App
            
emoji: 🏢
            
colorFrom: blue
            
colorTo: gray
            
sdk: streamlit
            
sdk_version: 1.36.0
            
app_file: app.py
            
pinned: false
            
license: mit
```
''')

# Some important things to 

################################################
# 4. TODO Quick intro to widgets
################################################

### 4.1 A few widget examples ###

### 4.2 Connecting widgets with plots ###

################################################
# 5. TODO Multi-page apps (?) this might be for next week/extra
################################################
