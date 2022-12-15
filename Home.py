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
st.markdown('# FIFA+ Collect marketplace')



st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',unsafe_allow_html=True)


st.markdown(
    """
    <div class="card text-white bg-primary mb-3" >
  <div class="card-header"></div>
  <div class="card-body">
    <h5 class="card-title">
    Introduction
    </h5>
    <p class="card-text"></p>
  </div>
  """, unsafe_allow_html=True)

def grey_card(header='',title='',text=''):
    return f"""
    <div class="card text-white bg-secondary mb-" style="margin:1rem;" >
    <div class="card-header">{header}</div>
    <div class="card-body">
    <h3 class="card-title">{title}</h3>
    <p class="card-text">{text}   
    """

st.markdown(grey_card(title='What Is Algorand? ',text=
"""

Algorand (ALGO) is both a digital currency and blockchain platform. The Algorand platform is designed to process many transactions quickly, similar to \
    major payment processors like Mastercard or Visa. In addition, Algorand can host other cryptocurrencies and blockchain-based projects, making it a \
    direct competitor to Ethereum. ALGO, the platform's native currency, is used to secure the Algorand blockchain and pay processing fees for Algorand-based \
    transactions. <br>
    Algorand is an open-source blockchain, meaning anyone can view and contribute to the platform's code. Algorand uses an operating protocol it calls \
    pure proof-of-stake (PoS), which recruits network validators from the pool of users.
"""
),unsafe_allow_html=True)

st.markdown(grey_card(title='What Is the FIFA? ', text=
"""

The FIFA World Cup, often simply called the World Cup, is an international association football competition contested by the senior men's and women's\
    national teams of the members of the Fédération Internationale de Football Association (FIFA), the sport's global governing body. \
    The tournament has been held every four years
"""
),unsafe_allow_html=True)

st.markdown(grey_card(title='What Is the FIFA+ collect? ', text=
"""

FIFA is launching a digital collectible platform later this month called FIFA+ Collect, which will allow fans to have blockchain ownership of iconic soccer \
    games along with men’s and women’s World Cup art and imagery. <br>
Powered by Algorand, FIFA+ Collect will be accessible on FIFA+, the mobile app that produces livestreams of matches, interactive games, news, tournament data \
     and original content. Users of FIFA+ Collect are asked to register on the FIFA+ app to gain information on the upcoming digital collectibles, with updates \
    to be provided as of now in English, French and Spanish.<br>
As recently as May, Algorand became FIFA’s official blockchain partner ahead of the 2022 FIFA World Cup Qatar. \
    Algorand is a carbon neutral tech company that is deployed by more than 2,000 global entities. In March, \
        it inked a three-year kit sponsorship with NJ/NY Gotham FC of the National Women’s Soccer League, enabling fans to use Algorand’s digital wallet to buy in-game NFTs, tickets and merchandise from the team.<br>

How do I get involved?

    Create your account and sign up to begin your FIFA+ Collect journey.

    Once you’ve selected your packs and scored your breathtaking moments, view and enjoy the collectibles you have landed, or trade and sell them on the designed FIFA+ Collect marketplace. 

    Compete with your collectibles in upcoming quests to win unforgettable rewards and grow your collection even more. 

"""
),unsafe_allow_html=True)

st.markdown(
    """
    <div class="card text-white bg-primary mb-3" >
  <div class="card-header"></div>
  <div class="card-body">
    <h5 class="card-title">
    Glossary
    </h5>
    <p class="card-text"></p>
  </div>
  """, unsafe_allow_html=True)
st.markdown(grey_card(title='Glossary', text=
"""
1. Drop_name : Fifa has released four different NFT collection. Genesis, Archives, Archives 2 and south america. These have been 'dropped' at different times. Hence we address them\
    as drops <br>
2. Rarity : FIFA has classifed the cards based on thier rarity (maybe based on how rare the ecent might occur again ?) These are classified as common, rare, epic and iconic with Iconic being the rarest of them all <br>
3. Pack : A set of 3 NFTs.  An user has to buy(mint) a pack of NFT. and each pack contains 3 unknown NFTs. <br>
4. FIFA+ COLLECT NFT Marketplace : A marketplace dedicated to selling/buying of FIFA NFTs on Algorand. <br>
5. Host country: The country that hosted the FIFA in that particular year. 2022 FIFA was hosted by Qatar.<br>
6. MVP (most valuable players) : Players whose total NFT sales value are among the top 10. <br>
7. Holding period : The time difference between buying and selling. The minimum time period is 14 days which is set into the smart contract by FIFA.
8. Profit : The amount of price difference between minting and selling an NFT.
9. New users : Users who made thier first transaction on Algorand. ( be it with traditional algorand application or FIFA)
10. Weekly active users : Users who have made transactions for atleast 3 days in a week. """
),unsafe_allow_html=True)

st.markdown(
    """
    <div class="card text-white bg-primary mb-3" >
  <div class="card-header"> Twitter </div>
  <div class="card-body">
    <h5 class="card-title">
    Twitter link : https://twitter.com/Sandesh_K_12/status/1603247772152393729?s=20&t=H_nMwprisl37SFJuNCCQFQ
    </h5>
    <p class="card-text"></p>
  </div>
  """, unsafe_allow_html=True)
