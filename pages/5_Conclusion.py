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
    <h2 class="card-title">Conclusion</h2>
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
st.write(grey_card(title='Key Takeaways',text=""" \
    1. Genesis pack was the first pack to be released and accounts for almost 80% of the sales. And even today has the most amount of sales. <br>
    2. Curator Collection - South American Flair is the costliest NFT. <br>
    3. Iconic moments are rare. like very rare. But man, the probability that you get one is close to 0. The only silver lining of the high cost of south american flair pack is that you are more likely to get an Iconic card here than anywhere else. <br>
    4. The Epic and rare cards are more likely to be found in genesis collection. <br>
    6. In the secondary marketplace, Genesis cards are more pricier than the rest costing an average of 35 USD. <br>
    7. Rare and epic cards are sold more than common cards. <br>
    8. The number of iconic NFTs sold are the least. Why ?, Bruh, only a few are there. But holy, they are the ones that make 35% of the volume.<br>
    9. Epic and Rare NFTs account for 50+ % of the total volume. <br>
    10. NFTs depicting goals are sold the highest. Especially the rare and epic goals are very likely to be sold. <br>
    11. Initially when the marketplace launched, FIFA addresses accounted for 5 % of the new algorand users, however this has been on a decline since. with now only\
        0.05% of the new algorand users onboarding because of FIFA. <br>
    12. The number of weekly active users ( transacting more than twice in a week) has been a constant and hovers around 300 to 400 users. <br>"""),unsafe_allow_html=True)
