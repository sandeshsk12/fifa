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
    <h2 class="card-title">Analysis of Secondary Sales</h2>
  </div>
</div>
"""
,unsafe_allow_html=True)

def grey_card(header='',title='',text=''):
    return f"""
    <div class="card text-white bg-secondary mb-"  style="margin:1rem;">
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
c1.write(grey_card(title='FIFA+ Secondary sales',
text=' NFT minting takes place on aa <br> <br>'),unsafe_allow_html=True)
######


######## Mint stats
sec_stats_url="https://node-api.flipsidecrypto.com/api/v2/queries/a185ace6-3651-4ae0-b041-6ae871de2021/data/latest"
sec_stats=pd.read_json(sec_stats_url)
sec_stats=sec_stats.T
sec_stats.columns=['Value']
sec_stats['Value']=sec_stats['Value'].apply(lambda x: int(x))
c2.dataframe(sec_stats,use_container_width=True)


###############
st.markdown("""
<div class="card text-white bg-warning mb-3" style="margin:1rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h3 class="card-title">Analysis of Pack sales</h3>
    <p class="card-text"></p>
  </div>
</div>"""
, unsafe_allow_html=True)
###############

c1,c2=st.columns((60,40))



######## Number of NFTS minted
mint_trends = "https://node-api.flipsidecrypto.com/api/v2/queries/2d9dbf0f-0a9a-46a2-b13d-e318fd39f37f/data/latest"
mint_trends = pd.read_json(mint_trends)

nft_sales_by_drop_fig_trend=px.bar( \
       data_frame=mint_trends,
       x='date',
       y="NUMBER_OF_NFTS",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Trend of Pack Sales"
      )
nft_sales_by_drop_fig_trend.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig_trend.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2d9dbf0f-0a9a-46a2-b13d-e318fd39f37f'>Query link</a>")
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
       title="Distibution of Pack sales",
       orientation='h'
      )
nft_sales_by_drop_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2d9dbf0f-0a9a-46a2-b13d-e318fd39f37f'>Query link</a>")
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
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2d9dbf0f-0a9a-46a2-b13d-e318fd39f37f'>Query link</a>")
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
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2d9dbf0f-0a9a-46a2-b13d-e318fd39f37f'>Query link</a>")
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
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2d9dbf0f-0a9a-46a2-b13d-e318fd39f37f'>Query link</a>")
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
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/2d9dbf0f-0a9a-46a2-b13d-e318fd39f37f'>Query link</a>")
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
From the above graphs we notice that <br>
1. The number of NFTs sold in secondary marketplace were the highest in the 2nd and 3rd week of Novemeer. Primarily due to new pack launches and the hype aound Football. <br>
2. Genesis pack was the first pack to be on sale and accounts for almost 80% of the sales. And even today has the most amount of sales. <br>
3. Genessis packs alone have contributed to 83% of the volume generated by FIFA+ COLLECT NFT Marketplace.<br>
4. The South american Flair (psst, higher chance of Iconic card here) which released on Novemeber 15,2022 is quickly graining ground to become one of the best sellers.<br><br>
<br>"""),unsafe_allow_html=True)
#######
c1,c2=st.columns((25,75))

####### Average amount spent on each collection 
t=mint_trends.groupby(by="DROP_NAME",as_index=False).sum()
t['avg']=t['USD_AMOUNT']/t['NUMBER_OF_NFTS']

avg_spent_on_collection_fig=px.bar( \
       data_frame=t,
       x='DROP_NAME',
       y="avg",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Average cost of each pack"
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


c1.write(grey_card(title='Observation',text='<br><br>In the secondary marketplace, Genesis cards are more pricier than the rest costing an average of 35 USD. However\
    south american flair which is the costliest collection to mint does not rank 1 in terms of resale value.'),unsafe_allow_html=True)


##################




###############
st.markdown("""
<div class="card text-white bg-warning mb-3" style="margin:1rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h3 class="card-title">Analysis of Rarity cards</h3>
    <p class="card-text"></p>
  </div>
</div>"""
, unsafe_allow_html=True)
###############










c1,c2=st.columns((60,40))

######## Number of NFTS minted
mint_trends = "https://node-api.flipsidecrypto.com/api/v2/queries/e2d37d47-4215-45b4-82cb-de83913ea805/data/latest"
mint_trends = pd.read_json(mint_trends)

nft_sales_by_drop_fig_trend=px.bar( \
       data_frame=mint_trends,
       x='date',
       y="NUMBER_OF_NFTS",
       color='RARITY',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Trend of Pack Sales"
      )
nft_sales_by_drop_fig_trend.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig_trend.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/e2d37d47-4215-45b4-82cb-de83913ea805'>Query link</a>")
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
       data_frame=mint_trends.groupby(by="RARITY",as_index=False).sum(),
       y='RARITY',
       x="NUMBER_OF_NFTS",
       color='RARITY',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of Pack sales",
       orientation='h'
      )
nft_sales_by_drop_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/e2d37d47-4215-45b4-82cb-de83913ea805'>Query link</a>")
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
       color='RARITY',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Trend of Buyers"
      )
nft_sales_by_drop_fig_trend.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig_trend.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/e2d37d47-4215-45b4-82cb-de83913ea805'>Query link</a>")
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
       data_frame=mint_trends.groupby(by="RARITY",as_index=False).sum(),
       x='RARITY',
       y="NUMBER_OF_WALLETS",
       color='RARITY',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of Buyers",
       orientation='v'
      )
nft_sales_by_drop_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/e2d37d47-4215-45b4-82cb-de83913ea805'>Query link</a>")
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
       color='RARITY',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Trend of Volume($)"
      )
nft_sales_by_drop_fig_trend.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig_trend.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/e2d37d47-4215-45b4-82cb-de83913ea805'>Query link</a>")
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
       data_frame=mint_trends.groupby(by="RARITY",as_index=False).sum(),
       names='RARITY',
       values="USD_AMOUNT",
       color='RARITY',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Distibution of USD"
      )
nft_sales_by_drop_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_sales_by_drop_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/e2d37d47-4215-45b4-82cb-de83913ea805'>Query link</a>")
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
From the above graphs we notice that <br>
1. The number of NFTs sold in secondary marketplace were the highest in the 2nd and 3rd week of Novemeer. Primarily due to new pack launches and the hype aound Football. <br>
2. Surprisingly, Rare and epic cards are sold more than common cards. Well, maybe they are the only ones worth paying a hefty sum. <br>
3. The number of iconic NFTs sold are the least. Why ?, Bruh, only a few are there. But holy, they are the ones that make 35% of the volume. <br>
4. Epic and Rare NFTs account for 50+ % of the total volume<br>"""),unsafe_allow_html=True)
#######
c1,c2=st.columns((25,75))

####### Average amount spent on each collection 
t=mint_trends.groupby(by="RARITY",as_index=False).sum()
t['avg']=t['USD_AMOUNT']/t['NUMBER_OF_NFTS']

avg_spent_on_collection_fig=px.bar( \
       data_frame=t,
       x='RARITY',
       y="avg",
       color='RARITY',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Average cost of each rarity card"
      )
avg_spent_on_collection_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
avg_spent_on_collection_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/e2d37d47-4215-45b4-82cb-de83913ea805'>Query link</a>")
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


c1.write(grey_card(title='Observation',text='<br><br><br>Holy!!. Iconic cards completely destroys the other cards. An iconic card sells for an average of 1500$<br><br><br><br><br>'),unsafe_allow_html=True)















######################

##########
c1,c2=st.columns((40,60))
####### Distribution of event type
nft_minted_per_event_url="https://node-api.flipsidecrypto.com/api/v2/queries/cef335b4-74f4-49b3-bcae-41abd214908b/data/latest"
nft_minted_per_event=pd.read_json(nft_minted_per_event_url)

# nft_minted_per_event_fig=px.pie( \
#        data_frame=nft_minted_per_event,
#        names='EVENT_TYPE',
#        values="NUMBER_OF_NFTS",
#        color='EVENT_TYPE',\
#        color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
#        title="Distibution of NFTS"
#       )
nft_minted_per_event_fig=px.sunburst(nft_minted_per_event,path=['EVENT_TYPE','RARITY'],values='NUMBER_OF_NFTS',\
    color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']\
    ,title="Distibution of NFTS"
    )
nft_minted_per_event_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
nft_minted_per_event_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/cef335b4-74f4-49b3-bcae-41abd214908b'>Query link</a>")
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
c1.write(grey_card(title='Observation',text=""" \
    Goalazo, Gooooooooooal !! <br> 
    NFTs depicting goals are sold the highest. Especially the rare and epic goals are very likely to be sold. <br> 
    Additionally, Rare and epic saves are among the most sold. <br><br><br><br><br><br>"""),unsafe_allow_html=True)






###############
st.markdown("""
<div class="card text-white bg-warning mb-3" style="margin:1rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h3 class="card-title">Analysis of NFTs with respect to Host country </h3>
    <p class="card-text"></p>
  </div>
</div>"""
, unsafe_allow_html=True)
###############








###### number of nfts minted for every hosts
top_hosts_url = "https://node-api.flipsidecrypto.com/api/v2/queries/3522b05c-0362-4c6c-abe5-8a99971e9d9e/data/latest"
top_hosts = pd.read_json(top_hosts_url)
top_hosts['HOST']=top_hosts['HOST'].apply(lambda x:x.replace("‚",'').strip().split('/')[0])
top_hosts=top_hosts.groupby(by='HOST',as_index=False).sum()

top_hosts_fig=px.choropleth(top_hosts,locationmode='country names',locations='HOST',color='NUMBER_OF_NFTS_MINTED',color_continuous_scale='Viridis',scope='world',
title='Number of NFTs sold for each host country')
top_hosts_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/3522b05c-0362-4c6c-abe5-8a99971e9d9e'>Query link</a>")
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







###############
st.markdown("""
<div class="card text-white bg-warning mb-3" style="margin:1rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h3 class="card-title">Analysis of NFTs with respect to players and moments </h3>
    <p class="card-text"></p>
  </div>
</div>"""
, unsafe_allow_html=True)
###############

c1,c2=st.columns((30,70))



######### players with most NFT

top_player_nft_url = "https://node-api.flipsidecrypto.com/api/v2/queries/6f2d4ef2-0a6f-4c60-8d9f-402db6ea3505/data/latest"
top_player_nft = pd.read_json(top_player_nft_url)

top_player_nft_fig=px.bar( \
       data_frame=top_player_nft,
       x='PLAYER',
       y="USD",
    #    color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="Most valuable Players ($)",
       hover_data=['ERA','PLAYER','USD']
      )
top_player_nft_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
top_player_nft_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/6f2d4ef2-0a6f-4c60-8d9f-402db6ea3505'>Query link</a>")
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
c1.write(grey_card(title='Observation',text=""" \
    Ronaldo (el phenomeno), C. Ronaldo along with women superstar Carli Lloyd rule the secondary NFT marketplace. Those three together bought in a volume of 206k $. Huge. <br>
    Surprisingly, Lionel Messi is behind van persie and casillas. 
    Link to query for the below table [here](https://app.flipsidecrypto.com/velocity/queries/8eed772b-2e3c-4513-876d-ae98ab858e18)"""),unsafe_allow_html=True)


######### Top NFTs

top_nft_url = "https://node-api.flipsidecrypto.com/api/v2/queries/8eed772b-2e3c-4513-876d-ae98ab858e18/data/latest"
top_nft = pd.read_json(top_nft_url)
st.dataframe(top_nft,use_container_width=True)


##########
#########
###############
st.markdown("""
<div class="card text-white bg-warning mb-3" style="margin:1rem;">
  <div class="card-header"></div>
  <div class="card-body">
    <h3 class="card-title">Top cards in each collection </h3>
    <p class="card-text"></p>
  </div>
</div>"""
, unsafe_allow_html=True)
###############
######### Top cards in each collection 

top_cards_collection_url = "https://node-api.flipsidecrypto.com/api/v2/queries/6ff7960e-6dfc-45cb-b5d1-c073dfc37ebb/data/latest"
top_cards_collection = pd.read_json(top_cards_collection_url)

top_cards_collection_fig=px.bar( \
       data_frame=top_cards_collection,
       x=str('DESCRIPTION'),
       y="TOTAL_AMOUNT",
       color='DROP_NAME',\
       color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
       title="TOP VALUABLE CARDS ($)",
       hover_data=['DESCRIPTION','RARITY','DROP_NAME','NFT_ASSET_ID','TOTAL_AMOUNT']
      )
top_cards_collection_fig.update_layout({'plot_bgcolor': 'rgba(100, 0, 0, 0)','paper_bgcolor': 'rgba(85,85,85,255)',})
top_cards_collection_fig.add_annotation(
    text = (f"<a href='https://app.flipsidecrypto.com/velocity/queries/6ff7960e-6dfc-45cb-b5d1-c073dfc37ebb'>Query link</a>")
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
st.plotly_chart(top_cards_collection_fig, use_container_width=True)

