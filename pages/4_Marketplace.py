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
    <div class="card text-white bg-secondary mb-" style="margin:1rem;" >
    <div class="card-header">{header}</div>
    <div class="card-body">
    <h3 class="card-title">{title}</h3>
    <p class="card-text">{text}
    </p>
    </div>
    </div>    
    """


###############
st.markdown("""
<div class="card text-white bg-warning mb-3" style="margin:1rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h3 class="card-title">Average profit and duration held</h3>
    <p class="card-text"></p>
  </div>
</div>"""
, unsafe_allow_html=True)
###############




c1,c2=st.columns((60,40))

######## Held time and profit made
held_time_and_profit_made_url = "https://node-api.flipsidecrypto.com/api/v2/queries/3ae53041-cb35-419c-8cb9-3eb84a9dadb2/data/latest"
held_time_and_profit_made = pd.read_json(held_time_and_profit_made_url)
held_time_fig=held_time_and_profit_made.groupby(['HELD_TIME','RARITY'],as_index=False).count()
held_time_fig=px.area(held_time_fig,x='HELD_TIME',y='MINT_AMOUNT',color='RARITY', title='Average holding period')
held_time_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
held_time_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/3ae53041-cb35-419c-8cb9-3eb84a9dadb2'>Query link</a>")
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
c1.plotly_chart(held_time_fig, use_container_width=True)

profit_made = "https://node-api.flipsidecrypto.com/api/v2/queries/3ae53041-cb35-419c-8cb9-3eb84a9dadb2/data/latest"
profit_made = pd.read_json(held_time_and_profit_made_url)
profit_made_fig=held_time_and_profit_made.groupby(['PROFIT','RARITY'],as_index=False).count()
profit_made_fig=px.area(profit_made_fig,x='PROFIT',y='MINT_AMOUNT',color='RARITY',log_x=True,log_y=True, title='Average Profit made')
profit_made_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
profit_made_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/3ae53041-cb35-419c-8cb9-3eb84a9dadb2'>Query link</a>")
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
c2.plotly_chart(profit_made_fig, use_container_width=True)
st.write(grey_card(title='Observation',text=""" \
    1. FIFA's NFT marketplace has a mandatory 14 day cooling period to avoid flippers. A cooling period of 14 days ensures that people cannot \
        sell the NFT they bought for 14 days. Hence we see a huge number of NFTs being sold after a period of 14 days. Most of the NFTs are sold 
        on the 15th day. Additionally the sales reduce drastically after the  3 week mark.<br>
    2. From the graph on the right, we can clearly see that a lot of rare NFTs are sold for smaller amounts, while majority of the iconic NFTs are sold at \
        higher price. <br>
    3. The higher bracket of Epic and lower cap of iconic overlap"""),unsafe_allow_html=True)

######




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
st.write(grey_card(title='Observation',text=""" \
    1. Initially when the marketplace launched, FIFA addresses accounted for 5 % of the new algorand users, however this has been on a decline since. with now only\
        0.05% of the new algorand users onboarding because of FIFA. <br>
    2. The number of weekly active users ( transacting more than twice in a week) has been a constant and hovers around 300 to 400 users. <br>"""),unsafe_allow_html=True)
