import streamlit as st


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.sidebar.success("Select a Page")

st.header('Multi-page Apps')

st.markdown("""
So far our apps have been rather long and have many parts!  We can organize this a bit better by building [multi-page apps](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app).
 """)

st.subheader('Reorganize our App')

st.markdown("""We need to do several things including:
 * Rename our app file to something that starts with a capital letter
 * Make sure this is the name that is in the `README.md` file
 * Add in some page info on our "main" page
 * Add in a sidebar on our main page to view all pages
 * Add in a `pages` directory
 * Add pages with the correct format to the `pages` directory
 * Reorganize our page into this new format
 """)

st.write("Let's get to each of these!")

st.subheader('Step 1: Create our "landing" page')

st.markdown("""
First, let's rename our `app.py` file to `Hello.py`.
            
Then, we need to make sure this is also updated in our `README.md` file.
            
We can then start running our script with `streamlit run Hello.py`.
 """)

st.subheader('Step 2: Add some page info to our "landing" page')

st.markdown("""Now, let's add in some page info for this landing page:
 """)
st.code("""
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
 """)

st.markdown("""Finally, let's add a sidebar to display all our pages:""")
st.code("""
st.sidebar.success("Select a Page")
 """)
st.markdown("**Make sure both of these last items are at the top of your `Hello.py` file!**")

st.subheader('Step 3: Create pages')

st.markdown("""First, create a folder called `pages/`. 
            
Then, create four pages:
1. `1_Data_Introduction.py`
1. `2_Widget_Exploration.py`
1. `3_Altair_Plots.py`
1. `4_Other_Tools.py`
            
**NOTE: The formatting here of the file names is specific!** It determines their order and how they appear on the sidebar.
            
Each page will need to have:
1. A `set_page_config` call, including a title and an icon
1. A message displayed on page selection with a `sidebar.header` call
            """)

st.markdown("""
Once this is done, we can then move the items from our original `app.py` file to each page.
 """)

# day 2/3 -- "grab bag" of other things
# multi-page apps? ==> maybe day 2? ==> does this work with HF apps??
# Week 12 --  https://docs.streamlit.io/develop/tutorials/databases <- touch on but say we'll be just doing csv files
# Week 12 -- embedding streamlit spaces on other webpages? wait until Jekyll? https://huggingface.co/docs/hub/en/spaces-sdks-streamlit#embed-streamlit-spaces-on-other-webpages

