---
layout: week
visible: true
icon: undraw_playing_fetch_cm19.svg
notitle: true
examples:
  - filename: In Class Jekyll Files
    type: iodide
    title: In class Jekyll materials, Week 12
    description: Updating storage of Jekyll files in class
    link: https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2023/tree/master/week12/inClass
  - filename: Prep Jekyll Files
    type: iodide
    title: Prep Jekyll materials, Week 12
    description: We'll be building toward a webpage like <a href="https://jnaiman.github.io/online_cv_public/">this</a> today using <a href="https://jekyllrb.com/">Jekyll</a>+<a href="https://altair-viz.github.io/index.html">Altair</a>. 
    link: https://github.com/jnaiman/online_cv_public/blob/main/_example_projects/
  - filename: inClass_week12.ipynb
    type: ipynb
    title: In Class Notebook, Week 12
    description: In class notebook
  - filename: prep_notebook_week12.ipynb
    type: ipynb
    title: Prep Notebook, Week 12
    description: Prep notebook for this week
data:
  - filename: mobility.csv
    type: dataLink
    title: The Mobility dataset (online)
    description: A dataset of USA "mobility" which (I <b>think</b> comes from a <a href="https://www.census.gov/library/working-papers/2018/adrm/CES-WP-18-40R.html">a large census study from 1989-2015</a>) and is collected in several places <a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/mobility.csv">including right here</a>.  Here "mobility" is refering to how easy it is for a person to move up in economic status (<a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf">more info can be found here</a>) based on factors like parental income, location, race, etc.
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv
  - filename: building_inventory.csv
    type: dataLink
    title: Buildings dataset
    description: Illinois buildings dataset
    link: https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv
  - filename: corgs_per_country_over_time_columns_2020.csv
    type: dataLink
    title: Corgis per country over time 
    description: This dataset is from the <a href="http://cardiped.net/">Cardigan Archives</a> and <a href="https://github.com/UIUC-iSchool-DataViz/spring2020/blob/master/week12/corg/grabCorgData_subpages.py">scraped using Beautiful Soup in Python</a> and <a href="https://github.com/UIUC-iSchool-DataViz/spring2020/blob/master/week12/corg/calc_corgData.ipynb">further processed in Python</a> into this form.
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/corgs_per_country_over_time_columns_2020.csv

---

# Jekyll+Altair+vega-lite, Publishing Viz & Intro to SciViz

We move on to our next visualization tool -- Jekyll.


We talk a little bit about 3D graphics and how it relates to Scientific Visualiazation, and carry on with Jekyll and add in some Altair in Python.

Also, here is a slightly more in-depth explanation of path/ray tracing:

<iframe width="560" height="315" src="https://www.youtube.com/embed/frLwRLS_ZR0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



## Extra files

Full corgi dataset available [here](corg/corgiData_countries_full_2020.json).



## Optional reading list

 1. <a href="https://jekyllrb.com/tutorials/home/">Jekyll Tutorials (hit "Next" to see them at bottom)</a>
 2. <a href="https://books.google.com/books?hl=en&lr=&id=jUw7DwAAQBAJ&oi=fnd&pg=PA91&dq=scientific+visualization+misinformation&ots=Cv0QmoCdM2&sig=7xycURu8Um_C9VtHqf-aWg4qaEo#v=onepage&q=scientific%20visualization%20misinformation&f=false">Chapter 5: Dimensions of Visual Misinformation in the Emerging Media Landscape in the book "Misinformation and Mass Audiences"</a> 
 
