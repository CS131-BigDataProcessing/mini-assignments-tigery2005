# Crime Test Package

## Setup:
- **Unzip the Crime_Data.zip file (GitHub file size limitations)

## Part 1: Modules and Unit Tests

### 1. `validate_functions.py`
This module provides functions to validate the data:
- **Vict sex validation**: Checks that the 'Vict sex' column only contains values 'M' or 'F', and checks that no value is missing (NULL).
- **Vict age validation**: Checks that the 'Vict age' column contains values between 1 and 100 and does not have missing (NULL) values.

### 2. 'stats_functions.py'
This module calculates the mean and median of the ge colulm:
- **Mean age calculation: returns the mean age of victims
- **Median age calculation: returns the median age of victims

## Part 2: Unittesting

- **Test that the stat_function module returns valid values
- **Test that the validate_functions module returns correct datatype

## Part 3: Freeze 

- 'pip freeze' and store required libraries in a 'requirements.txt' file

## Part 4: Build the package 














