# DSCI 510 Final Project
## Impact of Global Warming on Weather Trends

Global warming is one of the most discussed topics in the modern world. It has numerous dangerous effects on the planet, directly impacting the world's future. People are trying to identify the reasons for this and prevent it. Weather patterns all over the world have changed as a result of the causes of global warming. Analyzing weather data over several years will allow us to identify trends in weather variation caused by the global warming effect.

# Dependencies

The following Python libraries are used in this project:

> matplotlib==3.5.2

> meteostat==1.6.5

> pandas==1.4.2

> seaborn==0.11.2

# Installation

Run the following command in the Command Line Window to install the project requirements:

```
pip install -r requirements.txt
```

# Running the project

Run the following command in the Command Line Window to run the project:

```
python code/main.py
```

# GitHub Repository Link

https://github.com/aahmed7867/aahmed_dsci510_final_project

# Methodology

- First, the data is loaded into data frames from the CSV files and stored in a dictionary data structure.
- In each data frame, columns with all null values are removed using the “dropna” method.
- There are 3 data frames for each city relevant to the years 2018, 2019, and 2020. These 3 data frames are combined vertically to make an “alltime” data frame for every city.
- A function is defined to find the maximum "n" records of a data frame with respect to a column. The data frame is selected by the year and city names.
- A function is defined to find the minimum "n" records of a data frame with respect to a column. The data frame is selected by the year and city names.
- According to the analysis procedure, the aforementioned minimum and maximum record-finding functions can be used in the main code.
- Initially, I was planning to perform the analysis on the data for Los Angeles for the years 2018, 2019, and 2020. The plan was changed to use data in six cities representing six continents, to analyze the impact of global warming worldwide. The challenge presented was finding the optimum representation of the world, from the available weather stations in the API. It was solved by selecting cities from every continent available in the weather API.

# Visualization

- A function is defined to plot line charts. We can plot multiple line plots in the same figure using this function. The corresponding data frame and the interesting columns can be specified in the main code when we call this function to plot a line chart.
- A correlation plotting method is defined to view the correlation coefficients of a data frame. It generates a heatmap plot with the correlation coefficient values.
- A scatter plot method is added to view the data distribution. It generates a scatter plot of the distribution of data points in the specified columns.
- A method is added to plot grouped bar chart. It can be used to visualize several parameters of several cities in a single plot. This will represent the data in a quickly understandable manner.
- According to the above calculations and the data visualizations, we can identify that there is a small effect on weather parameters due to the global warming effect. The line plot shows this effect on the “tavg” parameter. This variation can be used as evidence on this point. Also, the minimum and maximum parameter calculations give insights into the facts.
- The grouped bar chart was not in the initial plan. It was added to the project since there was no method to visualize and compare the parameter variation across all cities. While creating this plot, it was required to add the numerical values of each bar to the plot to give an informative representation. For that, I wanted to extract the maximum number of parameters and store them in a data structure. This proved to be a bit of a challenge.

> [Bonus]
> As an advanced plot, I have created a line chart simulation, which shows the line plotting as a simulation with respect to time. Each data point is added to the plot separately, and a time interval is set between the two data points. The process is done by using a “for” loop. For this plotting, I only selected the data records from January 1st to April 30th, 2018 for Cairo city. Also, I added 3 line charts to show the variation of ‘tmin’, ‘tavg’, and ‘tmax’ values. Those 3 plots are shown in 3 different colors.
> The specialty of this plot is that it shows past data as a real-time data stream. The data that I am using to plot was collected in 2018, but with this plot, I can show it as a real-time data collection process.

# Future Work

> As a future expansion, we can collect data for more years in more cities around the world and use it for analysis. Also, we can use the other weather parameters except “tavg” for the processing. This will be helpful to identify the global warming effect on weather parameters in a very accurate manner.
