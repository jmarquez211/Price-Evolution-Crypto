import yfinance as yf
import streamlit as st
#from PIL import Image   #if anyone wants to use images from another links
#from urllib.request import urlopen



# titles

st.title("Daily prices of cryptocurrency selected")

# list of cryptocurrencies I like the most, one can select others

Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Polygon = 'MATIC-USD'
Cardano = 'ADA-USD'
Solana = 'SOL-USD'
Polkadot = 'DOT-USD'
Shiba = 'SHIB-USD'
Avalanche = 'AVAX-USD'
Monero = 'XMR-USD'
Cosmos = 'ATOM-USD'

# access data from yahoo finance

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
MATIC_Data = yf.Ticker(Polygon)
ADA_Data = yf.Ticker(Cardano)
SOL_Data = yf.Ticker(Solana)
DOT_Data = yf.Ticker(Polkadot)
SHIB_Data = yf.Ticker(Shiba)
AVAX_Data = yf.Ticker(Avalanche)
XMR_Data = yf.Ticker(Monero)
ATOM_Data = yf.Ticker(Cosmos)


#Fetch history data from yahoo finance

BTCHist = BTC_Data.history(period="max")
ETHHist = ETH_Data.history(period="max")
MATICHist = MATIC_Data.history(period="max")
ADAHist = ADA_Data.history(period="max")
SOLHist = SOL_Data.history(period="max")
DOTHist = DOT_Data.history(period="max")
SHIBHist = SHIB_Data.history(period="max")
AVAXHist = AVAX_Data.history(period="max")
XMRHist = XMR_Data.history(period="max")
ATOMHist = ATOM_Data.history(period="max")


# crypto data for the dataframe
# it's easy to select other dates you wish to use, here is where I started to do this project

BTC = yf.download(Bitcoin, start="2023-8-20",end="2023-8-24")
ETH = yf.download(Ethereum, start="2023-08-24",end="2023-08-24")
ADA = yf.download(Cardano, start="2023-08-24",end="2023-08-24")
SOL = yf.download(Solana, start="2023-08-24",end="2023-08-24")
DOT = yf.download(Polkadot, start="2023-08-24",end="2023-08-24")
SHIB = yf.download(Shiba, start="2023-08-24",end="2023-08-24")
AVAX = yf.download(Avalanche, start="2023-08-24",end="2023-08-24")
XMR = yf.download(Monero, start="2023-08-24",end="2023-08-24")
ATOM = yf.download(Cosmos, start="2023-08-24",end="2023-08-24")

### only a pic to show


st.write("CoinMarketCap ($)")
st.image('coinmarket.jpg',use_column_width=True)



import pandas as pd
import plotly.graph_objects as go

# list of crypto available
cryptos = [
    ("Bitcoin", Bitcoin),
    ("Ethereum", Ethereum),
    ("Cardano", Cardano),
    ("Solana", Solana),
    ("Polygon", Polygon),
    ("Polkadot", Polkadot),
    ("Shiba Inu", Shiba),
    ("Avalanche", Avalanche),
    ("Monero", Monero),
    ("Cosmos", Cosmos),
    # more crypto here
]

# Widget for the user to select the crypto
selected_crypto = st.selectbox("Select the crypto", [crypto[0] for crypto in cryptos])

# Obtain the symbol of the crypto
selected_crypto_symbol = [crypto[1] for crypto in cryptos if crypto[0] == selected_crypto][0]

# Widget for selecting dates
start_date = st.date_input("Select the start date", pd.to_datetime("2023-01-01"))
end_date = st.date_input("Select the end date", pd.to_datetime("2023-08-24"))

# get the data from the crypto selected
crypto_data = yf.download(selected_crypto_symbol, start=start_date, end=end_date)

# showing the dataframe
st.write(f"{selected_crypto} Prices ($)")
st.table(crypto_data)

# showing an interactive graph for the crypto and its price evolution
fig = go.Figure(data=[go.Candlestick(x=crypto_data.index,
                open=crypto_data['Open'],
                high=crypto_data['High'],
                low=crypto_data['Low'],
                close=crypto_data['Close'])])
fig.update_layout(title=f"Graph evolution prices of {selected_crypto}",
                  xaxis_title='Fecha',
                  yaxis_title='Precio',
                  xaxis_rangeslider_visible=False,
                  height=600,
                  width=800)
st.plotly_chart(fig)

