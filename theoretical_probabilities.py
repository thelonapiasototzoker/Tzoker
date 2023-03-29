# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:38:10 2023

@author: thelonapiasototzoker@gmail.com
"""


import math


def combinations(n, k):
    '''
    find the n by k combinations
    '''
    return math.comb(n, k)


n_main_numbers = 45
k_main_numbers = 5
n_extra_numbers = 20

total_main_combinations = combinations(n_main_numbers, k_main_numbers)

# Winning combinations
combinations_to_check = [
    (5, 1), (5, 0),
    (4, 1), (4, 0),
    (3, 1), (3, 0),
    (2, 1), (2, 0),
    (1, 1), (1, 0),
    (0, 1), (0, 0)
]
# Calculate and print probabilities for each winning combination

for correct_main_numbers, correct_extra_numbers in combinations_to_check:
    false_main_numbers = 5-correct_main_numbers
    if correct_main_numbers == 5:
        main_prob = 1 / total_main_combinations
    else:
        main_prob = (combinations(n_main_numbers - k_main_numbers, false_main_numbers) *
                     combinations(k_main_numbers, k_main_numbers - false_main_numbers)) /\
            total_main_combinations

    if correct_extra_numbers == 1:
        extra_prob = 1/n_extra_numbers
    else:
        extra_prob = (n_extra_numbers - correct_extra_numbers)/n_extra_numbers
    print(main_prob, extra_prob)
    prob = main_prob * extra_prob
    print(
        f"Probability of getting {correct_main_numbers} main numbers and {correct_extra_numbers}\
        extra numbers: {prob}, 1/{round(1/prob,2)}")
