from  data_spider import DataSpider
from storedata import store_history_game,store_playing,delete_files


ds = DataSpider()
try:
    ds.get_playing_game_info_hupu()
except:
    pass
store_playing()

