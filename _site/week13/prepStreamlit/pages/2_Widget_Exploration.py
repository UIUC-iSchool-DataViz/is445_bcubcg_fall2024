import streamlit as st

st.set_page_config(page_title="Widget Exploration", page_icon=":1234:")
st.sidebar.header("Widget Exploration")

st.title('Widget Exploration')

st.write("""In a "real" app, we probably wouldn't 
publish our explorations, but here it is a nice excuse to use pages here :smiley:.""")


st.write("How great are you feeling right now?")
sentiment_mapping = ["one", "two", "three", "four", "five"] # map to these numers
selected = st.feedback("stars")
if selected is not None: # make sure we have a selection
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    if selected < 1:
        st.markdown('Sorry to hear you are so sad :(')
    elif selected < 3:
        st.markdown('A solid medium is great!')
    else:
        st.markdown('Fantastic you are having such a great day!')

st.subheader('Radio Buttons')

st.markdown("""
Let's try out a [radio button](https://docs.streamlit.io/develop/api-reference/widgets/st.radio) example.
""")

favoriteViz = st.radio(
    "What's your visualization tool so far?",
    [":rainbow[Streamlit]", "vega-lite :sparkles:", "matplotlib :material/Home:"],
    captions=[
        "New and cool!",
        "So sparkly.",
        "Familiar and comforting.",
    ],
)

if favoriteViz == ":rainbow[Streamlit]":
    st.write("You selected Streamlit!")
else:
    st.write("You didn't select Streamlit but that's ok, Data Viz still likes you :grin:")

st.header('Connecting Plots and Widgets')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO


df = pd.read_csv("https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv")

# vertical alignment so they end up side by side
fig_col2, controls_col2 = st.columns([2,1], vertical_alignment='center')

bins = np.linspace(df['Student_teacher_ratio'].min(),df['Student_teacher_ratio'].max(), 10)
table = df.pivot_table(index='State', columns=pd.cut(df['Student_teacher_ratio'], bins), aggfunc='size')

# multi-select
states_selected2 = controls_col2.multiselect('Which states do you want to view?', 
                                             table.index.values)#, key='unik1155') 
#                                            had to pass unique key to have double widgets with same value

# range slider -- added
student_teacher_ratio_range = controls_col2.slider("Range of student teacher ratio:", 
                                                   df['Student_teacher_ratio'].min(), 
                                                   df['Student_teacher_ratio'].max(), 
                                                   (0.25*df['Student_teacher_ratio'].mean(), 
                                                    0.75*df['Student_teacher_ratio'].mean()))

# note all the "2's" here, probably will just update the original one
if len(states_selected2) > 0: # here we set a default value for the slider, so no need to have a tag
    min_range = student_teacher_ratio_range[0] # added
    max_range = student_teacher_ratio_range[1] # added

    df_subset2 = df[(df['State'].isin(states_selected2)) & (df['Student_teacher_ratio'] >= min_range) & (df['Student_teacher_ratio']<=max_range)] # changed

    # just 10 bins over the full range --> changed
    bins2 = 10 #np.linspace(df['Student_teacher_ratio'].min(),df['Student_teacher_ratio'].max(), 10)

    # make pivot table -- changed
    table_sub2 = df_subset2.pivot_table(index='State', 
                                  columns=pd.cut(df_subset2['Student_teacher_ratio'], bins2), 
                                  aggfunc='size')

    base_size = 4
    fig2,ax2 = plt.subplots(figsize=(base_size,2*base_size)) # this changed too for different size
    extent2 = [df_subset2['Student_teacher_ratio'].min(), 
               df_subset2['Student_teacher_ratio'].max(), 
               0, len(table_sub2.index)]
    ax2.imshow(table_sub2.values, cmap='hot', interpolation='nearest', extent=extent2)
    ax2.set_yticks(range(len(table_sub2.index)))
    ax2.set_yticklabels(table_sub2.index)
    #ax2.set_xticklabels()

    buf2 = BytesIO()
    fig2.tight_layout()
    fig2.savefig(buf2, format="png")
    fig_col2.image(buf2, width = 400) # changed here to fit better
else:
    min_range = student_teacher_ratio_range[0] # added
    max_range = student_teacher_ratio_range[1] # added

    df_subset2 = df[(df['Student_teacher_ratio'] >= min_range) & (df['Student_teacher_ratio']<=max_range)] # changed

    # just 10 bins over the full range --> changed
    bins2 = 10 #np.linspace(df['Student_teacher_ratio'].min(),df['Student_teacher_ratio'].max(), 10)

    # make pivot table -- changed
    table_sub2 = df_subset2.pivot_table(index='State', 
                                  columns=pd.cut(df_subset2['Student_teacher_ratio'], bins2), 
                                  aggfunc='size')

    base_size = 4
    fig2,ax2 = plt.subplots(figsize=(base_size,2*base_size)) # this changed too for different size
    extent2 = [df_subset2['Student_teacher_ratio'].min(), 
               df_subset2['Student_teacher_ratio'].max(), 
               0, len(table_sub2.index)]
    ax2.imshow(table_sub2.values, cmap='hot', interpolation='nearest', extent=extent2)
    ax2.set_yticks(range(len(table_sub2.index)))
    ax2.set_yticklabels(table_sub2.index)
    #ax2.set_xticklabels()

    buf2 = BytesIO()
    fig2.tight_layout()
    fig2.savefig(buf2, format="png")
    fig_col2.image(buf2, width = 400) # changed here to fit better