import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

# number of gun laws
x = np.zeros(50)
# number of deaths
y = np.zeros(50)

def main():
	df_laws = pd.read_csv("gun_laws_per_state.csv")
	df_deaths = pd.read_csv("processed_deaths.csv")

	for i, row in df_laws.iterrows():
		subsamples = df_deaths.loc[df_deaths['State'] == row['State']]
		total_deaths = np.sum(subsamples['# Killed'])

		x[i] = df_laws.get_value(i, '# Laws')
		y[i] = total_deaths

	plt.scatter(x, y, color="blue")
	plt.show()

if __name__ == "__main__":
	main()

# countries with a greater number of gun laws 
# don't have a high number of deaths, 
# all of them below or around average
# however, the results do not appear conclusive