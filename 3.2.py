from _datetime import datetime, timedelta
import calendar

def prev_month(date):
    year = date.year
    month = date.month - 1
    if date.month == 1:
        year = date.year - 1
        month = 12
    return date - timedelta(days=calendar.monthrange(year, month)[1])

print('Yesterday was {}'.format((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')))
print('Tomorrow will be {}'.format((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')))
print('Month ago was {}'.format(prev_month(datetime.now()).strftime('%Y-%m-%d')))
dt = datetime.strptime('01/01/17 12:10:03.234567', '%d/%m/%y %H:%M:%S.%f')
