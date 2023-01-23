
from datetime import date
import calendar

print(date.today())

c=calendar.TextCalendar(calendar.SUNDAY)
str=c.formatmonth(2023,1,1,1)
print(str)
