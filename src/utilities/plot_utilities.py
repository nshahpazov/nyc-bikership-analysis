import numpy as np
import pandas as pd
import seaborn as sns
from plotnine import ggplot, aes, geom_bar, xlab, ylab

def plot_bikers_count_by_temp(bikes_df, weather_df, field, nbins=5):
    # construct lowest and highest temperatures
    low = bikes_df[field].min()
    high = bikes_df[field].max()

    # construct the bins based on lowest and highest
    temp_bins = np.linspace(low - 1, high + 1, nbins).round().astype(int)

    # construct ranges of temperatures and number each range has occured in the month
    temp_ranges = pd.cut(bikes_df[field], bins=temp_bins)
    number_of_ranges = pd.cut(weather_df[field], bins=temp_bins).value_counts()

    # count, normalize and plot
    return (temp_ranges.value_counts()
        .div(number_of_ranges)
        .reset_index()
        .rename(columns={'index': 'temp_range'})
        .pipe((sns.barplot, 'data'), x='temp_range', y=field))


# TOOD: make this dynamic and not hard corded
START = '2016-01-31'
END = '2016-03-01'

def plot_average_rides_count_per_week(df, usertype):
    start_times = df[df.usertype == usertype]['starttime']
    ride_counts = start_times.dt.day_name().value_counts()

    days_count = (ride_counts
     .index
     .str
     .slice(stop=3)
     .map(lambda x: np.busday_count(START, END, x)))

    return (ride_counts
        .div(days_count)
        .reset_index()
        .set_axis(['day', 'average_count'], axis=1)
        .pipe(ggplot) +
            aes(x='day', y='average_count') +
            geom_bar(stat='identity', fill='#336600', alpha=0.6) +
            xlab("Day") +
            ylab("Average count")
        )
