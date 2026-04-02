from datamodel import Listing, OrderDepth, Trade, TradingState
from Trader import Trader

if __name__ == "__main__":

    timestamp = 1000

    listings = {
        "TOMATOES": Listing(
            symbol="TOMATOES", 
            product="TOMATOES", 
            denomination= "XIRECS"
        ),
        "EMERALDS": Listing(
            symbol="EMERALDS", 
            product="EMERALDS", 
            denomination= "XIRECS"
        ),
    }

    order_depths = {
        "TOMATOES": OrderDepth(
            buy_orders={10: 7, 9: 5, 10:3, 9:8, 5:25, 3:2,1:19, 98:14, 65:4, 56:99},
            sell_orders={11: -4, 12: -8, 5: -7, 90: -1, 10:4, 9:1, 25:5}
        ),
        "EMERALDS": OrderDepth(
            buy_orders={142: 3, 141: 5},
            sell_orders={144: -5, 145: -8}
        ),	
    }

    own_trades = {
        "TOMATOES": [
            Trade(
                symbol="TOMATOES",
                price=11,
                quantity=4,
                buyer="SUBMISSION",
                seller="",
                timestamp=1000
            ),
            Trade(
                symbol="TOMATOES",
                price=12,
                quantity=3,
                buyer="SUBMISSION",
                seller="",
                timestamp=1000
            )
        ],
        "EMERALDS": [
            Trade(
                symbol="EMERALDS",
                price=143,
                quantity=2,
                buyer="",
                seller="SUBMISSION",
                timestamp=1000
            ),
        ]
    }

    market_trades = {
        "TOMATOES": [
            Trade(
                symbol="TOMATOES",
                price=11,
                quantity=4,
                buyer="",
                seller="",
                timestamp=900
            )
        ],
        "EMERALDS": []
    }

    position = {
        "TOMATOES": 3,
        "EMERALDS": -5
    }

    observations = {}
    traderData = ""

    state = TradingState(
        traderData,
        timestamp,
        listings,
        order_depths,
        own_trades,
        market_trades,
        position,
        observations
    )
    trader = Trader()
    trader.run(state)