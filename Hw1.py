# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106060024.csv'
data = []
header = []
list_wdsd = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))


def FindRange(station_id) :
   target_data = list(filter(lambda item: item['station_id'] == station_id, data))
   for i in target_data : 
      if(i['WDSD'] != -99.000 and i['WDSD'] != -99.000) :
         list_wdsd.append(i['WDSD'])
   # print(list_wdsd)
   max_wdsd = -10000
   min_wdsd = 10000
   for wdsd_iter in list_wdsd :
      wdsd_iter = float(wdsd_iter)
      if wdsd_iter > max_wdsd :
         max_wdsd = wdsd_iter
      if wdsd_iter < min_wdsd :
         min_wdsd = wdsd_iter
   # print(max_wdsd)
   # print(min_wdsd)
   max_range = max_wdsd - min_wdsd
   print("['" +  station_id + "'," + str(max_range) + "]", end = '')

   # print(max_range)


#=======================================

# Part. 4
#=======================================
print('[', end = '')
FindRange('C0A880')
print(',', end = '')
FindRange('C0F9A0')
print(',', end = '')
FindRange('C0G640')
print(',', end = '')
FindRange('C0R190')
print(',', end = '')
FindRange('C0X260')
print(']', end = '')
#========================================