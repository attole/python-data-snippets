import numpy as np

# task1
def task1(array1, array2):
    result_array = np.concatenate((array1, array2))
    min, max = np.min(result_array), np.max(result_array)
    sum, prod = np.sum(result_array), np.prod(result_array)

    print('concatenated array: ', result_array)
    print('min:', min, ' max:', max)
    print('sum: ', sum, ' prod: ', prod)

# a = np.random.random(5)
# print('array1: ', a)
# b = np.random.random(5)
# print('array2: ', b)

# task1(a, b)

import numpy as np
import random as rnd

# task2
def mean_by_gender(grades, genders) -> dict[str, float]:
    result_dict = {gender: 
                   round(np.mean(grades[np.where(genders == gender)]), 2) 
                   for gender in np.unique(genders)}
    return result_dict

array_size = 7
all_genders = ["male", "female"]
grades, genders = np.random.randint(0, 5, size=array_size), []

for _ in range(array_size):
    genders.append(all_genders[int(rnd.random() > 0.5)])
    
# print('grades: ', grades)
# print('genders: ', genders)

# print('result:', mean_by_gender(grades, np.array(genders)))

import numpy as np

# task 3
def wipe_even(array, target_value = 0, in_place = False) -> None | list[int]:
    if in_place:
        array[array % 2 == 0] = target_value
        return None
    else:
        return np.where(array % 2 == 0, target_value, array)
        
array = np.random.randint(0, 10, size = 10)
# print('array: ', array)
# print('result array: ', wipe_even(array))
# wipe_even(array, 10, True)
# print('changed previous array:', array)

import numpy as np
import matplotlib.pyplot as plt
# task 4

def calc_y(x) -> list:
    return x * 16

x = np.random.randint(0, 10, size=10)
y = calc_y(x)

# plt.rc('lines', linewidth = 2, linestyle='-')
# plt.plot(x, y, color='red', label='y = 16 * x')
# plt.title("Linear Graph", fontsize= 20)
# plt.xlabel("X-axis", fontsize=14)
# plt.ylabel("Y-axis", fontsize=14)
# plt.legend(loc='lower right', fontsize=14)
# plt.grid(True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# task 5
def func1(x):
    return x * np.sin(5 * x)

def func2(x):
    return 5 * np.sin(1 / x) * np.cos(x ** 2) ** 3

def func3(x):
    return x ** np.sin(10 * x)

def func4(x):
    return np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

def func5(x):
    return np.sin(10 * x) * np.sin(3 * x) / (x ** 2)

def func6(x):
    return 5 * np.sin(10 * x) * np.sin(3 * x) / np.sqrt(x)

x = [np.linspace(-2, 5, 100),
     np.linspace(-4, 4, 100),
     np.linspace(1, 10, 100),
     np.linspace(0.01, 10, 100),
     np.linspace(0.01, 4, 100),
     np.linspace(1, 7, 100)]
y = [func1, func2, func3, func4, func5, func6]
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'orange']
linestyles = ['-', '--', '-.', ':', '-', '--']
# fig, axs = plt.subplots(3, 2, figsize=(10, 10))
# counter = 0

# for i in range(3):
#     for j in range(2):
#         axs[i, j].plot(x[counter], y[counter](x[counter]), color = colors[counter], linestyle=linestyles[counter], linewidth=counter + 1)
#         axs[i, j].set_title('Function ' + str(counter + 1))
#         axs[i, j].grid(True)
#         counter += 1

# plt.tight_layout()
# plt.show()


import matplotlib.pyplot as plt

# task 6
table = {'A': 2310, 'B': 3145, 'C': 1520}
colors = ['orange', 'green', 'red']
explode = (0.1, 0, 0) 

# plt.figure(figsize=(5, 5))
# plt.pie(table.values(), labels=table.keys(), colors=colors, explode=explode, autopct='%1.1f%%', startangle=90)
# plt.title('Profit of Companies')

# plt.savefig('D:\\kpi\\python\\lab5\\pie_chart.png')
# plt.show()


import matplotlib.pyplot as plt

# task 7
table = {'A': 2310, 'B': 3145, 'C': 1520}
colors = ['orange', 'green', 'red']

# plt.figure(figsize=(5, 5))
# plt.pie(table.values(), labels=table.keys(), colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.65})
# plt.title('Profit of Companies')

# plt.savefig('D:\\kpi\\python\\lab5\\pie2_chart.png')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# task 8
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
companies = {'A': [470, 684, 350, 806],
             'B': [787, 586, 980, 792],
             'C': [320, 440, 360, 400]}
width = 0.2
colors = ['red', 'green', 'blue']
x = np.arange(len(quarters))
xs = [x - width, x, x + width]
# fig, ax = plt.subplots(figsize=(10, 6))

# counter = 0
# for key in companies.keys():
#     ax.bar(xs[counter], companies[key], width, color=colors[counter], label='Company ' + str(key))
#     counter += 1

# ax.set_xlabel('Quarters')
# ax.set_ylabel('Sales')
# ax.set_title('Sales Volumes by Company and Quarter')
# ax.set_xticks(x)
# ax.set_xticklabels(quarters)
# ax.legend(loc='upper right', fontsize=14)

# plt.savefig('D:\\kpi\\python\\lab5\\histogram_chart.png')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# task 9.1
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
companies = {'A': [470, 684, 350, 806],
             'B': [787, 586, 980, 792],
             'C': [320, 440, 360, 400]}
width = 0.2
colors = ['red', 'green', 'blue']
y = np.arange(len(quarters))
ys = [y - width, y, y + width]
# fig, ax = plt.subplots(figsize=(10, 6))

# counter = 0
# for key in companies.keys():
#     ax.barh(ys[counter], companies[key], width, color=colors[counter], label='Company ' + str(key))
#     counter += 1

# ax.set_ylabel('Quarters')
# ax.set_xlabel('Sales')
# ax.set_title('Horizontal group diagram')
# ax.set_yticks(x)
# ax.set_yticklabels(quarters)
# ax.legend(loc='upper right', fontsize=14)

# plt.savefig('D:\\kpi\\python\\lab5\\histogram2_chart.png')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# task 9.2
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
companies = {'A': [470, 684, 350, 806],
             'B': [787, 586, 980, 792],
             'C': [320, 440, 360, 400]}
width = 0.2
colors = ['red', 'green', 'blue']
x = np.arange(len(quarters))
bottoms = np.zeros(len(quarters))
# fig, ax = plt.subplots(figsize=(10, 6))

# counter = 0
# for key in companies.keys():
#     ax.bar(x, companies[key], width, color=colors[counter], bottom=bottoms, label='Company ' + str(key))
#     bottoms += np.array(companies[key])
#     counter += 1

# ax.set_xlabel('Quarters')
# ax.set_ylabel('Sales')
# ax.set_title('Stacked group diagram')
# ax.set_xticks(x)
# ax.set_xticklabels(quarters)
# ax.legend(loc='lower right', fontsize=14)

# plt.savefig('D:\\kpi\\python\\lab5\\histogram3_chart.png')
# plt.show()