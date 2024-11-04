# we will often times use an app.py instead of a workbook so here is just a placeholder for that kind of file as well!
import streamlit as st

st.title('This is my fancy app!')

st.header("This is a header")
st.subheader('This is a subheader')

st.text('This is some text.')


# 1. Layout elements
col1,col2 = st.columns(2)
col1.write('This is thing 1')
col2.write('This is thing 2')

# 2. Images
st.subheader('Images')
st.image('https://i.redd.it/on-a-scale-of-1-10-how-derpy-is-she-v0-z8gtdwu5n5zb1.jpg?width=3024&format=pjpg&auto=webp&s=345e7e1d5b45f20c733e497a9f746f4cbd3a61da',
         width=200,
         caption='A thinly veiled excuse for a cute corg!')


import numpy as np

img_data = np.random.random((200,200))
st.image(img_data, 
         caption='Random numpy data')

st.header('Altair in Streamlit')
import altair as alt

mobility_url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'

scatters = alt.Chart(mobility_url).mark_point().encode(
    x = 'Mobility:Q',
    y=alt.Y('Population:Q', scale=alt.Scale(type='log')),
    color=alt.Color('Income:Q',
                    scale=alt.Scale(scheme='sinebow'),
                    bin=alt.Bin(maxbins=5))
)
scatters

st.markdown("""Add in altair charts with layout elements
 """)

col1,col2 = st.columns([0.7, 0.25])
col1.altair_chart(scatters, theme='streamlit',
                  use_container_width=True)
col2.markdown("Here is some text on the side of the plot.")
col2.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAXjp6mzNlkMEEiMomUfTEMiX8NHpopoyyXg&s')


st.header("Day 2 (Week 11)")

# Read in data with pandas
import pandas as pd
df = pd.read_csv(mobility_url)

#df
st.write(df)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
df['Seg_income'].plot(kind='hist',ax=ax)
#plt.show() # need to use streamlit infrastructure for this
st.pyplot(fig)

st.write("""Note I have added some things to 
         the requirements.txt file. """)
st.code("""
streamlit==1.39.0
altair
numpy
matplotlib
pandas
 """)

st.header("Widgets in Streamlit apps")

st.markdown("""Using markdown for a reminder, we can use
            widgets in Streamlit (similar to `ipywidgets`).
 """)

st.subheader('Feedback Widget')

st.markdown("""We could try the 
            [feedback widget](https://docs.streamlit.io/develop/api-reference/widgets/st.feedback).
 """)

st.markdown("Using the following code:")
st.code("""
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
         """)

# sentiment_mapping = ["one", "two", "three", "four", "five"]
# selected = st.feedback("stars")
# if selected is not None:
#     st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

st.write("How are you feeling right now?")
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None: # only run if a star is selected
    if selected < 1:
        st.markdown("Sorry to hear you are so sad :(")
    elif selected < 3:
        st.markdown("A solid medium is great!")
    else:
        st.markdown("Fantastic to hear you are having a great day!")

st.subheader("Connecting Widgets to Plots")

st.markdown("We'll start with a static plot:")

# bins along student to teacher ratio
bins = np.linspace(df['Student_teacher_ratio'].min(),
                   df['Student_teacher_ratio'].max(), 10)
#bins # note -- this will be "pandas-like" in view

table = df.pivot_table(index='State', 
                       columns=pd.cut(df['Student_teacher_ratio'],bins),
                       aggfunc='size')

fig, ax = plt.subplots()
ax.imshow(table.values, cmap='hot', interpolation='nearest')
ax.set_yticks(range(len(table.index)))
ax.set_yticklabels(table.index)
st.pyplot(fig)