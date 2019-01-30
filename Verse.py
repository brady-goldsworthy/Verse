from datetime import date
from dateutil.relativedelta import relativedelta

#Compare amount of weekend days certain dates will have in the future

today = date.today()

print("Todays date: ", today)

TOTAL_YEARS = 100 #Amount of future years to consider
year_counter = 0

weekend_counter = 0 #Counter of how many weekend days chosen date will have in next YEARS amount of years

date1 = date(today.year, 12, 5)
date1weekenddays = 0

date2 = date(today.year, 12, 15)
date2weekenddays = 0

print("Date1:", date1)
print("Date2:", date2)

while year_counter < TOTAL_YEARS :
	year_counter += 1

	if date1.weekday() > 3 :
		date1weekenddays += 1
		
	if date2.weekday() > 3 :
		date2weekenddays += 1

	date1 = date1 + relativedelta(years=+1)
	date2 = date2 + relativedelta(years=+1)

	if year_counter % 20 == 0:
		print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("December 5th has", date1weekenddays, "weekend days in the next", year_counter, "years.")
		print("December 12th has", date2weekenddays, "weekend days in the next", year_counter, "years.")

	