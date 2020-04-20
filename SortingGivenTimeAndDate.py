from datetime import date
from time import sleep
dates=[]
d1=date(2018,4,17)
d2=date(1995,11,17)
d3=date(1995,11,4)
dates.append(d1)
dates.append(d2)
dates.append(d3)
dates.sort()
sleep(5)
print(dates)
for d in dates:
    print(d)
    
