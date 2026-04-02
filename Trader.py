from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import numpy as np
import string

STD_T_TRADE_PRICE = 21.117578935455207
STD_E_TRADE_PRICE = 7.886405278701014

class Trader:

    def bid(self):
        return 15

    def scaled_sigmoid(self,c,k,x):
        return c/(1+np.exp(-x)) + k
    
    def run(self, state: TradingState):
        """Only method required. It takes all buy and sell orders for all
        symbols as an input, and outputs a list of orders to be sent."""

        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

        # Orders to be placed on exchange matching engine
        result = {}
        for product in state.order_depths:
            print(product)
            order_depth: OrderDepth = state.order_depths[product]
            orders: List[Order] = []

            if len(order_depth.sell_orders) != 0:
                best_ask = min(list(order_depth.sell_orders.keys()))
    
            if len(order_depth.buy_orders) != 0:
                best_bid = max(list(order_depth.buy_orders.keys()))

            mid_price = (best_bid + best_ask) / 2

            buy_volume = sum(order_depth.buy_orders.values())
            sell_volume = -sum(order_depth.sell_orders.values())

            imbalance = (buy_volume - sell_volume) / (buy_volume + sell_volume)

            if product == "TOMATOES":
                std_price = STD_T_TRADE_PRICE
            else: 
                std_price = STD_E_TRADE_PRICE

            std_avg_ratio = std_price/mid_price
            weight = self.scaled_sigmoid(2*std_avg_ratio, 1-std_avg_ratio, imbalance) # No lo usamos ahora

            acceptable_price = acceptable_price = mid_price + std_price * imbalance
            print(f"Mid price: {mid_price}")
            print(f"Std price: {std_price}")
            print(f"Raw weight:{imbalance}")
            print(f"Weight: {weight}")
            print("Acceptable price : " + str(acceptable_price))
            print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))

            if len(order_depth.sell_orders) != 0:
                best_ask_amount = order_depth.sell_orders[min(list(order_depth.sell_orders.keys()))]
                if int(best_ask) < acceptable_price:
                    print("BUY", str(-best_ask_amount) + "x", best_ask)
                    orders.append(Order(product, best_ask, -best_ask_amount))
    
            if len(order_depth.buy_orders) != 0:
                best_bid_amount = order_depth.buy_orders[max(list(order_depth.buy_orders.keys()))]
                if int(best_bid) > acceptable_price:
                    print("SELL", str(best_bid_amount) + "x", best_bid)
                    orders.append(Order(product, best_bid, -best_bid_amount))
            
            result[product] = orders
    
        # String value holding Trader state data required. 
        # It will be delivered as TradingState.traderData on next execution.
        traderData = "SAMPLE" 
        
        # Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData
    
