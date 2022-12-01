from datetime import datetime
from meteostat import Point, Daily

los_a = Point(34.0167, -118.2833, 70)

new_delhi = Point(28.5833, 77.2, 70)

london = Point(51.5167, -0.1167, 70)

sydney = Point(-33.9, 151.2, 70)

rio_de_jan = Point(-22.9, -43.1667, 70)

cairo = Point(30.1333, 31.4, 70)

places = {'Los_Angeles': los_a, 'New_Delhi': new_delhi,
          'London': london, 'Sydney': sydney, 'Rio_De_Janeiro': rio_de_jan, 'Cairo': cairo}

for year in [2018, 2019, 2020]:  
    for k in places:
        data = Daily(places[k], datetime(year, 1, 1), datetime(year, 12, 31))
        data = data.fetch()
        data.to_csv(k+'_weather_data_'+str(year)+'.csv')


