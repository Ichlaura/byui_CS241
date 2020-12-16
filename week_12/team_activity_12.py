# import matplotlib
# from datetime import datetime
# import pandas as pd
# import numpy as np
# # matplotlib.use("TkAgg")
# import matplotlib.pyplot as plt
# pd.set_option('display.max_columns', 25)
# pd.set_option('display.max_rows', 8)
# pd.set_option('display.width', 1000)
#
# data = pd.read_csv("weather_year.csv")
#
# data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
#                 "mean_dew", "min_dew", "max_humidity", "mean_humidity",
#                 "min_humidity", "max_pressure", "mean_pressure",
#                 "min_pressure", "max_visibilty", "mean_visibility",
#                 "min_visibility", "max_wind", "mean_wind", "min_wind",
#                 "precipitation", "cloud_cover", "events", "wind_dir"]
#
# first_date = data.date.values[0]
#
# print(first_date)
# print(datetime.strptime(first_date, "%Y-%m-%d"))
#
# print("* * * * * ")
#
# data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
#
# print(data.date.head())
#
# print("* * * * * ")
#
# data.max_temp.plot()
# plt.show()
import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv("weather_year.csv")
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]
                # this reassigns column names
data.max_temp.plot()
plt.show()
