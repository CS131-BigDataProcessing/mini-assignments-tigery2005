import pandas as pd
import os

curr_dir = os.path.dirname(__file__)
file_path = os.path.join(curr_dir, 'Crime_Data_from_2020_to_Present.csv')

data = pd.read_csv(file_path)

column_index = 11
if column_index < len(data.columns):
    col_11 = data.iloc[:, column_index]

    mean_value = col_11.mean()
    median_value = col_11.median()

    print(f"Mean of Age: {mean_value}")
    print(f"Median of Age: {median_value}")

def get_mean():
	column_index = 11
	if column_index < len(data.columns):
		col_11 = data.iloc[:, column_index]
	
	col_11_numeric = pd.to_numeric(col_11, errors='coerce')
	mean_value = col_11_numeric.mean()

	return mean_value

def get_median():
	column_index = 11
	if column_index < len(data.columns):
		col_11 = data.iloc[:, column_index]

	col_11_numeric = pd.to_numeric(col_11, errors='coerce')
	median_value = col_11_numeric.median()

	return median_value


