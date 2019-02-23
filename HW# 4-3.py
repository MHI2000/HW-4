import datetime
import time
def __init__(self, time, date, hour, minute):
    self.time = time
    self.date = date
    self.hour = hour
    self.minute = minute

    
time = datetime.datetime.now()
last_quarter_minute = 15*(time.minute//15)

current_time = time.strftime("%Y/%m/%d %H:%M")

print (last_quarter_minute)
print (current_time)
