
# env constants
RIDES_YEAR = 2016

START_TIME_COL = 'starttime'
STOP_TIME_COL = 'stoptime'

def cast_bike_types(bikes_df):
    # cast the birth year to a correct format
    bikes_df['birth year'] = bikes_df['birth year'].astype('Int32')

    # change the gender to a category
    bikes_df[['gender']] = (bikes_df[['gender']]
     .replace({0: 'unknown', 1: 'male', 2: 'female'})
     .astype('category')
    )

    # change the usertype to a category
    bikes_df['usertype'] = bikes_df['usertype'].astype('category')
    return bikes_df

def attach_additional_bike_columns(bikes_df):

    # add helper columns for the start and stop time dates
    bikes_df['month'] = bikes_df[START_TIME_COL].dt.month
    bikes_df['day'] = bikes_df[START_TIME_COL].dt.day
    bikes_df['start_hour'] = bikes_df[START_TIME_COL].dt.hour
    bikes_df['start_minute'] = bikes_df[START_TIME_COL].dt.minute

    # add stop hour and minute
    bikes_df['stop_hour'] = bikes_df[STOP_TIME_COL].dt.hour
    bikes_df['stop_minute'] = bikes_df[STOP_TIME_COL].dt.minute

    # add an age column
    bikes_df['age'] = RIDES_YEAR - bikes_df['birth year']

    # add additional columns for duration (minutes and hours)
    bikes_df['tripduration_minutes'] = bikes_df['tripduration'] / 60
    bikes_df['tripduration_hours'] = bikes_df['tripduration'] / (60 * 60)

    return bikes_df
