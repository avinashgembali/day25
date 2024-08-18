# with open("weather_data.csv", mode="r") as File:
#     data = File.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv", mode="r") as File:
#     data = csv.reader(File)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["day"])
# print(data["temp"])
# print(data["condition"])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# total = 0
# for num in temp_list:
#     total += num
# print(total/len(temp_list))
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data["day"] == "Thursday"])
# to satisfy the condition and get the row we require can be done by this
# print(data[data["temp"] == data["temp"].max()])
# tuesday = data[data["day"] == "Tuesday"]
# print(tuesday["temp"])
#
# new_data_dict = {
#     "names": ["avinash", "rahul", "dhruva"],
#     "scores": [70, 90, 99]
# }
# new_data = pandas.DataFrame(new_data_dict)
# print(new_data)
# new_data.to_csv("new_data.csv")
import pandas
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240818.csv")
# this method give total count of all colours o squirrels
# count = [squirrel_data["Primary Fur Color"].value_counts()]
# print(count) this is in form of list
grey_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
squirrel_count_dict = {
    "Fur Color": ["grey", "red", "black"],
    "count": [grey_count, red_count, black_count]
}
squirrel_count_data = pandas.DataFrame(squirrel_count_dict)
squirrel_count_data.to_csv("squirrel_count.csv")



