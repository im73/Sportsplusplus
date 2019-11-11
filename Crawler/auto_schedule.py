from Crawler.data_spider import DataSpider
from Crawler.storedata import store_schedule,updatetoken

updatetoken()
ds = DataSpider()
ds.get_team_schedule_hupu()
store_schedule()
