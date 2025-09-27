def print_ascii_from_range(n, m):
    for code in range(n, m + 1):
        print(f"{chr(code)} {code}")
# n = int(input("Enter  the starting code (n): "))
# m = int(input("Enter the ending code (m): "))
# print_ascii_from_range(n, m)

def print_char_and_index(input_str):
    print("Index\tCharacter")
    for index, char in enumerate(input_str):
        print(f"{index}\t{char}")
# user_input = input("Enter a string: ")
# print_char_and_index(user_input)
        
films = [
    ("Film 1", 5.0),
    ("Film 2", 9.9),
    ("Film 3", 4.6),
    ("Film 4", 9.5),
    ("Film 5", 6.6)
]

def sort(films):
    return sorted(films, key=lambda x: x[1])
#print("Sorted films by rating:")
#for film in sort(films):
    #print(f"{film[0]}\t{film[1]}")

def generate_square_tuple(n):
    new_tuple = tuple(x ** 2 for x in range(1, n + 1))
    return new_tuple
# n = int(input("Enter n: "))
# result_tuple = generate_square_tuple(n)
# print("A tuple with values of squares of numbers: ", result_tuple)

def check_f_or_l_equal(list1, list2):
    if list1 and list2:
        return list1[0] == list2[0] or list1[-1] == list2[-1]
    else:
        return False

list1 = [1, 2, 3, 4]
list2 = [3, 2, 1]
list3 = [1, 3, 2, 4]
# print(check_f_or_l_equal(list1, list2))
# print(check_f_or_l_equal(list1, list3))

def create_sublists(input_list):
    return [list(range(num + 1)) for num in input_list]

input_list = [1, 2, 3, 4]
output_list = create_sublists(input_list)
# print("Result: ", output_list)

def merge_dictionaries(dict1, dict2):
   merged_dict = {key: dict1.get(key, 0) + value for key, value in dict1.items()}
   merged_dict.update({key: dict2.get(key, 0) + value for key, value in dict2.items()})
   return merged_dict

dict1 = {'a': 200, 'b': 50}
dict2 = {'a': 200, 'c': 50}
merged_dict = merge_dictionaries(dict1, dict2)
# print("Result: ", merged_dict)

def events_on_exact_date(dict, date):
    if date in dict:
        return dict[date]
    else:
        return []

events = {
    '2024-05-10': ['Something', 'Something2'],
    '2024-01-13': ['Anything', 'Anything2'],
    '2024-04-15': ['Nothing', 'Nothing2']
}


date_input = input("Enter exact date (YYYY-MM-DD): ")

events_for_date = events_on_exact_date(events, date_input)

if events_for_date:
    print(f"Events on {date_input}:")
    for event in events_for_date:
        print(event)
else:
    print("No events for this exact date.")
