def doubleElements(list):
    return [x * 2 for x in list]

def squareNotMoreThan(list):
    return [x for x in list if x ** 2 <= 30]

def uniqueElements(list):
    return [x for i, x in enumerate(list) if x not in list[:i]]

#start = int(input("Enter start of list: "))
#end = int(input("Enter end of list: "))

#inputList = list(range(start, end))
#print(inputList)

#print(doubleElements(inputList))
#print(squareNotMoreThan(inputList))
#print(uniqueElements(inputList))

def generateDict(min, max):
    return {str(i): i ** 2 for i in range(min, max) if i % 3 == 0 and i % 5 != 0}

#start = int(input("Enter start of range: "))
#end = int(input("Enter end of range: "))
#print(generateDict(start, end))

from collections.abc import Hashable

def generateSets(input_list):
    return [item for item in input_list if isinstance(item, Hashable)]
      
inputList = [3, 'ok', [1, 2], (True, False), {'flag': 1}]
print(inputList)
print(generateSets(inputList))
