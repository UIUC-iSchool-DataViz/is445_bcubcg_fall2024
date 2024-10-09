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
