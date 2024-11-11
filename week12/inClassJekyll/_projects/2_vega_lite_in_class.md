---
name: In Class Example
tools: [Python, HTML, vega-lite, Altair]
image: assets/pngs/vega_editor_viz.png
description: This is an in class example.
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---


# In Class Examples

## Example 1: Directly from Vega-editor

**Be careful:** make sure the full data-path is in the URL in the vega-editor.

<vegachart schema-url="{{ site.baseurl }}/assets/json/from_vega_editor.json" style="width: 100%"></vegachart>

## Example 2.1: From Altair

This is a plot I saved from Altair in Python.

<vegachart schema-url="{{ site.baseurl }}/assets/json/population_scatter.json" style="width: 100%"></vegachart>

For single (non-faceted) plots, we can make them change with the container:
<vegachart schema-url="{{ site.baseurl }}/assets/json/population_scatter_container.json" style="width: 100%"></vegachart>

This is not so for side-by-side plots: 
<vegachart schema-url="{{ site.baseurl }}/assets/json/mobility_container.json" style="width: 100%"></vegachart>

But I can mess with the individual plot sizes:
<vegachart schema-url="{{ site.baseurl }}/assets/json/mobility_small.json" style="width: 100%"></vegachart>

### Can also pull from a dataframe
<vegachart schema-url="{{ site.baseurl }}/assets/json/mobility_from_df.json" style="width: 100%"></vegachart>



## Search The Data & Methods

Below is where we can put some links to both the data and the analysis code as buttons:

```
<div class="left">
{% include elements/button.html link="https://github.com/vega/vega/blob/main/docs/data/cars.json" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://blog.4dcu.be/programming/2021/05/03/Interactive-Visualizations.html" text="The Analysis" %}
</div>
```

<!-- these are written in a combo of html and liquid --> 

<div class="left">
{% include elements/button.html link="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2024/blob/main/week12/inClass_week12.ipynb" text="The Analysis" %}
</div>

