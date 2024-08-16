---
title: Lecture 9.3 - Streamlit & HuggingFace Introduction; VSCode
layout: lecture
description: >-
 Streamlit, HuggingFace, VSCode ecosystem
date: 2023-10-19

---

## Altair

```javascript

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

chart
```

notes:
just some reminders for what we worked on last time -- mostly with altair and making some initial dashboards

---

## Altair in Streamlit (and Jekyll)

```javascript

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

chart
```

How can we share our creations with the public?

notes:
so we can make some cool things but how can we share them with our audience?

we'll discuss how to do this with Streamlit (and later Jekyll)

---

## Streamlit

[Streamlit](https://streamlit.io/) is a way to write "apps" in a Python script that can be hosted on the web.

![streamlit "hello world"](images/streamlit1.png)

notes:
where we see a simple example from the video linked above showing how Markdown as a string in Python is translated into headers and text on a page.

---

## HuggingFace

[HuggingFace](https://huggingface.co/) is the platform that we'll be using to host our interactive apps.

![huggingface icon](https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo-with-title.png)

notes:
have folks heard of huggingface?

huggingface is a place where folks can share code/datasets and also host apps 

---

## Spaces on HuggingFace

We will make use of [Streamlit "Spaces"](https://huggingface.co/spaces?sort=trending&search=streamlit) on HuggingFace to host our apps.

![huggingface spaces](images/huggingface_apps_list.png)

---

## Streamlit in HuggingFace

We'll learn how to build Altair visualizations like [this IS445 Demo](https://huggingface.co/spaces/jnaiman/is445_demo).

notes:
**go to this page!!!**

---

## VSCode to develop apps

We'll be using a new interface on PrairieLearn to develop code: VSCode

![](images/vscode_view.png)

---

## VSCode to develop apps

![](images/vscode_link.png)


notes: 
you'll see now a brow VSCode workspace option for in class activities

---

## VSCode to develop apps

![](images/vscode_link.png)

If you want to install locally:
* Install VSCode: https://code.visualstudio.com/download
* Install local conda environment: https://uiuc-ischool-dataviz.github.io/is445_bcubcg_fall2024/week01/installation_instructions.html


notes: 
if you want to install locally you'll have to figure out two steps

---

## VSCode to develop apps

![](images/vscode_link.png)

If you want to install locally:
* Install VSCode: https://code.visualstudio.com/download
* Install local conda environment: https://uiuc-ischool-dataviz.github.io/is445_bcubcg_fall2024/week01/installation_instructions.html

We don't expect you to do any of this!  You can just use the VSCode workspaces provided for you on PrairieLearn.


notes: 
you'll see now a brow VSCode workspace option for in class activities

---

## To Streamlit in Python!