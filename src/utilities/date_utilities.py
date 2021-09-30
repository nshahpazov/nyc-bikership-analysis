# load required packages
import pandas as pd

# env constants
RIDES_YEAR = '2016'
RIDES_MONTH = '2'
RIDES_NEXT_MONTH = '3'
START_TIME_COL = 'starttime'
STOP_TIME_COL = 'stoptime'

TIME_COLUMNS = [START_TIME_COL, STOP_TIME_COL]

# message constants
INVALID_DATE_EXCEPTION_MSG = "Start and end dates are not all in the correct format!"

# regex and format constants
CORRECT_DATE_FORMAT = "%m/%d/%Y %H:%M:%S"
START_REGEX = r'' + RIDES_MONTH + '\/[0-9]{1,2}\/' + RIDES_YEAR
STOP_REGEX = r'[' + RIDES_MONTH + '-' + RIDES_NEXT_MONTH + ']\/[0-9]{1,2}\/' + RIDES_YEAR

def is_bike_time_correct(time_series):
    is_start = time_series.name == START_TIME_COL
    return time_series.str.contains(START_REGEX if is_start else STOP_REGEX)

def format_bike_times(df):
    col_names = [START_TIME_COL, STOP_TIME_COL]
    is_correct = df[col_names].apply(is_bike_time_correct).mean(axis=0) < 1

    # if there are rows with incorrect date format, throw an exception
    if is_correct.any():
        raise Exception(INVALID_DATE_EXCEPTION_MSG)

    # add zeros in front of the date strings
    return df.assign(**{
        START_TIME_COL: '0' + df[START_TIME_COL],
        STOP_TIME_COL: '0' + df[STOP_TIME_COL]
    # cast to the correct date format
    }).apply(pd.to_datetime, format=CORRECT_DATE_FORMAT)
