
from collectionpy.date import RelativeDate
from datetime import datetime 

data = datetime(2024, 1, 5, 7, 55, 33)
segunda_data = datetime(2025, 9, 2, 7, 55, 33)

rd = RelativeDate()
print(rd.datetime)

rd.add(month=-1)

print(rd.datetime)
print(rd.dateDiff(segunda_data, 'month'))
print(rd.lastDay())
print(rd.lastDate())
print(rd.getUtilDay(7, [1, 2]))

