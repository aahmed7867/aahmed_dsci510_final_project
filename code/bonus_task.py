import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import time


def bonus_plot():
    # reading the data file and creating the dataframe
    df = pd.read_csv('data/Cairo_weather_data_2018.csv')

    dates_main = []
    y1_main = []
    y2_main = []
    y3_main = []

    fig, axes = plt.subplots(figsize=(12, 8))
    # formatter - shows the year and month only
    date_formatter = mdates.DateFormatter("%Y-%m")
    # the labels are shown in an interval of two months
    date_locator = mdates.MonthLocator(interval=1)
    # adding the formatter to the figure
    axes.xaxis.set_major_formatter(date_formatter)
    axes.xaxis.set_major_locator(date_locator)

    for i in range(120):
        # plotting data in the figure as a simulation
        dates_main.append([datetime.datetime.strptime(d, "%Y-%m-%d")
                           for d in df['time'].values.tolist()][i])
        y1_main.append(df['tmin'].values.tolist()[i])
        y2_main.append(df['tavg'].values.tolist()[i])
        y3_main.append(df['tmax'].values.tolist()[i])
        axes.clear()   # clearing the figure
        fig.autofmt_xdate()
        axes.plot(dates_main, y1_main, 'r')
        axes.plot(dates_main, y2_main, 'g')
        axes.plot(dates_main, y3_main, 'b')
        # defining plot parameters
        axes.set_xlabel('Date', fontsize=18)
        axes.set_ylabel('Temperature value', fontsize=18)
        axes.set_title(
            'Temperature variation in Cairo city in January-May 2018', fontsize=20)
        axes.legend(['Tmin', 'Tavg', 'Tmax'])
        axes.annotate('tmin-'+str(y1_main[-1]),
                      xy=(dates_main[-1], y1_main[-1]+0.5))
        axes.annotate('tavg-'+str(y2_main[-1]),
                      xy=(dates_main[-1], y2_main[-1]+0.5))
        axes.annotate('tmax-'+str(y3_main[-1]),
                      xy=(dates_main[-1], y3_main[-1]+0.5))
        plt.pause(0.5)  # pausing the plotting for a short time

    plt.savefig('results/bonus_task_plot.png', bbox_inches='tight')
    time.sleep(10)
    plt.show()