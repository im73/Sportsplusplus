from  data_spider import DataSpider
from storedata import store_history_game,store_playing,delete_files


ds = DataSpider()

ds.get_playing_game_info_hupu()
store_playing()
delete_files()