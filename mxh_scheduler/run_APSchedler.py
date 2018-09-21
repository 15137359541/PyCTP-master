import time, datetime
import schedule
import threading
from PyCTP_API import Trade1, Utils, Market1
from mxh_scheduler import DBManage
from apscheduler.schedulers.background import BackgroundScheduler


class GetDataFromCtp():
    def __init__(self, InstrumentID):
        self.BrokerID = b'9999'
        self.UserID = b'123141'  # 063802
        self.Password = b'062929AAA'  # 123456
        self.ExchangeID = b'SHFE'
        self.listInstrumentID = [b'j1901', b'cu1612']
        # 必须是字节形式，否则会报错
        self.InstrumentID = InstrumentID.encode('utf-8')
        self.trader = Trade1.PyCTP_Trader.CreateFtdcTraderApi(b'tmp/_tmp_t_')  # Trade实例
        self.market = Market1.PyCTP_Market.CreateFtdcMdApi(b'tmp/_tmp_m_')  # Market实例
        # 连接交易前置
        self.trader.Connect(b'tcp://180.168.146.187:10000')
        self.market.Connect(b'tcp://180.168.146.187:10010')
        # 交易账号登陆
        self.trader.Login(self.BrokerID, self.UserID, self.Password)
        self.market.Login(self.BrokerID, self.UserID, self.Password)
        print('交易日', Utils.code_transform(self.trader.GetTradingDay()))
        # print('查询行情', Utils.code_transform(self.trader.QryDepthMarketData(self.InstrumentID)))

    def queryMarketDate(self):

        # 查询的行情数据
        k_data = Utils.code_transform(self.trader.QryDepthMarketData(self.InstrumentID))

        # 将结果添加到数据库
        print(datetime.datetime.now())
        for dict_one in k_data:
            try:
                res = db01.add_kdata(dict_one)
                print("添加数据成功")
            except Exception as e:
                print("错误为", e)
                print("添加数据失败")

    # schedule执行时，会有函数阻塞，所以使用多线程
    def thread_method(self):
        threading.Thread(target=self.queryMarketDate()).start()

    # 每一秒执行一次查询
    def run(self):
        #在start-end之间，每周一到周五
        scheduler.add_job(self.thread_method, 'interval',seconds=1,start_date ='2018-8-24 09:00:00' , end_date='2018-9-24 15:00:01' )
        scheduler.start()
        while True:
            time.sleep(1)


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    code = input('请数据查询的期货代码：')
    demo01 = GetDataFromCtp(code)
    db01 = DBManage.DBManger(code)
    demo01.run()
    # while True:
    # con = demo01.queryMarketDate()
    # for dict_one in con:
    #     # res = db01.add_kdata(dict_one)
    #     print('行情数据：',dict_one)
