from asyncio import exceptions

from pytradegate import *
from time import sleep
from datetime import datetime
products = ['Oil 3X Daily', ' Oil 3x Short']
isin = ['IE00BMTM6B32','XS2819844387']


 # make a configured request. Provide a proper header
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
header = {'user-agent': user_agent}
request = Request(header=header)

# make the instrument you wish
oil_long = Instrument('IE00BMTM6B32', request)
oil_short = Instrument('XS2819844387', request)

short_open = 1
long_open = 1

short_entry = 1
long_entry = 1

short_qnty = 5000/short_open
long_qnty = 5000/long_open

def pl( l_bid, l_ask, s_bid, s_ask):
    pl_bid = short_qnty * (s_bid - short_entry) + long_qnty * (l_bid - long_entry)
    pl_ask = short_qnty * (s_ask - short_entry) + long_qnty * (l_ask - long_entry)
    return pl_bid, pl_ask


def initialis_instrument():
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    header = {'user-agent': user_agent}
    request = Request(header=header)

    # make the instrument you wish
    oil_long = Instrument('IE00BMTM6B32', request)
    oil_short = Instrument('XS2819844387', request)

while True:
    sleep(2)

    time_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    x = f"{time_str},{products[0]},{isin[0]},{oil_long.ask}, {oil_long.bid}, {oil_long.data} \n"
    y = f"{time_str},{products[1]},{isin[1]},{oil_short.ask}, {oil_short.bid}, {oil_short.data} \n"
    
    print(pl(oil_long.bid, oil_long.ask, oil_short.bid, oil_short.ask))

    date_str = datetime.now().strftime("%Y%m%d")
    with open(f"ticker_data_log/mats_logs_{date_str}.txt", "a") as file:
        file.write(x)
        file.write(y)
