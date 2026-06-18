from data.market_data_service import (
MarketDataService)

df = (

    MarketDataService
    .load_processed()

)

print(

    "Rows:",

    MarketDataService.candle_count(
        df
    )


)

print(

    "Latest Candle"

)

print(

    MarketDataService.latest_candle(
        df
    )


)
