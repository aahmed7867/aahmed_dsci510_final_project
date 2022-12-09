import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

df = pd.read_csv('data/Cairo_weather_data_2018.csv')

dates_main = []
y1_main = []
y2_main = []
y3_main = []

fig, axes = plt.subplots(figsize=(12, 8))
date_formatter = mdates.DateFormatter("%Y-%m")
date_locator = mdates.MonthLocator(interval=1)
axes.xaxis.set_major_formatter(date_formatter)
axes.xaxis.set_major_locator(date_locator)