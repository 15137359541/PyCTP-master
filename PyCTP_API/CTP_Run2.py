import time
from PyCTP_API import Trade1,Utils,Market1

class GetDataFromCtp():
    def __init__(self,InstrumentID):
       self.BrokerID = b'9999'
       self.UserID = b'123141'  # 063802
       self.Password = b'062929AAA'  # 123456
       self.ExchangeID = b'SHFE'
       self.listInstrumentID = [b'j1901', b'cu1612']
       self.InstrumentID = InstrumentID
       self.trader = Trade1.PyCTP_Trader.CreateFtdcTraderApi(b'tmp/_tmp_t_')  # Trade实例
       self.market = Market1.PyCTP_Market.CreateFtdcMdApi(b'tmp/_tmp_m_')  # Market实例
       #连接交易前置
       self.trader.Connect(b'tcp://180.168.146.187:10000')
       self.market.Connect(b'tcp://180.168.146.187:10010')
       #交易账号登陆
       self.trader.Login(self.BrokerID, self.UserID, self.Password)
       self.market.Login(self.BrokerID, self.UserID, self.Password)
       print('交易日', Utils.code_transform(self.trader.GetTradingDay()))
       print('查询行情', Utils.code_transform(self.trader.QryDepthMarketData(InstrumentID)))

    def queryMarketDate(self):

        time.sleep(1.0)
        #查询的行情数据
        return Utils.code_transform(self.trader.QryDepthMarketData(self.InstrumentID))

if __name__=="__main__":
    code = input('请数据查询的期货代码：')
    demo01 = GetDataFromCtp(code)
    # con = demo01.queryMarketDate()
    # print('行情数据：',con)