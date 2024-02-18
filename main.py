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

# data = pandas.read_csv("weather_data.csv")
# max_temp = data[data.temp == data.temp.max()]
# print(max_temp.day)

data = pandas.read_csv("Squirrel_Data.csv")

grey_squirrels_count = data[data["Primary Fur Color"] == "Gray"].shape[0]
red_squirrels_count = data[data["Primary Fur Color"] == "Cinnamon"].shape[0]
black_squirrels_count = data[data["Primary Fur Color"] == "Black"].shape[0]


print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

