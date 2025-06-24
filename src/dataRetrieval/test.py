#!/usr/bin/env python3
from alpaca.data.timeframe import TimeFrameUnit, TimeFrame
from datetime import datetime
from stockDataRequests import getStockPriceData
import pandas as pd

def main():
    symbol = "AAPL"
    window = TimeFrame(amount = 1, unit = TimeFrameUnit.Hour)
    start = datetime(2024, 2, 23, 13, 30, 0)
    end = datetime(2024, 2, 23, 23, 30, 0)
    limit = 100

    data = getStockPriceData(symbol, window, start, end, limit)

    print(data)

if __name__ == "__main__":
    main()
