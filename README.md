# DSCI 510 - Final Project 

This repository is for the final project in the DSCI 510 class

# Dependencies

The following Python libraries are used in this project:

> matplotlib==3.5.2

> meteostat==1.6.5

> pandas==1.4.2

> seaborn==0.11.2

# Installation

Run following command in Command Line Window to install the requirements necessary to run your project:

```
pip install -r requirements.txt
```

# Running the project

Run following command in Command Line Window to run the project:

```
python code/main.py
```

# Methodology

- First, the data is loaded into data frames from the CSV files and stored in a dictionary data structure.
- In each data frame, columns with all null values are removed using the “dropna” method.
- There are 3 data frames for each city relevant to the years 2018, 2019, and 2020. These 3 data frames are combined vertically to make an “alltime” data frame for every city.
- A function is defined to find the maximum "n" records of a data frame with respect to a column. The data frame is selected by the year and city names.
- A function is defined to find the minimum "n" records of a data frame with respect to a column. The data frame is selected by the year and city names.
- According to the analysis procedure, the aforementioned minimum and maximum record-finding functions can be used in the main code.

# Visualization

- A function is defined to plot line charts. We can plot multiple line plots in the same figure using this function. The corresponding data frame and the interesting columns can be specified in the main code when we call this function to plot a line chart.
- A correlation plotting method is defined to view the correlation coefficients of a data frame. It generates a heatmap plot with the correlation coefficient values.
- A scatter plot method is added to view the data distribution. It generates a scatter plot of the distribution of data points in the specified columns.

> [Bonus]
> As an advanced plot, I have created a line chart simulation, which shows the line plotting as a simulation with respect to time. Each data point is added to the plot separately, and a time interval is set between the two data points. The process is done by using a “for” loop. For this plotting, I only selected the data records from January 1st to April 30th, 2018 for Cairo city. Also, I added 3 line charts to show the variation of ‘tmin’, ‘tavg’, and ‘tmax’ values. Those 3 plots are shown in 3 different colors.
> The specialty of this plot is that it shows past data as a real-time data stream. The data that I am using to plot was collected in 2018, but with this plot, I can show it as a real-time data collection process.

# Future Work

> Given more time, what is the direction that you would want to take this project in?