import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_prices_1 = pd.read_csv("training_data/prices_round_0_day_-1.csv", sep=";", index_col=False)
df_prices_2 = pd.read_csv("training_data/prices_round_0_day_-2.csv", sep=";", index_col=False)
df_prices = pd.concat([df_prices_1, df_prices_2], ignore_index=True)

df_trades_1 = pd.read_csv("training_data/trades_round_0_day_-1.csv", sep=";", index_col=False)
df_trades_2 = pd.read_csv("training_data/trades_round_0_day_-2.csv", sep=";", index_col=False)
df_trades = pd.concat([df_trades_1, df_trades_2], ignore_index=True)

df_t_prices = df_prices[df_prices["product"] == "TOMATOES"]
df_t_trades = df_trades[df_trades["symbol"] == "TOMATOES"]

df_e_prices = df_prices[df_prices["product"] == "EMERALDS"]
df_e_trades = df_trades[df_trades["symbol"] == "EMERALDS"]

avg_t_trade_price = np.mean(df_t_trades["price"])
avg_e_trade_price = np.mean(df_e_trades["price"])
std_t_trade_price = np.std(df_t_trades["price"])
std_e_trade_price = np.std(df_e_trades["price"])

print(avg_t_trade_price)
print(avg_e_trade_price)
print(std_t_trade_price)
print(std_e_trade_price)
print(len(df_e_trades))
print(len(df_t_trades))

