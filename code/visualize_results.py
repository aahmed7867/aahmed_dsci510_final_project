import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
import datetime


def line_plot(df_dict, year, city, columns):
    '''
    This function plots line charts for given column parameters in a single figure and save the plot in outputs folder.
    Here 'columns' is a list of parameters.
    '''

    ''' 
        If we display all the time values in x-axis in the plot, it will become very messy. To solve that problem,
        I have defined a formatter to display the dates using an interval.
    '''
    # formatter - shows the year and month only
    date_formatter = mdates.DateFormatter("%Y-%m")
    # the labels are shown in an interval of two months
    date_locator = mdates.MonthLocator(interval=2)
    # making date objects for x-axis
    dates = [datetime.datetime.strptime(
        d, "%Y-%m-%d") for d in df_dict[year][city]['time'].values.tolist()]
    fig = plt.figure(figsize=(14, 9))
    ax = plt.gca()
    # adding the formatter to the figure
    ax.xaxis.set_major_formatter(date_formatter)
    ax.xaxis.set_major_locator(date_locator)
    # plotting each column paramater in the columns list
    for col in columns:
        plt.plot(dates, df_dict[year][city][col].values.tolist(), label=col)
    plt.tight_layout()
    # defining plot parameters
    plt.xlabel('Time (Year - Month)')
    plt.ylabel('Values')
    fig.autofmt_xdate()
    plt.legend()
    # adding the title and saving the plot
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
    '''
    This function plots a correlation plot for the given dataframe (to specify the dataframe, we use year and city parameters).
    '''
    sns.heatmap(df_dict[year][city].corr(),
                annot=True)  # plotting a heatmap for correlations
    sns.set(rc={'figure.figsize': (10, 10)})
    # adding the title and saving the plot
    plt.title('Correlation between columns in ' +
              str(year)+' - '+city+' dataframe')
    plt.savefig('results/'+'Correlation between columns in ' +
                str(year)+' - '+city+' dataframe.png', bbox_inches='tight')
    plt.show()


def scatter_plot(df_dict, year, city, cols):
    '''
    This function plots the data points distribution for the given data columns in 'cols' list in a single scatter plot.
    '''
    sns.scatterplot(data=df_dict[year][city][cols]) # plotting the scatter plot
    sns.set(rc={'figure.figsize': (10, 10)})
    plt.xlabel('Value Index')
    plt.ylabel('Value')
    # adding the title and saving the plot
    if year == 'alltime':
        plt.title(', '.join(cols) +
                  ' Data distribution over time 2018, 2019, 2020 in '+city)
        plt.savefig('results/'+', '.join(cols) +
                    ' Data distribution over time 2018, 2019, 2020 in '+city+'.png', bbox_inches='tight')

    else:
        plt.title(', '.join(cols)+' Data distribution over time ' +
                  str(year)+' in '+city)
        plt.savefig('results/'+', '.join(cols)+' Data distribution over time ' +
                    str(year)+' in '+city+'.png', bbox_inches='tight')
    plt.show()