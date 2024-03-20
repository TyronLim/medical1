from datetime import datetime
import time

now = datetime.today()

# start_day = datetime(now.year,now.month,now.day,now.hour,now.minute,now.second)
end_day = datetime(2024,6,24,00,00,00)

d_day = end_day - now
print(d_day)
print(d_day.days)



