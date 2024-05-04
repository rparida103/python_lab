from datetime import datetime, timedelta
from pytz import timezone

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(get_previous_byday('Monday'))

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

#A major use of pytz is in localizing simple dates created with the datetime
d = datetime(2012, 12, 21, 9, 30, 0)
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

#Once the date has been localized, it can be converted to other time zones.
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

#Normalize can be used to handle daylight changes.
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)
