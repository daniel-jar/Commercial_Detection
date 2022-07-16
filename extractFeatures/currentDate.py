from datetime import datetime



def time():
    dateTimeObj = datetime.now()
    time = dateTimeObj.strftime("%H:%M")
    return time

def day():
    dateTimeObj = datetime.now()
    return dateTimeObj.weekday()

def run():
    dateTimeObj = datetime.now()
    return dateTimeObj.strftime("%D_%m_%Y_%H%M").replace("/","_")