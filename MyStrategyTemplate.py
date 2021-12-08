# --- Do not remove these libs ---
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame

from freqtrade.strategy import (BooleanParameter, CategoricalParameter, DecimalParameter,IStrategy, IntParameter)

# --- Add your lib to import here ---
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib

# --- Generic strategy settings ---

class MyStrategyTemplate(IStrategy):
    INTERFACE_VERSION = 2
    
    # Determine timeframe and # of candles before strategysignals becomes valid
    timeframe = '5m'
    startup_candle_count: int = 30

    # Determine roi take profit and stop loss points
    minimal_roi = {"0": 0.99}
    stoploss = -0.10
    trailing_stop = False
    use_sell_signal = True
    sell_profit_only = False
    sell_profit_offset = 0.0
    ignore_roi_if_buy_signal = False

# --- Plotting ---

    # Use this section if you want to plot the indicators on a chart after backtesting
    plot_config = {
        'main_plot': {
            'SMA': {'color': 'blue'},
        },
        'subplots': {
            "RSI": {
                'rsi': {'color': 'red'},
            }
        }
    }

# --- Used indicators of strategy code ----

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Populate this section with the indicators you want to use in your strategy


        return dataframe

# --- Buy settings ---

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Enter the conditions for buying
        dataframe.loc[
            (


            ),
            'buy'] = 1

        return dataframe

# --- Sell settings ---

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Enter the conditions for selling (besides ROI TP if available)
        dataframe.loc[
            (


            ),
            'sell'] = 1
        return dataframe
