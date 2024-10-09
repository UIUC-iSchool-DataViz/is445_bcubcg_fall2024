import streamlit as st

st.set_page_config(page_title="Altair Plots", page_icon=":1234:")
st.sidebar.header("Altair Plots")

st.title('Altair Plots!')
st.write("""This is probably the main page we'd be showing in a "real" app.""")

# Let's start by copying things we did last time
import streamlit as st
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
