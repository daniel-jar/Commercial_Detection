from datetime import datetime



def time():
    dateTimeObj = datetime.now()
    time = dateTimeObj.strftime("%H:%M")
    return time

def day():
    dateTimeObj = datetime.now()
    return dateTimeObj.weekday()
