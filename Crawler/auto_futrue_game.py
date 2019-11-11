from Crawler.data_spider import DataSpider
from Crawler.storedata import store_approaching_game,predrate


ds = DataSpider()

ds.get_future_game_info_hupu()

store_approaching_game()

predrate()
