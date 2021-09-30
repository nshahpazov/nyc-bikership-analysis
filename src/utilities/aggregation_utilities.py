import pandas as pd

def get_bike_counts_per_day(bikes_df):
    return (bikes_df
     .groupby('day')
     .count()['year']
     .reset_index()
     .rename(columns={'year': 'Bikers Count'})
    )


def get_bike_counts_by_avg_temperature(bikes_df):
    return (bikes_df
     .groupby('average temperature')
     .count()['tripduration']
     .reset_index()
     .rename(columns={'tripduration': 'bikes_count'})
    )


def get_mean_trip_durations(bikes_df):
    return (bikes_df[bikes_df['tripduration_minutes'] <= 60]
     .groupby('day')['tripduration_minutes']
     .mean()
     .reset_index()
     .rename(columns={'tripduration_minutes': 'Average Duration in Minutes'})
    )

def get_average_durations_and_counts(bikes_df):
    return pd.merge(
        get_mean_trip_durations(bikes_df),
        get_bike_counts_per_day(bikes_df),
        left_on='day',
        right_on='day'
    )

def get_popular_stations(bikes_df, type='start', n=10):
    return (bikes_df[f"{type} station name"]
     .value_counts(normalize=True)
     .head(n)
     .multiply(100)
    #  .map('{:,.2f}%'.format)
     .reset_index()
     .rename(columns={'index': "Station Name", 	f"{type} station name": 'Percentage'})
     .assign(Type=type)
    )

