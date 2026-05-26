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

short_open = 1.5272
long_open = 49.3

short_entry = short_open
long_entry = long_open

short_qnty = 5000/short_open
long_qnty = 5000/long_open

def pl( l_bid, l_ask, s_bid, s_ask):
    pl_bid = short_qnty * (s_bid - short_entry) + long_qnty * (l_bid - long_entry)
    pl_ask = short_qnty * (s_ask - short_entry) + long_qnty * (l_ask - long_entry)
    pl_long_bid_short_ask = short_qnty * (s_ask - short_entry) + long_qnty * (l_bid - long_entry)
    pl_long_ask_short_bid = short_qnty * (s_bid - short_entry) + long_qnty * (l_ask - long_entry)

    r3 = f"long_bid_short_ask {pl_long_bid_short_ask}"
    r4 = f"long_ask_short_bid {pl_long_ask_short_bid}"
    return pl_bid, pl_ask,r3,r4


def initialis_instrument():
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    header = {'user-agent': user_agent}
    request = Request(header=header)

    # make the instrument you wish
    oil_long = Instrument('IE00BMTM6B32', request)
    oil_short = Instrument('XS2819844387', request)

while True:
    sleep(5)


    try:
        time_str = datetime.now().strftime("%Y%m%d-%H%M%S")
        x = f"{time_str},{products[0]},{isin[0]},{oil_long.ask}, {oil_long.bid}, {oil_long.data} \n"
        y = f"{time_str},{products[1]},{isin[1]},{oil_short.ask}, {oil_short.bid}, {oil_short.data} \n"
        print(pl(float(oil_long.bid), float(oil_long.ask), float(oil_short.bid), float(oil_short.ask)))
        date_str = datetime.now().strftime("%Y%m%d")
        with open(f"ticker_data_log/mats_logs_{date_str}.txt", "a") as file:
            file.write(x)
            file.write(y)
    except:
        print("error")

