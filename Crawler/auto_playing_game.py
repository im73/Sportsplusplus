from Crawler.data_spider import DataSpider
from Crawler.storedata import store_playing

ds = DataSpider()
try:
    ds.get_playing_game_info_hupu()
except:
    pass
store_playing()

