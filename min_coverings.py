# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:02:42 2023
@author: johnpsom
"""
import itertools
import pandas as pd
# a python way to create any covering for any lottery in the world
# initial set of all possible number combinations of K numbers out of N
# change values below as wanted
K = 5
N = 45
# covering of how many max numbers
C = 4  # C should be K-1, K-2, K-3 etc. the least prize category you want at least one success
initial_set = list(itertools.combinations(range(1, N+1), K))
# use lines below to create covering for a file
#df = pd.read_csv('jkr_data/mynewstiles.csv', index_col=0, dtype={'XE20': str})
#df = df.loc[:, 'st1':'st5']
#initial_set = (df.values.tolist())

# covering set
covering_set = []
co = 0  # this is a counter variable
# iterate over initial set
for combination in initial_set:
    # flag to check if all combinations of the covering set have at max C common number
    flag = True
    # iterate over combinations of the covering set
    for c in covering_set:
        # count number of common values
        count = 0
        # iterate over combination
        for i in combination:
            # check if value is present in other combinations
            if i in c:
                count += 1
        # if greater or equal to 3 common values set flag to false, break and continue
        if count >= C:
            flag = False
            break
    # if flag is still true, add to covering set
    if flag:
        covering_set.append(combination)
    co += 1
    if co % 100 == 0:
        # print info on how many combinations have been searched and how many have passed
        print(co, len(covering_set), combination)
# save the covering_set to a dataframe and a csv file
df = pd.DataFrame(covering_set, columns=[
                  f'st{i}' for i in range(1, K+1)]).reset_index(drop=True)
df.to_csv(f'jkr_data/covering_{N}_{K}_{C}_{len(covering_set)}.csv')
