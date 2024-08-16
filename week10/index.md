---
layout: week
visible: true
icon: undraw_programmer_imem.svg
notitle: true
examples:
  - filename: prep_script_week10.py
    type: py
    title: Prep script file, Week 10
    description: In class notebook
  - filename: prep_notebook_week09_fall2022
    type: iodidePast
    title: Prep Starboard Notebook, Fall 2023
    description: Prep Starboard Notebook
    link: https://starboard.gg/nb/n9nb6N8
  - filename: prep_notebook_week10_fall2022
    type: iodidePast
    title: Extra Starboard Fall 2023 - Dashboarding
    description: Prep Starboard Notebook
    link: https://starboard.gg/nb/nuXwr0l
  - filename: prep_notebook_week11
    type: iodidePast
    title: Previous class notebook
    description: Prep Iodide Notebook, Spring 2020
    link: https://alpha.iodide.io/notebooks/4399/
  - filename: prep_notebook_week10_fall2021
    type: iodidePast
    title: Previous class notebook
    description: Prep Starboard Notebook, Fall 2021
    link: https://starboard.gg/nb/nXvyanN
data:
  - filename: GDP.csv
    type: dataLink
    title: The GDP dataset (online)
    description: GDP dataset from FRED (stored online for easy linking in Starboard)
    link:  https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/GDP.csv
  - filename: mobility.csv
    type: dataLink
    title: The Mobility dataset (online)
    description: A dataset of USA "mobility" which (I <b>think</b> comes from a <a href="https://www.census.gov/library/working-papers/2018/adrm/CES-WP-18-40R.html">a large census study from 1989-2015</a>) and is collected in several places <a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/mobility.csv">including right here</a>.  Here "mobility" is refering to how easy it is for a person to move up in economic status (<a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf">more info can be found here</a>) based on factors like parental income, location, race, etc.
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv
---

# Web dev with Streamlit + HuggingFace; Considering your audience

Starting to develop Streamlit apps for hosting on HuggingFace.

Viz for self/peers/public.


## Optional reading list

 1. <a href="https://medium.com/multiple-views-visualization-research-explained/same-data-multiple-perspectives-curse-of-knowledge-in-visual-data-communication-d827c381f936">Same Data, Multiple Perspectives</a>
 2. <a href="https://serialmentor.com/dataviz/telling-a-story.html">FDV, Ch. 29: Telling a story and making a point</a>
 3. <a href="https://streamlit.io/">Streamlit docs</a>
 4. <a href="https://huggingface.co/docs/hub/en/spaces-sdks-streamlit">Streamlit on HuggingFace</a>
 5. <a href="https://altair-viz.github.io/gallery/index.html">Altair Docs</a> - in particular <a href="https://altair-viz.github.io/user_guide/data.html#including-index-data">Including Indexes</a>, <a href="https://altair-viz.github.io/altair-tutorial/notebooks/06-Selections.html">Interactivity & Selections</a>, <a href="https://altair-viz.github.io/gallery/multiline_tooltip.html#multi-line-tooltip">Multi-line tooltips</a>, <a href="https://altair-viz.github.io/user_guide/interactions.html#bindings-selections-conditions-making-charts-interactive">Interactive Binning</a>, <a href="https://altair-viz.github.io/user_guide/transform/filter.html#filter-transform">Filter Transformations</a>