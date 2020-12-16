import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)
# %matplotlib inline

# # http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
#
# """ Series """
# # create a Series with an arbitrary list
# print("---> basic output <---")
# s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
# print(s)
#
# print("\n---> can specify an index to use when creating the Series <---")
# ss = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
#                index=['A', 'Z', 'C', 'Y', 'E'])
# print(ss)
#
# print("\n---> can convert a dictionary, using the keys of the dictionary as its index <---")
# d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
#      'Austin': 450, 'Boston': None}
# cities = pd.Series(d)
# print(cities)
#
# print("\n---> use the index to select specific items from the Series <---")
# print(f"*** 'Chicago' {cities['Chicago']} ***")
# print(cities[['Chicago', 'Portland', 'San Francisco']])
#
# print("\n---> use boolean indexing for selection <---")
# print(cities[cities < 1000])
#
# print("\n---> returns a Series of True/False values, which we then pass to our Series cities, returning the corresponding True items. <---")
# less_than_1000 = cities < 1000
# print(less_than_1000)
# print("")
# print(cities[less_than_1000])
#
# print("\n---> can also change the values in a Series on the fly <---")
# # changing based on the index
# print('Old value:', cities['Chicago'])
# cities['Chicago'] = 1400
# print('New value:', cities['Chicago'])
#
# # changing values using boolean logic
# print(cities[cities < 1000])
# print('\n')
# cities[cities < 1000] = 750
# print(cities[cities < 1000])
#
# print("\n---> see if an item is in the Series? check using idiomatic Python. <---")
# print('Seattle' in cities)
# print('San Francisco' in cities)
#
# print("\n---> Mathematical operations can be done using scalars and functions. <---")
# # divide city values by 3
# print(cities / 3)
# print("")
# # square city values
# print(np.square(cities))
#
# print("\n---> can add two Series together, which returns a union of the "
#       "two Series with the addition occurring on the shared index values. "
#       "Values on either Series that did not have a shared index will "
#       "produce a NULL/NaN <---")
# print(cities[['Chicago', 'New York', 'Portland']])
# print('\n')
# print(cities[['Austin', 'New York']])
# print('\n')
# print(cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']])
#
# print("\n---> NULL checking can be performed with isnull and notnull. <---")
# # returns a boolean series indicating which values aren't NULL
# print(cities.notnull())
# # use boolean logic to grab the NULL cities
# print(cities.isnull())
# print('\n')
# print(cities[cities.isnull()])
#
# """ DataFrame """
# print("\n---> Using the columns parameter allows us to tell the constructor "
#       "how we'd like the columns ordered. By default, the DataFrame constructor "
#       "will order the columns alphabetically <---")
# data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
#         'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
#         'wins': [11, 8, 10, 15, 11, 6, 10, 4],
#         'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
# football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
# print(football)
#
# print("\n---> Reading a CSV is as simple as calling the read_csv function. By "
#       "default, the read_csv function expects the column separator to be a "
#       "comma, but you can change that using the sep parameter. <---")
# from_csv = pd.read_csv('mariano-rivera.csv')
# print(from_csv.head())
#
# print("\n---> Our file had headers, which the function inferred upon reading "
#       "in the file. Had we wanted to be more explicit, we could have passed "
#       "header=None to the function along with a list of column names to use: <---")
# cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
#         'result', 'quarter', 'distance', 'receiver', 'score_before',
#         'score_after']
# no_headers = pd.read_csv('peyton-passing-TDs-2012.csv', sep=',', header=None,
#                          names=cols)
# print(no_headers.head())


