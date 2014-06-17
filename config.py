leftticket_queue = []
seats = {
            'edz': "ze_num",
            'ydz': "zy_num",
            'swz': "swz_num",
            'yz' : "yz_num",
            'yw' : "yw_num",
            'rz' : "rz_num",
            'rw' : "rw_num",
            'wz' : "wz_num"
}
train_no = "station_train_code"
class LeftTicketConfig:
    def __init__(self,date,from_station,to_station):
        url = "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=" + date + "&from_station=" + from_station + "&to_station=" + to_station
        self.url = url
        self.json_format = "html['data']['datas']"
