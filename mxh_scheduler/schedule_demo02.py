import datetime,time,threading
from apscheduler.schedulers.background import BackgroundScheduler

def job_func(text):
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
    time.sleep(5)
    print(text)

#schedule执行时，会有函数阻塞，所以使用多线程
def thread_method(text):
    text = [text]
    threading.Thread(target=job_func,args=text).start()

scheduler = BackgroundScheduler()
# 每隔两分钟执行一次 job_func 方法
scheduler.add_job(thread_method, 'interval', seconds=2,args=['第一种方式调度'])
# 在 2017-12-13 14:00:01 ~ 2017-12-13 14:00:10 之间, 每隔两分钟执行一次 job_func 方法
# scheduler.add_job(job_func, 'interval', seconds=2, start_date='2018-8-24 17:11:01' , end_date='2018-8-24 17:12:01' ,args=['第erer种方式调度'])

scheduler.start()
while True:
    time.sleep(1)

