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





st.set_page_config(page_title="Data Explorer", layout="wide",initial_sidebar_state="expanded")
st.markdown('# FIFA+ COllect marketplace')
st.sidebar.success("select a page above")


st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',unsafe_allow_html=True)


st.markdown(
    """
    <div class="card text-white bg-primary mb-3" style="max-width: 18rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h5 class="card-title">
    Introduction
    </h5>
    <p class="card-text">Introduction.</p>
  </div>
  """, unsafe_allow_html=True)

mint_trends = "https://node-api.flipsidecrypto.com/api/v2/queries/76c297d4-0d36-4aab-b545-2985e54e5fa7/data/latest"
mint_trends = pd.read_json(mint_trends)
nft_sales_by_drop_fig=px.bar( \
       data_frame=mint_trends.groupby(by="DROP_NAME",as_index=False).sum(),
       y='DROP_NAME',
       x="NUMBER_OF_NFTS",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of Pack sales",
       orientation='h'
      )
nft_sales_by_drop_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(245,245,245,255)',})
nft_sales_by_drop_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2a048522-a80c-4cdb-b0d7-3a904aaf8416'>Query link</a>")
    , showarrow=False
    , x = 1.2
    , y = -0.15
    , xref='paper'
    , yref='paper' 
    , xanchor='right'
    , yanchor='bottom'
    , xshift=1
    , yshift=-5
    , font=dict(size=15, color="black")
    , align="right"
    ,)
st.plotly_chart(nft_sales_by_drop_fig)



a=st.radio('enter',['DROP_NAME','DROP_NAME'],horizontal=True)
a1,a2,a3=st.columns(3)

nft_sales_by_drop_fig=px.bar( \
       data_frame=mint_trends.groupby(by=a,as_index=False).sum(),
       y='DROP_NAME',
       x="NUMBER_OF_NFTS",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of Pack sales",
       orientation='h'
      )
nft_sales_by_drop_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(75,75,75,255)',})
nft_sales_by_drop_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2a048522-a80c-4cdb-b0d7-3a904aaf8416'>Query link</a>")
    , showarrow=False
    , x = 1.2
    , y = -0.15
    , xref='paper'
    , yref='paper' 
    , xanchor='right'
    , yanchor='bottom'
    , xshift=1
    , yshift=-5
    , font=dict(size=15, color="black")
    , align="right"
    ,)
a1.plotly_chart(nft_sales_by_drop_fig,use_container_width=True)
with a2:
    st.markdown('## a')
    st.markdown('## a')
    # st.plotly_chart(nft_sales_by_drop_fig,use_container_width=True)


c1,c2=st.columns(2)
drop=c1.selectbox("Enter drop name",('Genesis','Archives','South American Flair','Archives 2'))
card=c1.selectbox("Enter the card you want",('Common','Rare','Epic','Iconic'))

prob = "https://node-api.flipsidecrypto.com/api/v2/queries/3abb6abe-2f0e-475e-8394-77289d28f6c0/data/latest"
prob = pd.read_json(prob)
calc=[]
for i in prob['DROP_NAME'].unique():
    for j in prob['RARITY'].unique():
        a=prob.where((prob['DROP_NAME']==i) & (prob['RARITY']==j)).dropna()
        c=int([x for x in a['count']][0])
        b=prob.where((prob['DROP_NAME']==i)).dropna()
        b=b.groupby(by='DROP_NAME',as_index=False).sum()
        d=int([x for x in b['count']][0])
        z=((d-c)/d)*(((d-c-1)/(d-1)))*(((d-c-2)/(d-2)))
#         print(i,j,1-z)
        calc.append([i,j,(1-z)*100])
calc_prob=pd.DataFrame(calc)
calc_prob.columns=['Collection','Rarity','Probability (%)']

t=pd.pivot(calc_prob,index='Collection',columns='Rarity',values='Probability (%)')
z=(t[(card)][str.lower(drop)])

c2.markdown('## The probability that you will get a {} card if you pick the {} collecion is {} '.format(card,drop,z))

c2.markdown(
    """
    <div class="card text-white bg-primary mb-3" style="max-width: 18rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h5 class="card-title">
    <p>The probability that you will get <p>"{card}"</p> if you pick the {} collecion is {}.format(card,drop,z)</p>
    </h5>
    <p class="card-text">Introduction.</p>
  </div>
  """, unsafe_allow_html=True)
