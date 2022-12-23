import schedule
import time as tm
from schedule import every, repeat
from datetime import time, timedelta, datetime


@repeat(every(5).seconds, message="Paul !!!")
@repeat(every(2).seconds, message="Rory !!!")
@repeat(every(7).seconds, message="Caitlin !!!")
def job(message):
    print(f"Hello ! ", message)


@repeat(every(30).minutes)
def break_reminder():
    print("You need to take a break now....")

# EXAMPLES......
# schedule.every(5).seconds.do(job)
# schedule.every().day.at("17:26").do(job)
# schedule.every().thursday.at("12:26").do(job)
# schedule.every().minute.at(":33").do(job)
# schedule.every().hour.until(time(23, 33, 44)).do(job)
# schedule.every().hour.until(timedelta(hours=8)).do(job)
# schedule.every(1).to(5).seconds.do(job)
# job = schedule.every(1).to(5).seconds.do(job)


while True:
    schedule.run_pending()
    tm.sleep(1)

