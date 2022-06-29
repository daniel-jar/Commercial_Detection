from datetime import datetime
dateTimeObj = datetime.now()
time = dateTimeObj.strftime("%H:%M:%S.%f")
date = dateTimeObj.strftime("%d.%m.%Y")
print(date)
print(time)