import numpy as np
import matplotlib.pyplot as plt

#task 1
array1 = np.random.randint(1, 10, 5)
array2 = np.random.randint(1, 10, 5)
resultArray = np.concatenate((array1, array2))
#print(resultArray)

max, min = np.max(resultArray), np.min(resultArray)
sum, prod = np.sum(resultArray), np.prod(resultArray)
#print(max, min, sum, prod)

#task2
inputArray = np.random.randint(1, 10, 15)
#print(inputArray)

mean = np.mean(inputArray)
#print(mean)
resultArray = np.sort(inputArray - mean)
#print(resultArray)

#task3
inputArray = np.random.randint(1, 10, 20)
#print(inputArray)

resultArray = (inputArray + 10).reshape((5, 4))
#print(resultArray)

#task4
inputArray = np.random.randint(-15, 16, (2, 5))
#print(inputArray)

resultArray = np.where(inputArray < 0, -1, 1)
#print(resultArray)

#task5
inputArray = np.random.randint(1, 10, (4, 6))
#print('inputArray:', inputArray)

resultArray = np.sort(inputArray)
#print('sortedArray:', resultArray)

min, max = np.min(resultArray), np.max(resultArray)
#print('min:', min, 'max:', max)

sum, mean = np.sum(resultArray), np.mean(resultArray)
#print('sum:', sum, 'mean:', mean)

#task6
# x = np.random.randint(-10, 10, 10)
# y = x + 14

# plt.figure(figsize=(10, 5))
# plt.plot(x, y, label='y = x + 14', color='r', linestyle=':', marker='v')
# plt.title(loc='center', label='task6')
# plt.axis('equal')
# plt.legend(loc='lower right')
# plt.xlabel('X values', fontsize=14, color='blue')
# plt.ylabel('Y values', fontsize=14, color='blue')
# plt.grid(True)
# plt.show()

#task7
# x1 = np.linspace(-1, 2, 500)
# y1 = 3 ** x1 + np.cos(15 * x1)
# x2 = np.linspace(0, 4, 500)
# y2 = 10 * np.cos(x2 ** 2) / x2 ** 2

# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.plot(x1, y1, label='3 ^ x + cos(15 * x)', color='red', linestyle=':')
# plt.title(loc='center', label='plot 1: 3 ^ x + cos(15 * x)')
# plt.legend(loc='lower right')
# plt.grid(True)

# plt.subplot(1, 2, 2)
# plt.plot(x2, y2, label='10 * cos(x ^ 2) / x ^ 2', color='blue', linestyle='-')
# plt.title(loc='center', label='plot 2: 10 * cos(x ^ 2) / x ^ 2')
# plt.legend(loc='upper right')
# plt.ylim(-5, 25)
# plt.grid(True)

# plt.show()

#task 8
# x = np.linspace(-6, 6, 100)
# y1 = np.abs(x)
# y2 = x ** 3
# y3 = (1/2) ** x

# plt.plot(x, y1, label='|x|', color='red', linestyle=':')
# plt.plot(x, y2, label='x ^ 3', color='blue', linestyle='-')
# plt.plot(x, y3, label='(1/2) ^ x', color='green', linestyle='', marker='.')

# plt.title(loc='center', label='task8', color='black')
# plt.xlabel('X values', fontsize=14, color='red')
# plt.ylabel('Y values', fontsize=14, color='red')
# plt.legend(loc='lower right')
# plt.grid(True)

# plt.savefig('./task8.pdf')
# plt.show()

#task 9
# path = './input_text.txt'
# filter = "aeiouy"

# with open(path, 'r') as file:
#     text = file.read().lower()

# dict = {letter: text.count(letter) for letter in filter}
# plt.figure(figsize=(10, 5))
# plt.bar(dict.keys(), dict.values(), color='red')
# plt.xlabel('Letter', fontsize=14)
# plt.ylabel('Count', fontsize=14)
# plt.savefig('./task9.png')
# plt.show()

#task 10
# dict = {'A': 2310, 'B': 3145, 'C': 1520}

# plt.pie(x=dict.values(), explode=[0.25, 0, 0], labels=dict.keys(), autopct='%1.2f%%')
# plt.title('Валовий прибуток підприємств, тис. грн.', fontsize=14)
# plt.legend(dict.keys(), loc='lower left', title='company')
# plt.savefig('./task10.png')
# plt.show()

#task 11
# dict = {'A': 2310, 'B': 3145, 'C': 1520}

# plt.pie(x=dict.values(), explode=[0.25, 0, 0], labels=dict.keys(), autopct='%1.2f%%', wedgeprops={'width': 0.25})
# plt.title('Валовий прибуток підприємств, тис. грн.', fontsize=14)
# plt.legend(dict.keys(), loc='lower left', title='company')
# plt.savefig('./task11.png')
# plt.show()

#task 12
# dict = {'A': [470, 684, 350, 806], 
#         'B': [787, 586, 980, 792], 
#         'C': [320, 440, 360, 400]}

# quaters = np.array(range(1, 5))
# width = 0.25

# plt.figure(figsize=(10, 5))
# plt.bar(quaters - width, dict['A'], label='A', width=width, color='green')
# plt.bar(quaters, dict['B'], label='B', width=width, color='blue')
# plt.bar(quaters + width, dict['C'], label='C', width=width, color='red')

# plt.xticks(quaters, [str(quat) + ' кв.' for quat in quaters])
# plt.title('Об’єми продажу підприємств, тис. грн.', fontsize=14)
# plt.legend(title='company', loc='upper left')
# plt.savefig('./task12.png')
# plt.show()

#task 13 p1
# dict = {'A': [470, 684, 350, 806], 
#         'B': [787, 586, 980, 792], 
#         'C': [320, 440, 360, 400]}

# quaters = np.array(range(1, 5))
# width = 0.25

# plt.figure(figsize=(10, 5))
# plt.barh(quaters - width, dict['A'], label='A', height=width, color='green')
# plt.barh(quaters, dict['B'], label='B', height=width, color='blue')
# plt.barh(quaters + width, dict['C'], label='C', height=width, color='red')

# plt.yticks(quaters, [str(quat) + ' кв.' for quat in quaters])
# plt.title('Об’єми продажу підприємств, тис. грн.', fontsize=14)
# plt.legend(title='company', loc='lower right')
# plt.savefig('./task13.png')
# plt.show()

#task 13 p2
# dict = {'A': [470, 684, 350, 806], 
#         'B': [787, 586, 980, 792], 
#         'C': [320, 440, 360, 400]}

# quaters = np.array(range(1, 5))

# plt.figure(figsize=(10, 5))
# plt.bar(quaters, dict['A'], label='A', color='green')
# plt.bar(quaters, dict['B'], label='B', bottom=dict['A'], color='blue')
# plt.bar(quaters, dict['C'], label='C', bottom= np.array(dict['A']) + np.array(dict['B']), color='red')

# plt.xticks(quaters, [str(quat) + ' кв.' for quat in quaters])
# plt.title('Об’єми продажу підприємств, тис. грн.', fontsize=14)
# plt.legend(title='company', loc='upper left')
# plt.savefig('./task13p2.png')
# plt.show()
