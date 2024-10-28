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