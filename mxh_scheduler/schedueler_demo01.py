import datetime,time

import schedule

def myJob1():
    print(datetime.datetime.now())
    print("job1:我10s执行一次，每次执行3秒")
    time.sleep(3)
schedule.every(10).seconds.do(myJob1)

def myJob2():
    print(datetime.datetime.now())
    print('job2:一分钟执行一次，每次执行5秒')
    time.sleep(5)
schedule.every(1).minutes.do(myJob2)

def myJob3():
    print(datetime.datetime.now())
    print('job3: 我每天上午10点执行一次，每次执行10秒')
    time.sleep(10)
schedule.every().day.at('10:00').do(myJob3)

def myJob4():
    print(datetime.datetime.now())
    print('job4: 我每隔5到10s（具体时间随机）执行一次，每次执行3秒')
    time.sleep(3)
schedule.every(5).to(10).seconds.do(myJob4)

def myJob5():
    print(datetime.datetime.now())
    print('job5: 我每周一上午10:20执行一次，每次执行3秒')
    time.sleep(3)
schedule.every().monday.at('10:20').do(myJob5)

while True:
    schedule.run_pending()