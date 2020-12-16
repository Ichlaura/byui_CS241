import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 1000)

# load file data
player_info = pd.read_csv("data/basketball_players.csv")
master_data = pd.read_csv("data/basketball_master.csv")

data = pd.merge(player_info, master_data, how="left", left_on="playerID", right_on="bioID")
# print(data.columns)

print("* * * * * * * * * * * * * * * * * * * * * * * * * *\n"
      "Calculate the mean and median number of points scored.\n"
      "(In other words, each row is the amount of points a player\n"
      "scored during a particular season. Calculate the median of\n"
      "these values. The result of this is that we have the median\n"
      "number of points players score each season.)\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

p_mean = data.points.mean()
p_median = data.points.median()
# print(f"The mean - points scored: {p_mean}")
# print(f"The median - points scored: {p_median}")
print()
print()


print("* * * * * * * * * * * * * * * * * * * * * * * * * * \n"
      "Determine the highest number of points recorded in a single\n"
      "season. Identify who scored those points and the year they did so.\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

highest_points = data.points.max()
highest_points_year = data[data.points == highest_points][["points", "year", "firstName", "lastName"]]
# print(f"The highest points: {highest_points}")
# print(f"The year of highest of points: {highest_points_year}")
print()
print()


print("* * * * * * * * * * * * * * * * * * * * * * * * * * \n "
      "Produce a boxplot that shows the distribution of total points,\n"
      "total assists, and total rebounds (each of these three is a\n"
      "separate box plot, but they can be on the same scale and in the\n"
      "same graphic).\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

data["total_points"] = data.points + data.PostPoints
data["total_assists"] = data.assists + data.PostAssists
data["total_rebounds"] = data.rebounds + data.PostRebounds
# data[["total_points", "total_assists", "total_rebounds"]].plot(kind="box")
# matplotlib.pyplot.show()
print()
print()


print("* * * * * * * * * * * * * * * * * * * * * * * * * * \n "
      "Produce a plot that shows how the number of points scored has\n"
      "changed over time by showing the median of points scored per year,\n"
      "over time. The x-axis is the year and the y-axis is the median\n"
      "number of points among all players for that year.\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

year_points = data[["year", "points"]].groupby("year").median()
# year_points.plot(kind="bar")
# matplotlib.pyplot.show()
print()
print()


print("* * * * * * * * * * * * * * * * * * * * * * * * * * \n"
      "Some players score a lot of points because they attempt a lot of\n"
      "shots. Among players that have scored a lot of points, are there\n"
      "some that are much more efficient (points per attempt) than others?\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

# Part 1
# read in csv file
players = pd.read_csv("data/basketball_players.csv")
print(players.columns)



# find field goal success rate
players["fgSuccess"] = players["fgMade"] / players["fgAttempted"]
# find players who have attempted more then 0 shots
players = players[(players.fgAttempted > 0) & (players.fgSuccess <= 1)]

# find free throw success rate
players["ftSuccess"] = players["ftMade"] / players["ftAttempted"]
players = players[(players.ftAttempted > 0) & (players.ftSuccess <= 1)]


# The box plot should show the distribution of the rates
# sns.boxplot(data=players[["fgSuccessPercent", "ftSuccessPercent", "threeSuccessPercent"]])
# plt.show()

# 2 Part

# Players need to have shot over 150 points per season
newdat = players[(players.points > 150)]

# Players need a high shot rate, assists and rebounds

newdat = players[(players.ftSuccess > .6) & (players.fgSuccess > .6) & (players.rebounds > 100) & (players.assists > 100)]
data_ = pd.merge(newdat, master_data, how="left", left_on="playerID", right_on="bioID")
print(data_[["firstName", "lastName", "fgSuccess", "ftSuccess", "assists", "rebounds"]])



# make a group by year
grouped = players.groupby('year')
# find the mean and median for each of those years
three_stats = grouped['threeMade'].agg([np.mean, np.median])
# reset index
three_stats = three_stats.reset_index()
# melt the data so that its in long format
three_stats = pd.melt(three_stats, id_vars=["year"], var_name="stat")
# lets check it
print(three_stats)

# This first plot is to show the main distribution across the different leagues.
# sns.factorplot(data=players, x="year", y="threeMade")
# plt.show()

stats = ["points","rebounds","assists","steals","blocks","turnovers"]
player_stat = data[["playerID"] + stats].groupby("playerID").mean()

for i in stats:
    player_stat[i+ "Rank"] = player_stat[i].rank(ascending = True, pct =  True)
    
print(player_stat)

player_stat_rank = player_stat.iloc[:,[x for x in range(6,12)]]
player_stat_rank_goat = player_stat_rank * [0.5, 0.1, 0.1, 0.1, 0.1, 0.1]
player_stat_rank_goat["GOAT_Status"] = player_stat_rank_goat.sum(axis = 1)
top_10_goat = player_stat_rank_goat.nlargest(3,"GOAT_Status")

print(player_stat_rank)
top_10_goat = pd.merge(top_10_goat["GOAT_Status"],master_data, how = "inner", left_on = "playerID", right_on = "bioID")[["firstName","middleName","lastName","nameSuffix","GOAT_Status"]]

sns.barplot(x="Count", y="Stats", data = top_10_goat)

matplotlib.pyplot.show()

#print(master_data["birthCity"].value_counts())


