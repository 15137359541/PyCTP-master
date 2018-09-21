import datetime

def mnTime():
    #获取当前时间（小时分钟）
    now_time = int(datetime.datetime.now().strftime("%H%M"))

    print('现在时间：',now_time)
    if 900<=now_time<=1015 or 1030<=now_time<=1130 or 1330<=now_time<=1500 or 2100<=now_time<=2359 or 0<=now_time<=230:
        return True
    else:return False


mnTime()