# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 00:31:14 2016

@author: Zhuolin
"""

import sys
import time
import os
import threading
import chardet
import pandas as pd
from pandas import Series, DataFrame
import FunctionLog
# from PyCTP_API import FunctionLog
# from PyCTP_API.Trade import PyCTP_Trader
from Trade import PyCTP_Trader
# from PyCTP_API.Market import PyCTP_Market
from Market import PyCTP_Market
#
import Utils
# from PyCTP_API import Utils


def __main__():
    BrokerID = b'9999'
    UserID = b'123141'  # 063802
    Password = b'062929AAA'  # 123456
    ExchangeID = b'SHFE'
    listInstrumentID = [b'j1901', b'cu1612']
    InstrumentID = b'ag1905'
    trader = PyCTP_Trader.CreateFtdcTraderApi(b'tmp/_tmp_t_')  # Trade实例
    market = PyCTP_Market.CreateFtdcMdApi(b'tmp/_tmp_m_')  # Market实例
    print('连接交易前置', Utils.code_transform(trader.Connect(b'tcp://180.168.146.187:10000')))
    print('连接行情前置', Utils.code_transform(market.Connect(b'tcp://180.168.146.187:10010')))
    print('交易账号登陆', Utils.code_transform(trader.Login(BrokerID, UserID, Password)))
    print('交易账号登陆', Utils.code_transform(market.Login(BrokerID, UserID, Password)))
    print('交易日', Utils.code_transform(trader.GetTradingDay()))
    print('设置投资者代码', Utils.code_transform(trader.setInvestorID(UserID)))
    # time.sleep(1.0)
    # print('查询交易所', Utils.code_transform(trader.QryExchange()))
    # time.sleep(1.0)
    # print('查询投资者', Utils.code_transform(trader.QryInvestor()))
    # time.sleep(1.0)
    # print('查询资金账户', Utils.code_transform(trader.QryTradingAccount()))
    # time.sleep(1.0)
    # print('查询合约', Utils.code_transform(trader.QryInstrument(b'SHFE')))
    # time.sleep(1.0)
    # dfInstrument.to_csv('data/dfInstrument.csv')
    # time.sleep(1.0)
    # print('查询交易代码', Utils.code_transform(trader.QryTradingCode(ExchangeID)))
    # time.sleep(1.0)
    # print('合约手续费率', Utils.code_transform(trader.QryInstrumentCommissionRate(InstrumentID)))
    # time.sleep(1.0)
    # print('合约保证金率', Utils.code_transform(trader.QryInstrumentMarginRate(InstrumentID)))
    # time.sleep(1.0)
    # print('查询报单', Utils.code_transform(trader.QryOrder()))
    # time.sleep(1.0)
    # print('查询成交单', Utils.code_transform(trader.QryTrade()))
    # time.sleep(1.0)
    # print('投资者持仓', Utils.code_transform(trader.QryInvestorPosition()))
    time.sleep(1.0)
    print('查询行情', Utils.code_transform(trader.QryDepthMarketData(InstrumentID)))
    time.sleep(1.0)
    print('订阅行情', Utils.code_transform(market.SubMarketData(listInstrumentID)))
    try:
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        pass



if __name__ == '__main__':
    __main__()

