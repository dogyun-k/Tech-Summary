import numpy as np

dic = {
    'HP': [130, 250, 190, 300, 210, 220, 170],
    'weight': [1900, 2600, 2200,  2900, 2400, 2300, 2100],
    'KPL': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
}


HP, weight = map(int, input('Enter HP, wieght? ').split())