import time,datetime
import schedule
import threading
from PyCTP_API import Trade1,Utils,Market1
from mxh_scheduler.Utils_datas import *
from mxh_scheduler import DBManage

class GetDataFromCtp():
    def __init__(self,InstrumentID):
       self.BrokerID = b'9999'
       self.UserID = b'123141'  # 063802
       self.Password = b'062929AAA'  # 123456
       self.ExchangeID = b'SHFE'
       self.listInstrumentID = [b'j1901', b'cu1612']
       #必须是字节形式，否则会报错
       self.InstrumentID = InstrumentID.encode('utf-8')
       self.trader = Trade1.PyCTP_Trader.CreateFtdcTraderApi(b'tmp/_tmp_t_')  # Trade实例
       self.market = Market1.PyCTP_Market.CreateFtdcMdApi(b'tmp/_tmp_m_')  # Market实例
       #连接交易前置
       self.trader.Connect(b'tcp://180.168.146.187:10000')
       self.market.Connect(b'tcp://180.168.146.187:10010')
       #交易账号登陆
       self.trader.Login(self.BrokerID, self.UserID, self.Password)
       self.market.Login(self.BrokerID, self.UserID, self.Password)
       print('交易日', Utils.code_transform(self.trader.GetTradingDay()))
       # print('查询行情', Utils.code_transform(self.trader.QryDepthMarketData(self.InstrumentID)))


    #判断交易日
    def mnTime(self):
        """
        周六周日不加入数据库
         0 : '星期一',
        1 : '星期二',
        2 : '星期三',
        3 : '星期四',
        4 : '星期五',
        5 : '星期六',
        6 : '星期天',
        :return:
        """
       # 获取当前时间（小时分钟）
        now_time = datetime.datetime.now().strftime("%H:%M:%S")
        week = datetime.datetime.now().weekday()
        if week in[5,6]:
            print("今天是星期",week+1)
            return False
        else:
            print("今天是星期", week + 1)
            print('现在时间：', now_time)
            print(datetime.datetime.now())
            if "09:00:00" <= now_time <= "10:15:00" or '10:30:00' <= now_time <= "11:30:00" or "13:30:00" <= now_time <= "15:00:00" or "21:00:00" <= now_time <= "23:59:59" or "00:00:00" <= now_time <= "02:30:00":
               return True
            else:
               return False

    def queryMarketDate(self):



        #判断是否可以在规定的时间段（查询数据，添加数据
        flag = self.mnTime()
        if flag:
            # 查询的行情数据,调用格式化函数
            k_data = put_Mongo(code_transform(self.trader.QryDepthMarketData(self.InstrumentID)))
            print(k_data,type(k_data))
            #将结果添加到数据库
            try:
                res = db01.add_kdata(k_data)
                print("添加数据成功")
            except Exception as e:
                print("错误为",e)
                print("添加数据失败")
        else:
            print('没有到时间段，不能添加数据')


    #schedule执行时，会有函数阻塞，所以使用多线程
    def thread_method(self):
        threading.Thread(target=self.queryMarketDate()).start()
    #每一秒执行一次查询
    def run(self):
        schedule.every(1).second.do(self.thread_method)

        while True:
            schedule.run_pending()


if __name__=="__main__":
    code = input('请数据查询的期货代码：')
    demo01 = GetDataFromCtp(code)
    db01 = DBManage.DBManger(code)
    demo01.run()
    # while True:
        # con = demo01.queryMarketDate()
        # for dict_one in con:
        #     # res = db01.add_kdata(dict_one)
        #     print('行情数据：',dict_one)
