from datetime import datetime
import time


for i in range(10):
    now = datetime.now()
    a= now.strftime('%Y-%m-%d  %H-%M-%S')
    print(a)
    time.sleep(1)