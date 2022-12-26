import os
import sys
from btbinance import BinanceStore

path_head = os.path.abspath('..')
sys.path.append(path_head)
print(path_head)

from sunday.datawizard.secure import Secure
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

""" Decrypt key and secret """
secure_key = Secure()
__key, __secret = secure_key.get_key()


def main():
    store = BinanceStore(crrency="BNBBTC",
                         key=__key,
                         secret=__secret,
                         ),

    if __name__ == '__main__':
        main()
