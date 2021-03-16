import numpy as np
import random
import matplotlib.pyplot as plt

start_money = 100000.0
win_rate = 2
prob_of_win = 0.6
number_of_games = 30

invest_proportion_list = np.linspace(0.01, 1, 99)


def experiment(start_money, invest_proportion, random_games):
    for game in random_games:
        money_to_invest = start_money * invest_proportion
        start_money = start_money - money_to_invest
        if game:
            start_money = start_money + money_to_invest * (win_rate + 1)
        return start_money


def start():
    random_games = np.random.choice([1, 0], number_of_games, p=[prob_of_win, 1.0 - prob_of_win])
    outcome_list = []
    for invest_proportion in invest_proportion_list:
        outcome = experiment(start_money, invest_proportion, random_games)
        outcome_list.append(outcome)
    plt.plot(np.array(invest_proportion_list), np.array(outcome_list))
    plt.show()

start()
