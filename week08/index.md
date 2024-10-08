---
layout: week
visible: true
icon: undraw_Around_the_world_re_n353.svg
notitle: true
examples:
  - filename: inClass_week08.ipynb
    type: ipynb
    title: In class notebook
    description: Placeholder for in class coding
  - filename: prep_notebook_week08.ipynb
    type: ipynb
    title: Prep Notebook, Week 8
    description: Prep notebook for this week
  - filename: spring2019_prep_notebook_week07_part1.ipynb
    type: ipynb
    title: spring2019_prep_notebook_week07_part1.ipynb
  - filename: spring2019_prep_notebook_week07_part2.ipynb
    type: ipynb
    title: spring2019_prep_notebook_week07_part2.ipynb
  - filename: spring2019_prep_notebook_week07_part3.ipynb
    type: ipynb
    title: spring2019_prep_notebook_week07_part3.ipynb
data:
  - filename: building_inventory.csv
    type: dataLink
    title: Buildings dataset
    description: Illinois buildings dataset
    link: https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv
  - filename: Champaign GIS Repo
    type: dataLink
    title: Champaign GIS Repo
    description: Various GIS datasets provided by Champaign
    link: https://gis-cityofchampaign.opendata.arcgis.com/search?collection=Dataset 
  - filename: Census GIS Repo
    type: dataLink
    title: Census GIS Repo
    description: GIS data provided by the US Census
    link: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html 
---

# Maps, maps and more maps

We will start thinking about maps & map projection, both in `bqplot` and `matplotlib` and with `geopandas`+`contextily`.  We'll continue this week with building dashboards of mappable data.

<!-- ## Downloads

### Data:

 * <a href="https://uiuc-ischool-dataviz.github.io/spring2019online/week04/data/ufo-scrubbed-geocoded-time-standardized-00.csv" download>The UFO Sitings Dataset (13Mb) - ufo-scrubbed-geocoded-time-standardized-00.csv</a>
 * <a href='total_export.csv' download>State export data (8Kb) - total_export.csv</a>
 * <a href="market_map_data.csv" download>Backup: Surgery Charges Dataset (37Mb) - market_map_data.csv</a>
 * <a href="https://uiuc-ischool-dataviz.github.io/spring2019online/week08/data/data_tohoku_norm_transpose.csv" download>Earthquake sensor data (59Mb) - data_tohoku_norm_transpose.csv</a>
 * <a href="https://uiuc-ischool-dataviz.github.io/spring2019online/week08/data/location.txt" download>Earthquake locations data (12Kb) - location.txt</a>

