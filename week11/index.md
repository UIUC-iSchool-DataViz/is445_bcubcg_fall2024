---
layout: week
visible: true
icon: undraw_Books_l33t.svg
notitle: true
examples:
  - filename: prep_script_week11.py
    type: py
    title: Prep script file, Week 11
    description: In class notebook
  - filename: InClass
    type: iodide
    title: In class Streamlit App, Week 10
    description: Updating storage of Streamlit files in class
    link: https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2024/tree/master/week11/inClass
  # - filename: inClass_script_week11.py
  #   type: py
  #   title: In class script file, Week 10
  #   description: In class notebook
  # - filename: prep-repo
  #   type: iodide
  #   title: Prep online_cv file, Week 10
  #   description: We'll be building toward a webpage like <a href="https://jnaiman.github.io/online_cv_public/">this</a> today using <a href="https://jekyllrb.com/">Jekyll</a>+<a href="https://altair-viz.github.io/index.html">Altair</a>. 
  #   link: https://github.com/jnaiman/online_cv_spring2023
  # - filename: inClass_week10.ipynb
  #   type: ipynb
  #   title: In Class Notebook, Week 10
  #   description: In class notebook
  # - filename: prep_notebook_week10.ipynb
  #   type: ipynb
  #   title: Prep Notebook, Week 10
  #   description: Prep notebook for this week
data:
  - filename: mobility.csv
    type: dataLink
    title: The Mobility dataset (online)
    description: A dataset of USA "mobility" which (I <b>think</b> comes from a <a href="https://www.census.gov/library/working-papers/2018/adrm/CES-WP-18-40R.html">a large census study from 1989-2015</a>) and is collected in several places <a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/mobility.csv">including right here</a>.  Here "mobility" is refering to how easy it is for a person to move up in economic status (<a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf">more info can be found here</a>) based on factors like parental income, location, race, etc.
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv
---

# Web dev with Streamlit + HuggingFace

Today we'll cover a brief intro of [Streamlit](https://streamlit.io/) on [HuggingFace Spaces](https://huggingface.co/docs/hub/en/spaces-sdks-streamlit)and web development in general.

 
## Extra files


Full corgi dataset available [here](corg/corgiData_countries_full_2020.json).



## Optional reading list

 1. <a href="https://streamlit.io/">Streamlit docs</a>
 2. <a href="https://huggingface.co/docs/hub/en/spaces-sdks-streamlit">Streamlit on HuggingFace</a>
 3. <a href="https://altair-viz.github.io/gallery/index.html">Altair Docs</a> - in particular <a href="https://altair-viz.github.io/user_guide/data.html#including-index-data">Including Indexes</a>, <a href="https://altair-viz.github.io/altair-tutorial/notebooks/06-Selections.html">Interactivity & Selections</a>, <a href="https://altair-viz.github.io/gallery/multiline_tooltip.html#multi-line-tooltip">Multi-line tooltips</a>, <a href="https://altair-viz.github.io/user_guide/interactions.html#bindings-selections-conditions-making-charts-interactive">Interactive Binning</a>, <a href="https://altair-viz.github.io/user_guide/transform/filter.html#filter-transform">Filter Transformations</a>