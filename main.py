import csv

# with open("weather_data.csv", mode="r") as file:
#     weather_data = file.readlines()
#     print(weather_data)
# temperatures = []
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#         print(row)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# temp_list = data["temp"].to_list()
#
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
max_temp = data[data.temp == data.temp.max()]
#print(data[data.temp == max_temp])

print(max_temp.day)