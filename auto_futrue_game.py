from  data_spider import DataSpider
from storedata import delete_files,store_approaching_game


ds = DataSpider()

ds.get_future_game_info_hupu()

store_approaching_game()