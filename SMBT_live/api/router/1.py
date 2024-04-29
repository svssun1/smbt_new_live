from datetime import datetime
now=datetime.now()
print(now)
date_time = now.strftime("%m/%b/%Y%H:%M:%S")
print(type(date_time))
print(date_time)
timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)
date_time = date_time.strftime("%m/%b/%Y%H:%M:%S")
print(date_time)