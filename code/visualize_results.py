import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
import datetime


def line_plot(df_dict, year, city, columns):
    date_formatter = mdates.DateFormatter("%Y-%m")
    date_locator = mdates.MonthLocator(interval=2)
    dates = [datetime.datetime.strptime(
        d, "%Y-%m-%d") for d in df_dict[year][city]['time'].values.tolist()]
    fig = plt.figure(figsize=(14, 9))
    ax = plt.gca()
    ax.xaxis.set_major_formatter(date_formatter)
    ax.xaxis.set_major_locator(date_locator)
    for col in columns:
        plt.plot(dates, df_dict[year][city][col].values.tolist(), label=col)
    plt.tight_layout()
    plt.xlabel('Time (Year - Month)')
    plt.ylabel('Values')
    fig.autofmt_xdate()
    plt.legend()
    if year == 'alltime':
        plt.title(', '.join(columns) +
                  ' Variation over time 2018, 2019, 2020 in '+city)
        plt.savefig('results/'+', '.join(columns) +
                    ' Variation over time 2018, 2019, 2020 in '+city+'.png', bbox_inches='tight')
    else:
        plt.title(', '.join(columns)+' Variation over time ' +
                  str(year)+' in '+city)
        plt.savefig('results/'+', '.join(columns) +
                    ' Variation over time '+str(year)+' in '+city+'.png', bbox_inches='tight')
    plt.show()


def correlation_plot(df_dict, year, city):
    sns.heatmap(df_dict[year][city].corr(),
                annot=True)  
    sns.set(rc={'figure.figsize': (10, 10)})
    plt.title('Correlation between columns in ' +
              str(year)+' - '+city+' dataframe')
    plt.savefig('results/'+'Correlation between columns in ' +
                str(year)+' - '+city+' dataframe.png', bbox_inches='tight')
    plt.show()