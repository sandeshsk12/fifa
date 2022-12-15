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
#st.markdown('# FIFA+ Collect Marketplace Dashboard')



st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',unsafe_allow_html=True)


st.markdown(
    """
    <div class="card text-white bg-primary mb-3">
  <div class="card-header"></div>
  <div class="card-body">
    <h1 class="card-title">
    FIFA+ Collect Marketplace Dashboard
    </h1>
    <p class="card-text"></p>
  </div>
  """, unsafe_allow_html=True)

  ###############
st.markdown("""
<div class="card text-white bg-warning mb-3" style="margin:1rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h3 class="card-title">Probability calculator </h3>
    <p class="card-text"></p>
  </div>
</div>"""
, unsafe_allow_html=True)
###############




c1,c2,c3=st.columns((30,30,40))
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

c3.markdown('### The probability that you will get a {} card if you pick the {} collection is {} % '.format(card,drop,round(z,2)))


  ###############
st.markdown("""
<div class="card text-white bg-warning mb-3" style="margin:1rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h3 class="card-title">Find the trend</h3>
    <p class="card-text"></p>
  </div>
</div>"""
, unsafe_allow_html=True)
###############


c1,c2,c3,c4  = st.columns(4)
parameter=c2.selectbox("Enter parameter name",('RARITY','DROP_NAME'))
metric=c1.selectbox("Enter metric name",('NUMBER_OF_NFTS','USD_AMOUNT','NUMBER_OF_WALLETS'))
sale_type=c3.selectbox("mint or secondary sale",('mint','secondary'))
tot='https://node-api.flipsidecrypto.com/api/v2/queries/effd7b89-9214-4544-8fc5-d8afce5b97af/data/latest'
df=pd.read_json(tot)

df_fig=px.bar( \
       df[df['SALE_TYPE']==sale_type].groupby(by=['date',parameter],as_index=False).sum(),
       x='date',
       y=metric,
       color=parameter,\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="({}) sale Trend of {} over {}".format(sale_type,parameter,metric)
      )
df_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
df_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/effd7b89-9214-4544-8fc5-d8afce5b97af'>Query link</a>")
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
st.plotly_chart(df_fig, use_container_width=True)

c1,c2=st.columns(2)
df_fig=px.bar( \
       df[df['SALE_TYPE']==sale_type].groupby(by=['date',parameter],as_index=False).sum(),
       y=parameter,
       x=metric,
       color=parameter,\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="({}) Distribution of {} over {}".format(sale_type,parameter,metric)
    #    orientation='h'
      )
df_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
df_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/effd7b89-9214-4544-8fc5-d8afce5b97af'>Query link</a>")
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
c2.plotly_chart(df_fig, use_container_width=True)

df_fig=px.pie( \
       df[df['SALE_TYPE']==sale_type].groupby(by=['date',parameter],as_index=False).sum(),
       names=parameter,
       values=metric,
       color=parameter,\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="({}) Distribution of {} over {}".format(sale_type,parameter,metric)
      )
df_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
df_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/effd7b89-9214-4544-8fc5-d8afce5b97af'>Query link</a>")
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
c1.plotly_chart(df_fig, use_container_width=True)



  ###############
st.markdown("""
<div class="card text-white bg-warning mb-3" style="margin:1rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h3 class="card-title">Where do the NFTs come from </h3>
    <p class="card-text"></p>
  </div>
</div>"""
, unsafe_allow_html=True)
###############

###### number of nfts minted for every hosts
c1,c2,c3,c4  = st.columns(4)
drop=c1.selectbox("drop name",('genesis','archives','south american flair','archives 2'))
card=c2.selectbox("card type",('Common','Rare','Epic','Iconic'))
metric=c3.selectbox("metric",('NUMBER_OF_NFTS','USD_AMOUNT','NUMBER_OF_WALLETS'))
sale_type=c4.selectbox("mint or secondary",('mint','secondary'))

top_hosts_url = "https://node-api.flipsidecrypto.com/api/v2/queries/887204dd-2467-46b6-b19a-e04b62d7e615/data/latest"
top_hosts = pd.read_json(top_hosts_url)
top_hosts['HOST']=top_hosts['HOST'].apply(lambda x:x.replace("‚",'').strip().split('/')[0])
top_hosts=top_hosts[top_hosts['SALE_TYPE']==sale_type]
top_hosts=top_hosts[top_hosts['DROP_NAME']==drop]
top_hosts=top_hosts[top_hosts['RARITY']==card]
top_hosts=top_hosts.groupby(by='HOST',as_index=False).sum()
top_hosts_fig=px.choropleth(top_hosts,locationmode='country names',locations='HOST',color=metric,color_continuous_scale='Viridis',scope='world',
title='Number of NFTs minted in each host country')
top_hosts_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/887204dd-2467-46b6-b19a-e04b62d7e615'>Query link</a>")
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
st.plotly_chart(top_hosts_fig,use_container_width=True)

c1,c2=st.columns((30,70))
