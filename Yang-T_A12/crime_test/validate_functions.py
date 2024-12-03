import pandas as pd
import os

curr_dir = os.path.dirname(__file__)
file_path = os.path.join(curr_dir, 'Crime_Data_from_2020_to_Present.csv')

data = pd.read_csv(file_path)

column_index = 12
if column_index < len(data.columns):
    col_values = data.iloc[:, column_index]

    is_male = col_values == "M"
    is_female = col_values == "F"
    is_missing = col_values.isnull()

    print(f"Number of 'M': {is_male.sum()}")
    print(f"Number of 'F': {is_female.sum()}")
    print(f"Number of missing values: {is_missing.sum()}")

column_index = 11
if column_index < len(data.columns):
    col_values = data.iloc[:, column_index]

    is_valid = (col_values >= 1) & (col_values <= 100) 
    is_invalid = (col_values < 1) | (col_values > 100)

    print(f"Number of Valid Ages (1-100): {is_valid.sum()}")
    print(f"Number of Invalid Ages: {is_invalid.sum()}")


def is_sex_valid():
	column_index = 12
	if column_index < len(data.columns):
		col_values = data.iloc[:, column_index]

	is_male = col_values == "M"
	is_female = col_values == "F"
	is_missing = col_values.isnull()

	return is_missing.sum() == 0

def is_age_valid():
	column_index = 11
	if column_index < len(data.columns):
		col_values = data.iloc[:, column_index]

	is_valid = (col_values >= 1) & (col_values <= 100)
	is_invalid = (col_values < 1) | (col_values > 100)

	return is_invalid.sum() == 0   













