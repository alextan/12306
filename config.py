seat_edz = "ze_num"
seat_ydz = "zy_num"
seat_swz = "swz_num"
seat_yz = "yz_num"
seat_yw = "yw_num"
seat_rz = "rz_num"
seat_rw = "rw_num"
seat_wz = "wz_num"
train_no = "station_train_code"
class LeftTicket:
    def __init__(self,date,from_station,to_station):
        url = "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=" + date + "&from_station=" + from_station + "&to_station=" + to_station
        self.url = url
        self.json_format = "html['data']['datas']"
