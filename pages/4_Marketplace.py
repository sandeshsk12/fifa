import streamlit as st 
import seaborn as sns
import plotly.express as px
from shroomdk import ShroomDK
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
import time
from plotly.subplots import make_subplots

from urllib.request import urlopen 
import json
import requests
from PIL import  Image
import plotly.graph_objs as go





st.set_page_config(page_title="Data Explorer", layout="wide",initial_sidebar_state="expanded")

# st.sidebar.success("select a page above")
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',unsafe_allow_html=True)

st.markdown(
    """
    <div class="card text-white bg-primary mb-3">
  
  <div class="card-body">
    <h2 class="card-title">Analysis of Marketplace</h2>
  </div>
</div>
"""
,unsafe_allow_html=True)

def grey_card(header='',title='',text=''):
    return f"""
    <div class="card text-white bg-secondary mb-" >
    <div class="card-header">{header}</div>
    <div class="card-body">
    <h3 class="card-title">{title}</h3>
    <p class="card-text">{text}
    </p>
    </div>
    </div>    
    """







######## Number of NFTS minted
nve = "https://node-api.flipsidecrypto.com/api/v2/queries/51162503-f456-4ad1-837b-d220aae3a1bc/data/latest"
nve = pd.read_json(nve)

nve_image=px.histogram( \
       data_frame=nve,
       x='DOJ',
       y='FIFA_CNT',
       color='USER_TYPE',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="New vs Existing users",
       barnorm='percent',
       log_y=True
    #    nbins=len(nve[])
      )
nve_image.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nve_image.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/51162503-f456-4ad1-837b-d220aae3a1bc'>Query link</a>")
    , showarrow=False
    , x = 0.05
    , y = -0.2
    , xref='paper'
    , yref='paper' 
    , xanchor='right'
    , yanchor='bottom'
    , xshift=1
    , yshift=-5
    , font=dict(size=15, color="Yellow")
    , align="right"
    ,)
st.plotly_chart(nve_image, use_container_width=True)

wau = "https://node-api.flipsidecrypto.com/api/v2/queries/5262b483-f968-4dc4-a542-5d5e63480ffb/data/latest"
wau = pd.read_json(wau)

wau_image=px.bar( \
       data_frame=wau,
       x='DATE',
       y="N_USERS",
       color='TYPE',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Weekly active users",
    #    orientation='h'
      )
wau_image.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
wau_image.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/5262b483-f968-4dc4-a542-5d5e63480ffb'>Query link</a>")
    , showarrow=False
    , x = 0.05
    , y = -0.2
    , xref='paper'
    , yref='paper' 
    , xanchor='right'
    , yanchor='bottom'
    , xshift=1
    , yshift=-5
    , font=dict(size=15, color="Yellow")
    , align="right"
    ,)
st.plotly_chart(wau_image, use_container_width=True)

######