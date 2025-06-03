import calendar
import locale

locale.setlocale(locale.LC_ALL, '')
print(calendar.calendar(2025))
#print(calendar.month(2025,5))
#print(calendar.monthrange(2025,5)) #para vê o ultimo dia do mês

print(locale.getlocale())
