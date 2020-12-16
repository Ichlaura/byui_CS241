import matplotlib
import seaborn as sns
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)

# load file data
player_info = pd.read_csv("data/basketball_players.csv")
master_data = pd.read_csv("data/basketball_master.csv")

data = pd.merge(player_info, master_data)

print(data)
print(data.columns)


# part 1

print("* * * * * * * * * * * * * * * * * * * * * * * * * * \n "
      "Calculate the mean and median number of points scored. \n"
      "(In other words, each row is the amount of points a player \n"
      "scored during a particular season. Calculate the median of \n"
      "these values. The result of this is that we have the median \n"
      "number of points players score each season.)\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

points_mean = data.points.mean()
print("The mean number of points scored: {}".format(points_mean))
points_median = data.points.median()
print("The median number of points scored: {}".format(points_mean))
#

print("* * * * * * * * * * * * * * * * * * * * * * * * * * \n "
      "Determine the highest number of points recorded in a single\n"
      "season. Identify who scored those points and the year they did so.\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

highest_points = data.points.max()
highest_points_year = data[data.points == highest_points][["points", "year", "firstName", "middleName", "lastName", "nameSuffix"]]
print(f"The highest points: {highest_points}")
print(f"The year of highest of points: {highest_points_year}")


print("* * * * * * * * * * * * * * * * * * * * * * * * * * \n "
      "Produce a boxplot that shows the distribution of total points,\n"
      "total assists, and total rebounds (each of these three is a\n"
      "separate box plot, but they can be on the same scale and in the\n"
      "same graphic).\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

data["total_points"] = data.points + data.PostPoints
data["total_assists"] = data.assists + data.PostAssists
data["total_rebounds"] = data.rebounds + data.PostRebounds
data[["total_points", "total_assists", "total_rebounds"]].plot(kind="box")
matplotlib.pyplot.show()


print("* * * * * * * * * * * * * * * * * * * * * * * * * * \n "
      "Produce a plot that shows how the number of points scored has\n"
      "changed over time by showing the median of points scored per year,\n"
      "over time. The x-axis is the year and the y-axis is the median\n"
      "number of points among all players for that year.\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

year_points = data[["year", "points"]].groupby("year").median()
year_points.plot(kind="line")
matplotlib.pyplot.show()


print("* * * * * * * * * * * * * * * * * * * * * * * * * * \n"
      "Some players score a lot of points because they attempt a lot of\n"
      "shots. Among players that have scored a lot of points, are there\n"
      "some that are much more efficient (points per attempt) than others?\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * ")

data["PointsPerAttempt"] = data.points / (data.fgAttempted + data.ftAttempted)
player_points_attempted = data[["playerID", "lastName", "PointsPerAttempt"]].groupby("playerID").mean()
player_points_attempted = player_points_attempted[player_points_attempted.PointsPerAttempt != np.inf]
print(player_points_attempted)


# top10_points_player = player_points_attempted.nlargest(10,"PointsPerAttempt")["PointsPerAttempt"]
# print(top10_points_player)
#
# pd.merge(top10_points_player, master, how = "left", left_on = "playerID", right_on = "bioID")[["firstName","middleName","lastName","nameSuffix","PointsPerAttempt"]]
#
# # part 2-2: Are there any players that are exceptional across many categories?
# statistical_category = ["points","rebounds","assists","steals","blocks","turnovers"]
# exceptional_player = data[statistical_category + ["playerID"]].groupby("playerID").mean().nlargest(10, statistical_category)
#
# for i in statistical_category:
#     exceptional_player[i+ "Rank"] = exceptional_player[i].rank(ascending = True, pct =  True)
#
# print(exceptional_player[exceptional_player.columns[-6:]])
#
# pd.merge(exceptional_player[exceptional_player.columns[-6:]], master, how = "left", left_on = "playerID", right_on = "bioID")[["firstName","middleName","lastName","nameSuffix"]]
#
# exceptional_player[exceptional_player.columns[-6:]].plot(kind = "bar")
# matplotlib.pyplot.show()
#
# # part 2-3: do you see a trend of more three-point shots either across the league or among certain groups of players?
# # Is there a point at which popularity increased dramatically?
#
# data["total_threeAttempted"] = data.threeAttempted + data.PostthreeAttempted
# data["total_threeMade"] = data.threeMade + data.PostthreeMade
#
# three_data_per_year = data.groupby(["lgID","year"]).mean().reset_index()[["lgID","year","total_threeAttempted","total_threeMade"]]
# three_data_per_year = three_data_per_year[(three_data_per_year.total_threeAttempted > 0) & (three_data_per_year.total_threeMade > 0)]
# three_data_per_year = three_data_per_year.melt(["lgID","year"])
#
# print(three_data_per_year)
#
# grid = sns.FacetGrid(three_data_per_year, col = "lgID", hue= "variable")
#
# grid.map(sns.lineplot, "year", "value").add_legend()
#
# matplotlib.pyplot.show()
#
#
#
# plot = sns.lineplot(x = "year", y = "total_threeAttempted", data = data)
# plot2 = sns.lineplot(x = "year", y = "total_threeMade", data = data)
#
# matplotlib.pyplot.legend(['threeAttempted','threeMade'])
# matplotlib.pyplot.show()
#
#
# # part 3
# # part 3-1: which player is the GOAT (the Greatest Of All Time) ?
# stats = ["points","rebounds","assists","steals","blocks","turnovers"]
# player_stat = data[["playerID"] + stats].groupby("playerID").mean()
#
# for i in stats:
#     player_stat[i+ "Rank"] = player_stat[i].rank(ascending = True, pct =  True)
#
# print(player_stat)
#
# player_stat_rank = player_stat.iloc[:,[x for x in range(6,12)]]
# player_stat_rank_goat = player_stat_rank * [0.5, 0.1, 0.1, 0.1, 0.1, 0.1]
# player_stat_rank_goat["GOAT_score"] = player_stat_rank_goat.sum(axis = 1)
# top_10_goat = player_stat_rank_goat.nlargest(10,"GOAT_score")
#
# print(player_stat_rank)
# top_10_goat = pd.merge(top_10_goat["GOAT_score"],master, how = "inner", left_on = "playerID", right_on = "bioID")[["firstName","middleName","lastName","nameSuffix","GOAT_score"]]
# print(top_10_goat)
# sns.barplot(x = "firstName", y = "GOAT_score", data = top_10_goat)
#
# matplotlib.pyplot.ylim(0.9, 1)
# matplotlib.pyplot.show()
#
# # part 3-2 : Can you find anything interesting about players who came from a similar location?
# print(master.columns)
#
# location_group_height = master.groupby(["birthState"]).mean()["height"].sort_values(ascending = False).nlargest(10)
# location_group_weight = master.groupby(["birthState"]).mean()["weight"].sort_values(ascending = False).nlargest(10)
# print(location_group_height)
# print(location_group_weight)
#
# location_group_height.plot(kind = 'barh', x = "birthState", y = "height")
#
# matplotlib.pyplot.show()
#
# location_group_weight.plot(kind = 'barh', x = "birthState", y = "weight")
#
# matplotlib.pyplot.show()
#
# # part 3-3 : Find something else in this dataset that you consider interesting. Produce a graph to communicate your insight.
#
# # The correlation between weight and height per position
# data_r = data[["pos","height","weight"]].replace([np.inf, -np.inf], np.nan).dropna()
#
# grid = sns.FacetGrid(data_r[data_r.height > 0][data_r.weight > 0], col = "pos")
# grid.map(sns.scatterplot, "height", "weight").add_legend()
# matplotlib.pyplot.show()
#
# # how much height have been changed over years per position
# data_r2 = data[["pos","year","height","weight"]].replace([np.inf, -np.inf], np.nan).dropna()[data.height > 0][data.weight > 0]
#
# sns.lineplot(x = "year", y = "height", data = data_r2, hue = "pos")
# matplotlib.pyplot.show()
