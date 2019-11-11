from Crawler.data_spider import DataSpider
from Crawler.storedata import store_history_game,delete_files


ds = DataSpider()

ds.get_history_games_info_hupu()
store_history_game()
delete_files()
