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