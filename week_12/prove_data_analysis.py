import pandas as pd  # Our data manipulation library
import seaborn as sns  # Used for graphing/plotting
import matplotlib.pyplot as plt  # If we need any low level methods
import os  # Used to change the directory to the right place

pd.set_option('display.max_columns', 45)
pd.set_option('display.max_rows', 8)
pd.set_option('display.width', 1000)

players = pd.read_csv("data/basketball_players.csv")
master = pd.read_csv("data/basketball_master.csv")

nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")

min = players["rebounds"].min()
max = players["rebounds"].max()
mean = players["rebounds"].mean()
median = players["rebounds"].median()

print("Rebounds per season: Min:{}, Max:{}, Mean:{:.2f}, Median:{}".format(min, max, mean, median))

# Let's just remove any rows with GP=0
nba = nba[nba.GP > 0]

nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]].sort_values("reboundsPerGame", ascending=False).head(10))

# Ploting
# sns.boxplot(data=nba.reboundsPerGame)
#sns.boxplot(data=nba[["rebounds", "oRebounds", "dRebounds"]])
eighties = nba[(nba.year >= 1980) & (nba.year < 1990)]
#sns.boxplot(eighties["reboundsPerGame"], orient="v")

# grid = sns.FacetGrid(eighties, col="year")
# grid.map(sns.boxplot, "reboundsPerGame", orient="v")

# Group by year
nba_grouped_year = nba[["reboundsPerGame", "year"]].groupby("year").median()
print(nba_grouped_year)

# nba_grouped_year = nba_grouped_year[nba_grouped_year["reboundsPerGame"] > 0]
# sns.regplot(data=nba_grouped_year, x="year", y="reboundsPerGame").set_title("Median rebounds per Year")

# Get the top 10 rebounders per year
nba_topRebounders_perYear = nba[["reboundsPerGame", "year"]].groupby("year")["reboundsPerGame"].nlargest(10)

# Get the median of these 10
nba_topRebounders_median_perYear = nba_topRebounders_perYear.groupby("year").median()

# Put year back in as a column
nba_topRebounders_median_perYear = nba_topRebounders_median_perYear.reset_index()

# Again no zeros...
nba_topRebounders_median_perYear_noZeros = nba_topRebounders_median_perYear[nba_topRebounders_median_perYear["reboundsPerGame"] > 0]

# Now plot
sns.regplot(data=nba_topRebounders_median_perYear_noZeros, x="year", y="reboundsPerGame").set_title("Median of Top 10 Rebounders Each Year")

# Show the current plot
plt.show()
# Save the current plot to a file
plt.savefig("boxplot_reboundsPerGame.png")