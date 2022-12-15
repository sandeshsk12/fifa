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
    <h2 class="card-title">Analysis of mints</h2>
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


c1,c2=st.columns((7,3))

###### mint info
c1.write(grey_card(title='FIFA+ Mints',
text=' NFT minting takes place on aa <br> <br>'),unsafe_allow_html=True)
######


######## Mint stats
mint_stats_url="https://node-api.flipsidecrypto.com/api/v2/queries/b8e1b922-3a74-4de2-9169-4290b6e69f0d/data/latest"
mint_stats=pd.read_json(mint_stats_url)
mint_stats=mint_stats.T
mint_stats.columns=['Value']
mint_stats['Value']=mint_stats['Value'].apply(lambda x: int(x))
c2.dataframe(mint_stats,use_container_width=True)


########

c1,c2=st.columns((60,40))

######## Number of NFTS minted
mint_trends = "https://node-api.flipsidecrypto.com/api/v2/queries/76c297d4-0d36-4aab-b545-2985e54e5fa7/data/latest"
mint_trends = pd.read_json(mint_trends)

nft_sales_by_drop_fig_trend=px.bar( \
       data_frame=mint_trends,
       x='date',
       y="NUMBER_OF_NFTS",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Trend of Pack mints"
      )
nft_sales_by_drop_fig_trend.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig_trend.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2a048522-a80c-4cdb-b0d7-3a904aaf8416'>Query link</a>")
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
c1.plotly_chart(nft_sales_by_drop_fig_trend, use_container_width=True)

nft_sales_by_drop_fig=px.bar( \
       data_frame=mint_trends.groupby(by="DROP_NAME",as_index=False).sum(),
       y='DROP_NAME',
       x="NUMBER_OF_NFTS",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of Pack mints",
       orientation='h'
      )
nft_sales_by_drop_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2a048522-a80c-4cdb-b0d7-3a904aaf8416'>Query link</a>")
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
c2.plotly_chart(nft_sales_by_drop_fig, use_container_width=True)

######


c1,c2=st.columns((60,40))

######## Number of NFTS minted
nft_sales_by_drop_fig_trend=px.bar( \
       data_frame=mint_trends,
       x='date',
       y="NUMBER_OF_WALLETS",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Trend of Buyers"
      )
nft_sales_by_drop_fig_trend.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig_trend.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2a048522-a80c-4cdb-b0d7-3a904aaf8416'>Query link</a>")
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
c1.plotly_chart(nft_sales_by_drop_fig_trend, use_container_width=True)

nft_sales_by_drop_fig=px.bar( \
       data_frame=mint_trends.groupby(by="DROP_NAME",as_index=False).sum(),
       x='DROP_NAME',
       y="NUMBER_OF_WALLETS",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of Buyers",
       orientation='v'
      )
nft_sales_by_drop_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2a048522-a80c-4cdb-b0d7-3a904aaf8416'>Query link</a>")
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
c2.plotly_chart(nft_sales_by_drop_fig, use_container_width=True)

#######

c1,c2=st.columns((40,60))

######## Number of NFTS minted
nft_sales_by_drop_fig_trend=px.bar( \
       data_frame=mint_trends,
       x='date',
       y="USD_AMOUNT",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Trend of Volume($)"
      )
nft_sales_by_drop_fig_trend.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig_trend.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2a048522-a80c-4cdb-b0d7-3a904aaf8416'>Query link</a>")
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
c2.plotly_chart(nft_sales_by_drop_fig_trend, use_container_width=True)

nft_sales_by_drop_fig=px.pie( \
       data_frame=mint_trends.groupby(by="DROP_NAME",as_index=False).sum(),
       names='DROP_NAME',
       values="USD_AMOUNT",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of USD"
      )
nft_sales_by_drop_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2a048522-a80c-4cdb-b0d7-3a904aaf8416'>Query link</a>")
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
c1.plotly_chart(nft_sales_by_drop_fig, use_container_width=True)

#######
############ Observation 
st.write(grey_card(title='Observation',
text=""" 
From the above graphs, we notice that
because mint cannot control the rarity, we do not analyse it <br><br>"""),unsafe_allow_html=True)
#######
c1,c2=st.columns((25,75))

####### Average amount spent on each collection 
avg_spent_on_collection_fig=px.bar( \
       data_frame=mint_trends.groupby(by="DROP_NAME",as_index=False).mean(),
       x='DROP_NAME',
       y="USD_AMOUNT",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of USD"
      )
avg_spent_on_collection_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
avg_spent_on_collection_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2a048522-a80c-4cdb-b0d7-3a904aaf8416'>Query link</a>")
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
c2.plotly_chart(avg_spent_on_collection_fig, use_container_width=True)


c1.write(grey_card(title='Observation',text='ffffffff'),unsafe_allow_html=True)

##########
c1,c2=st.columns((40,60))
####### Distribution of event type
nft_minted_per_event_url="https://node-api.flipsidecrypto.com/api/v2/queries/a2b372f3-f4d7-4323-aa60-d2393df81b01/data/latest"
nft_minted_per_event=pd.read_json(nft_minted_per_event_url)

nft_minted_per_event_fig=px.pie( \
       data_frame=nft_minted_per_event,
       names='EVENT_TYPE',
       values="NUMBER_OF_NFTS",
       color='EVENT_TYPE',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of NFTS"
      )
nft_minted_per_event_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_minted_per_event_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/a2b372f3-f4d7-4323-aa60-d2393df81b01'>Query link</a>")
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
c2.plotly_chart(nft_minted_per_event_fig, use_container_width=True)
c1.write(grey_card(title='Observation',text='ffffffff'),unsafe_allow_html=True)

###### number of nfts minted for every hosts
top_hosts_url = "https://node-api.flipsidecrypto.com/api/v2/queries/841f1b27-41e0-4b71-bd02-035d5fa67462/data/latest"
top_hosts = pd.read_json(top_hosts_url)
top_hosts['HOST']=top_hosts['HOST'].apply(lambda x:x.replace("‚",'').strip().split('/')[0])
top_hosts=top_hosts.groupby(by='HOST',as_index=False).sum()

top_hosts_fig=px.choropleth(top_hosts,locationmode='country names',locations='HOST',color='NUMBER_OF_NFTS_MINTED',color_continuous_scale='Viridis',scope='world',
title='Number of NFTs minted in each host country')
top_hosts_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/841f1b27-41e0-4b71-bd02-035d5fa67462'>Query link</a>")
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

c1,c2=st.columns((20,80))
######### players with most NFT
c1.markdown('q')
top_player_nft_url = "https://node-api.flipsidecrypto.com/api/v2/queries/2e2d2f18-8232-47a4-97d9-496dfa9a56e6/data/latest"
top_player_nft = pd.read_json(top_player_nft_url)

top_player_nft_fig=px.bar( \
       data_frame=top_player_nft,
       x='PLAYER',
       y="NUMBER_OF_NFTS",
    #    color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="PLAYERS WITH MOST NFT"
      )
top_player_nft_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
top_player_nft_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2e2d2f18-8232-47a4-97d9-496dfa9a56e6'>Query link</a>")
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
c2.plotly_chart(top_player_nft_fig, use_container_width=True)
##############
c1,c2=st.columns((80,20))
########## Probability table
c2.write()
import math
from math import comb
import pandas as pd
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
prob_heatmap_fig=px.imshow(pd.pivot(calc_prob,index='Collection',columns='Rarity',values='Probability (%)'))


prob_heatmap_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
prob_heatmap_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/3abb6abe-2f0e-475e-8394-77289d28f6c0'>Query link</a>")
    , showarrow=False
    , x = 0.05
    , y = -0.2
    , xref='paper'
    , yref='paper' 
    , xanchor='right'
    , yanchor='bottom'
    , xshift=1
    , yshift=-5
    , font=dict(size=20, color="Yellow")
    , align="right"
    ,)
c1.plotly_chart(prob_heatmap_fig,use_container_width=True)


