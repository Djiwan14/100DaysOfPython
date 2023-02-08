# opening the file nd converting it to a list
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# creating lists for all rows with csv module
# import csv
#
# with open("weather_data.csv") as weather_data:
#     datas = csv.reader(weather_data)
#     print(datas)

# coding challenge to make a list containing only temperature
#     temperatures = []
#     for data in datas:
#         if data[1] != "temp":
#             temperatures.append(int(data[1]))
#     for temp in temperatures:
#         print(temp)

# working with pandas module
import pandas
data = pandas.read_csv("weather_data.csv")
print(data)

# converting object of pandas to a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# converting object of pandas to a list
# temp_list = data["temp"].to_list()
# sum = 0
# for temp in temp_list:
#     sum += temp
# avg = round(float(sum / len(temp_list)), 2)
# print(avg)

# Average value of a list
# print(data["temp"].mean())

# Maximum value of a list
# print(data["temp"].max())

# Get data in a column
# print(data["condition"])
# print(data.condition)

# Get data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == 12])

# Coding challenge to find max degree and print its row
# print(data[data.temp == data["temp"].max()])

# declaring a variable for the whole row
# monday = data[data.day == "Monday"]
# print(monday)

# Coding challenge to convert monday's degree to Fahrenheit
# monday = data[data.day == "Monday"]
# Fahrenheit_temp = (monday.temp * 9/5) + 32
# print(Fahrenheit_temp)

# Creating a dataFrame from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# Coding challenge with squirrels
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
squirrel_dict = {
    "Fur Colors" : ["Gray", "Red", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
squirrel_data = pandas.DataFrame(squirrel_dict)
squirrel_data.to_csv("squirrel_count.csv")
