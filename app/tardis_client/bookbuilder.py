import asyncio
import datetime
from app.tardis_client.tardis_feed import TardisFeed
from app.tardis_client.book import Book
from app.time import datetime_to_str


async def booksbuilder(markets, dates):
    orderbooks = {}
    for market in markets:
        for date in dates:
            start = date[0]
            end = date[1]
            if isinstance(start, datetime.datetime) and isinstance(
                end, datetime.datetime
            ):
                start = datetime_to_str(start)
                end = datetime_to_str(end)

            feed = TardisFeed(market.exchange, market, start, end, True, True)
            await feed.replay()

            orderbooks[market.market] = Book(
                market.exchange, market.market, start, end, feed.messages
            )
    return orderbooks


async def tradesbuilder(markets, dates):
    orderbooks = {}
    for market in markets:
        for date in dates:
            start = date[0]
            end = date[1]
            if isinstance(start, datetime.datetime) and isinstance(
                end, datetime.datetime
            ):
                start = datetime_to_str(start)
                end = datetime_to_str(end)
            feed = TardisFeed(market.exchange, market, start, end, True, True)
            await feed.replay()
            orderbooks[market.market] = Book(
                market.exchange, market.market, start, end, feed.messages
            )
    return orderbooks
