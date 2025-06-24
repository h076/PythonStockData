#!/usr/bin/env python3
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from numpy import empty

import keys as k
from datetime import datetime
import pandas as pd

def getStockPriceData(symbol : str, window : TimeFrame, start_time : datetime,
                      end_time : datetime, bar_limit : int) -> pd.DataFrame:

    keys = k.loadAlpacaKeys("/Users/harry/Documents/Python/alpacaTests/alpacaKey.txt")

    if not bool(keys):
        return pd.DataFrame()

    stock_client = StockHistoricalDataClient(keys["APCA-API-KEY-ID"], keys["APCA-API-SECRET-KEY"])

    request_params = StockBarsRequest(symbol_or_symbols=symbol,
                                      timeframe=window,
                                      start=start_time,
                                      end=end_time,
                                      limit=bar_limit)

    dataa = stock_client.get_stock_bars(request_params)

    print(dataa)
    return pd.DataFrame(dataa)
