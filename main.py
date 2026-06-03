from asyncio import exceptions

from pytradegate import *
from time import sleep
import time
from datetime import datetime
import requests



def telegram_notify(message):
    try:
        TOKEN = "8949063853:AAFJXdL8r2fvn8gXVWsH4vBYPdCyF-orYg0"
        CHAT_ID = "8021938059"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        requests.post(
            url,
            json={
                "chat_id": CHAT_ID,
                "text": message
            }
        )
    except:
        print("error")





products = ['Oil 3X Daily', ' Oil 3x Short','Silver 3X Daily',' Silver 3x Short']
isin = ['IE00BMTM6B32','XS2819844387','XS3306516876','XS3306517924']


 # make a configured request. Provide a proper header
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
header = {'user-agent': user_agent}
request = Request(header=header)

# make the instrument you wish
oil_long = Instrument('IE00BMTM6B32', request)
oil_short = Instrument('XS2819844387', request)

silver_long = Instrument('IE00BMTM6B32', request)
silver_short = Instrument('XS2819844387', request)


oil_short_open = 1.5468
oil_long_open = 46.52

oil_short_entry = oil_short_open
oil_long_entry = oil_long_open

oil_short_qnty = 5000/oil_short_open
oil_long_qnty = 5000/oil_long_open

oil_bought_ind = False
oil_note_ts = 0

silver_short_open = 1.22
silver_long_open = 48.662

silver_short_entry = silver_short_open
silver_long_entry = silver_long_open

silver_short_qnty = 5000/silver_short_open
silver_long_qnty = 5000/silver_long_open



def pl_oil( l_bid, l_ask, s_bid, s_ask):
    pl_bid = oil_short_qnty * (s_bid - oil_short_entry) + oil_long_qnty * (l_bid - oil_long_entry)
    pl_ask = oil_short_qnty * (s_ask - oil_short_entry) + oil_long_qnty * (l_ask - oil_long_entry)
    pl_long_bid_short_ask = oil_short_qnty * (s_ask - oil_short_entry) + oil_long_qnty * (l_bid - oil_long_entry)
    pl_long_ask_short_bid = oil_short_qnty * (s_bid - oil_short_entry) + oil_long_qnty * (l_ask - oil_long_entry)

    r3 = f"oil_long_bid_short_ask {pl_long_bid_short_ask}"
    r4 = f"oil_long_ask_short_bid {pl_long_ask_short_bid}"
    return pl_bid, pl_ask,r3,r4


def pl_silver( l_bid, l_ask, s_bid, s_ask):
    pl_bid = silver_short_qnty * (s_bid - silver_short_entry) + silver_long_qnty * (l_bid - silver_long_entry)
    pl_ask = silver_short_qnty * (s_ask - silver_short_entry) + silver_long_qnty * (l_ask - silver_long_entry)
    pl_long_bid_short_ask = silver_short_qnty * (s_ask - silver_short_entry) + silver_long_qnty * (l_bid - silver_long_entry)
    pl_long_ask_short_bid = silver_short_qnty * (s_bid - silver_short_entry) + silver_long_qnty * (l_ask - silver_long_entry)

    r3 = f"silver_long_bid_short_ask {pl_long_bid_short_ask}"
    r4 = f"silver_long_ask_short_bid {pl_long_ask_short_bid}"
    return pl_bid, pl_ask,r3,r4



while True:
    sleep(5)


    try:
        time_str = datetime.now().strftime("%Y%m%d-%H%M%S")
        x = f"{time_str},{products[0]},{isin[0]},{oil_long.ask}, {oil_long.bid}, {oil_long.data} \n"
        y = f"{time_str},{products[1]},{isin[1]},{oil_short.ask}, {oil_short.bid}, {oil_short.data} \n"
        print(f"OIL:{pl_oil(float(oil_long.bid), float(oil_long.ask), float(oil_short.bid), float(oil_short.ask))} \t SILVER: {pl_silver(float(silver_long.bid), float(silver_long.ask), float(silver_short.bid), float(silver_short.ask))}")
        date_str = datetime.now().strftime("%Y%m%d")
        with open(f"ticker_data_log/wti_oil/mats_logs_{date_str}.txt", "a") as file:
            file.write(x)
            file.write(y)
        z = f"{time_str},{products[2]},{isin[2]},{silver_long.ask}, {silver_long.bid}, {silver_long.data} \n"
        v = f"{time_str},{products[3]},{isin[3]},{silver_short.ask}, {silver_short.bid}, {silver_short.data} \n"
        date_str = datetime.now().strftime("%Y%m%d")
        with open(f"ticker_data_log/wti_silver/mats_logs_{date_str}.txt", "a") as file:
            file.write(z)
            file.write(v)
        if pl_oil(float(oil_long.bid), float(oil_long.ask), float(oil_short.bid), float(oil_short.ask))[1] > 30 and oil_bought_ind is True and time.time() - oil_note_ts > 300:
            telegram_notify(f"SELL OIL AT {datetime.now()}: {pl_oil(float(oil_long.bid), float(oil_long.ask), float(oil_short.bid), float(oil_short.ask))}")
            oil_note_ts = time.time()

    except:
        print("error")

