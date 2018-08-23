import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

# for day-of-week data
x = range(7)
y = np.zeros(7)
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# for month data
x_month = range(6)
y_month = np.zeros(6)
labels_month = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'] 
# other months were removed not because there are no incidents then
# but because they are not entered in the csv file


dayOfJuly = np.zeros(31)
labels_july = ["%d" % i for i in range(1, 32)]

# converts dates from Month DD, YYY
# to datetime format of YYYY,MM,DD
# and sums them up in array named 'y'
def dayofweek(df):
	for i, row in df.iterrows():
		date = row["Incident Date"]
		year_sep = date.split(',')
		date_sep = year_sep[0].split(' ')
		months = {
			"August": 8,
			"July": 7,
			"June": 6,
			"May": 5,
			"April": 4,
			"March": 3
		}

		month = months[date_sep[0].strip()]
		day = int(date_sep[1].strip())
		year = int(year_sep[1].strip())

		readable_date = dt.date(year, month, day)

		# 0 - Monday, 6 - Sunday
		# print(readable_date.weekday())
		y[readable_date.weekday()] += 1
		y_month[month-3] += 1
		if month == 7:
			dayOfJuly[day-1] += 1

def main():
	df = pd.read_csv("processed_injuries.csv")

	dayofweek(df)
	print("number of incidents each day of week:")
	print(y)
	plt.bar(x, y, width=0.5, color="blue", tick_label=labels)
	plt.show()

	print("number of incidents per month:")
	print(y_month)
	plt.bar(x_month, y_month, width=0.5, color="red", tick_label=labels_month)
	plt.show()
	
	print("number of incidents per day in july:")
	print(dayOfJuly)
	plt.bar(range(31), dayOfJuly, width=0.5, color="green", tick_label=labels_july)
	plt.show()

if __name__ == "__main__":
	main()

# the graph shows a spike of recorded cases
# on weekends, especially on Saturday
# as for months, a spike is evident in June and July
