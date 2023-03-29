# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:05:57 2023

@author: thelonapiasototzoker@gmail.com
"""
import pandas as pd
import random
import matplotlib.pyplot as plt


def simulate_lottery(n_draws, n_tickets, ticket_cost, win_probability, win_amount,
                     smaller_prizes_probs, smaller_prizes_amounts):
    '''
    simulating the lottery draw
    '''
    won = 0
    win5p1 = 0
    win5 = 0
    tot_small_winnings = 0
    cumulative_winnings = [0]
    # Initial winnings are set to zero
    for _ in range(n_draws):
        total_draw_winnings = -n_tickets * ticket_cost

        for _ in range(n_tickets):
            # Check if the player wins in the current draw
            random_value = random.random()
            if random_value < win_probability:
                total_draw_winnings += win_amount
                win5p1 += 1
            else:
                # Check for smaller prize wins
                for prob, amount in zip(smaller_prizes_probs, smaller_prizes_amounts):
                    if random_value < 1/1221759:
                        win5 += 1
                    if random_value < prob:
                        total_draw_winnings += amount
                        tot_small_winnings += amount
                        break
        print(total_draw_winnings)
        if total_draw_winnings > 0:
            won += 1
        cumulative_winnings.append(cumulative_winnings[-1] + total_draw_winnings)
    return cumulative_winnings, win5p1, win5, tot_small_winnings-win5*50000


# Simulate a 1000 times for 150 draws in a year
dd = pd.DataFrame(columns=['w5p1', 'w5', 'yearly_small_winnings'])
for _ in range(1000):
    # Parameters for the simulation
    n_draws = 150
    n_tickets = 24000
    ticket_cost = 0.5
    win_probability = 1 / 24435180  # Example probability for a 5 out of 45 1st prize
    win_amount = 1000000  # Example winning amount for 1st prize
    # probabilities for smaller prizes
    smaller_prizes_probs = [1/1221759, 1/122175.9, 1/6108.8, 1/3132.72, 1/156.64,
                            1/247.32, 1/12.37, 1/53.47, 1/2.67, 1/37.14, 1.86]
    # amounts for smaller prizes
    smaller_prizes_amounts = [50000, 2500, 50, 50, 2, 2, 0,
                              1.5, 0, 0, 0]
    # Run the simulation and plot the results
    cumulative_winnings, win5p1, win5, total_small_winnings = simulate_lottery(
        n_draws, n_tickets, ticket_cost, win_probability, win_amount,
        smaller_prizes_probs, smaller_prizes_amounts)

    plt.plot(cumulative_winnings)
    plt.xlabel('Number of Draws')
    plt.ylabel('Cumulative Winnings')
    plt.title('Cumulative Winnings Over Time')
    plt.show()

    print(win5p1+win5, 'in ', n_draws)
    dd.loc[len(dd)] = [win5p1, win5, total_small_winnings]
print(dd.describe([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]))
