from pymongo import MongoClient

class DBManger:
    def __init__(self,futureName):
        '''Create Mongodb Connection'''
        self.__client = MongoClient('mongodb://localhost:27017/')
        self.__db = self.__client['FutureDatas']
        # print(self.__db.collection_names())
        self.__col_KDatas = self.__db[futureName]

    #添加数据,必须是字典形式，形如{'trader_id': 'xxx', 'trader_name': 'xxxx', 'password': 'xxxx', 'is_active': '1'}
    def add_kdata(self, data):
        print("数据为：",data,type(data))
        res = self.__col_KDatas.insert_one(data)
        return res

    #查询某个字段的数据
    def get_kdata(self,UpdateTime,HighestPrice,LowestPrice,_id ='_id'):
        res = self.__col_KDatas.find({},{UpdateTime:1,HighestPrice:1,LowestPrice:1,_id:0})
        return res


if __name__== "__main__":
    data1 = [{'AskVolume1': 88, 'AskVolume5': 0, 'BidPrice5': 1.7976931348623157e+308, 'UpperLimitPrice': 2759.0, 'LowestPrice': 2476.5, 'BidVolume5': 0, 'AskPrice4': 1.7976931348623157e+308, 'AskVolume4': 0, 'AskVolume3': 0, 'CurrDelta': 1.7976931348623157e+308, 'OpenInterest': 325016.0, 'AveragePrice': 250306.78677256388, 'PreDelta': 0.0, 'TradingDay': '20180824', 'SettlementPrice': 1.7976931348623157e+308, 'InstrumentID': 'j1901', 'BidVolume4': 0, 'AskPrice5': 1.7976931348623157e+308, 'ActionDay': '20180824', 'LowerLimitPrice': 2351.0, 'ClosePrice': 1.7976931348623157e+308, 'BidVolume2': 0, 'BidPrice3': 1.7976931348623157e+308, 'AskPrice3': 1.7976931348623157e+308, 'BidPrice1': 2509.5, 'ExchangeInstID': 'j1901', 'UpdateTime': '07:54:41', 'ExchangeID': 'DCE', 'HighestPrice': 2525.5, 'UpdateMillisec': 500, 'Turnover': 82445048200.0, 'LastPrice': 2510.0, 'AskPrice2': 1.7976931348623157e+308, 'BidVolume1': 4, 'AskVolume2': 0, 'OpenPrice': 2508.0, 'AskPrice1': 2510.5, 'Volume': 329376, 'BidPrice4': 1.7976931348623157e+308, 'PreClosePrice': 2504.5, 'BidPrice2': 1.7976931348623157e+308, 'PreOpenInterest': 372030.0, 'BidVolume3': 0, 'PreSettlementPrice': 2555.0}]
    db1 = DBManger('j1901')
    res = db1.add_kdata(data1)
    print(res)

    # res = db1.get_kdata('UpdateTime','HighestPrice','LowestPrice')
    # for each in res:
    #     print(each)