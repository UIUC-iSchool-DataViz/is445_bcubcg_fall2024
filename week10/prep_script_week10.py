###############################################
#  1. Intro to Streamlit -- Text & Layouts
###############################################
# Start off in PL!  Open up the "ungraded VSCode" space and make the "inclass" notebook

# For Streamlit apps, we'll need to write our apps in .py files, not notebook files like we've been doing so far.
# For this, we'll be using VSCode to do this.
# (Note: there is technically a jupyterlab wrapper for Streamlit, but its just been 
#    developed so we won't be using it for this class.)

# Let's start with running a very simple streamlit app:
import streamlit as st

st.title('This is my fancy app!')

# after this point, things will be a little different if you are on PL or running the code locally on your computer
# I'll be running locally usually, but let's look at PL first:

# INSTRUCTIONS FOR RUNNING ON PL:
# 1. Open a "Terminal" by: View --> Terminal OR just the "Terminal" through the hamburger menu
# 2. run in terminal with: "streamlit run <the app .py file>"
# 3. click the "Open in Browser" link that pops up OR click on "Ports" and copy the URL
# 4. Open a Simple Browser with View --> Command Palette --> Simple Browser: Show
# 5. use the URL from prior steps as intput into this simple browser

### 1.1 Text in Streamlit ###
# Let's look at a few more ways to include text in our Streamlit apps.
# We usually start our app with a title (like what we had above).
# We can also have headers and subheaders.
# See: https://docs.streamlit.io/develop/api-reference/text 

st.header('This is a "header"')
st.subheader('This is a "subheader"')

# On the docs there are several other ways to use text (like LaTeX and Markdown),
#  but we'll usually just be using the plain text:
st.text("This is plain text.")

# You can also use "magic" commands like:
'This is also plain text!!'

# ... but we will be using the "write" command typically for consistency:
st.write('This is also some text.')
# You should do whatever makes sense to you!

### 1.2 Layout elements ###
st.subheader('Layouts')
# There are several different ways we can layout our text/charts.
# See: https://docs.streamlit.io/develop/api-reference/layout 

col1, col2 = st.columns(2)
col1.write('This is me adding in some text to column 1')
col2.write('This is me adding in some text to column 2')

# Note that in theory we can have multiple columns, but in practice 
#  the columns will "wrap" after a certain number by default.

# There is a lot of fun stuff here to play with in layouts! 
# For our purposes, we'll start off with some of the simple defaults.

### 1.3 Images ###
st.subheader('Images')
# We can include images with a URL:
st.image('https://i.redd.it/on-a-scale-of-1-10-how-derpy-is-she-v0-z8gtdwu5n5zb1.jpg?width=3024&format=pjpg&auto=webp&s=345e7e1d5b45f20c733e497a9f746f4cbd3a61da',
         width=400,
         caption='A thinly veiled excuse to include a derpy corgi.')

st.write('We can also include images from data:')

import numpy as np
img_data = np.random.random((200,400))
st.image(img_data, caption='Some randomly generated data with NumPy.')



###############################################
#  2. Vega-lite in Streamlit (might skip in class)
###############################################

st.header('Vega-lite in Streamlit')

# While we'll be focusing on making Altair-based plots in Streamlit, if vega-lite is your jam,
# you can absolutely make vega-lite based plots with "st.vega_lite_chart": 
# https://docs.streamlit.io/develop/api-reference/charts/st.vega_lite_chart
# st.vega_lite_chart(data=None, spec=None, *, use_container_width=False, 
#    theme="streamlit", key=None, on_select="ignore", selection_mode=None, **kwargs)

# Example 1: from the st.vega_lite_chart docs -- you can pass data from Python + the vega-lite specification
import pandas as pd

chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

st.vega_lite_chart(
   chart_data,
   {
       "mark": {"type": "circle", "tooltip": True},
       "encoding": {
           "x": {"field": "a", "type": "quantitative"},
           "y": {"field": "b", "type": "quantitative"},
           "size": {"field": "c", "type": "quantitative"},
           "color": {"field": "c", "type": "quantitative"},
       },
   },
)

# Example 2: From our prior Altair work, we can also pass linked data through the specification.
#  This example is from when we built our dashboard:
spec = {
  # Data
  "data": {"url":"https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv"},
  # Mark
  "mark": "bar",
  # Encoding
  "encoding":{
    "x":{"field":"Mobility", "type":"quantitative", "bin":True, "axis":{"title":"Mobility Score"}},
    "y":{"aggregate":"count","type":"quantitative", "axis":{"title":"Mobility Score Distribution"}}
  }
}

st.vega_lite_chart(spec=spec)

###############################################
#  3. JavaScript in Streamlit (not covered)
###############################################

# We also won't cover JavaScript, but it is also possible to use JavaScript in Streamlit.
# Here are some resources to play around with this on your own if you are interested:
# https://discuss.streamlit.io/t/how-to-embed-javascript-into-streamlit/20152/3
# https://discuss.streamlit.io/t/how-to-run-a-javascript-code-in-streamlit/51556

# We won't be covering this in this class however.

###############################################
#  4. Altair in Streamlit
###############################################

st.header('Altair in Streamlit')

# We will spend most of our focus will be on using Altair to 
#  make charts, but we'll circle back to look at more complex 
#  things in the next few weeks as well.

import altair as alt

# Let's recall a plot that we made with Altair in Jupyterlab:
#    Make sure we copy the URL as well!
mobility_url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'


scatters = alt.Chart(mobility_url).mark_point().encode(
    x='Mobility:Q', # "Q for quantiative"
    #y='Population:Q',
    y=alt.Y('Population:Q', scale=alt.Scale(type='log')),
    color=alt.Color('Income:Q', scale=alt.Scale(scheme='sinebow'),bin=alt.Bin(maxbins=5))
)
scatters # note we can use the "magic" display here

st.write('We can also use some of the layout elements to enhance our plot instead of just using the "magic" function:')

col1,col2 = st.columns([0.7, 0.25]) # note we can give the relative size of the columns 
# vertical alignment should work!
#col1,col2 = st.columns([0.7, 0.25],vertical_alignment=['top','top']) # note we can give the relative size of the columns 
col1.altair_chart(scatters, theme="streamlit", use_container_width=True)
col2.write("Here is some text that I can write on the side of my plot.")
col2.image('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/589addc9-2a52-4635-a179-a31739ef8d8d/dex09mu-7f3926cb-46d6-4550-ac4e-13e4a5cff53f.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzU4OWFkZGM5LTJhNTItNDYzNS1hMTc5LWEzMTczOWVmOGQ4ZFwvZGV4MDltdS03ZjM5MjZjYi00NmQ2LTQ1NTAtYWM0ZS0xM2U0YTVjZmY1M2YuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.CcWUljPFORIshWxosDjUpl_D5nh00NpBA3Nku1DyXPY',
           width=200, caption='We can also include images/other elements in columns.')


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