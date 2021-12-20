from datetime import datetime, date


def getCurrentTime():
    cur_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    return cur_time


def getCurrentDate():
    cur_date = str(date.today().strftime("%B%d"))
    return cur_date
