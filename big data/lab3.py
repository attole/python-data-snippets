import re
from bs4 import BeautifulSoup, Tag
import requests
import json
from typing import List, Dict

"""
1. Написати програму, яка зчитує введений текст і записує у
вихідний файл ті слова, які є найдовшими, не змінюючи їх порядок.
"""
def takeLongest(path, output_path, percent) -> None:
    with open(path, 'r', encoding='utf-8') as textFile:
        words = [word.strip() 
                 for line in textFile 
                 for word in line.split(' ') 
                 if re.search('[a-zA-Z]', word)]
        take_count = int(len(words) * percent) if int(len(words) * 0.1) > 5 else 3
        words.sort(key=lambda word: len(word), reverse=True)
        result = '\n'.join(words[:take_count])

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(result)
            print('Data was written to file')

output_path = 'D://Coding//code_sources//python_lab3//testResult.txt'
base_path = 'D://Coding//code_sources//python_lab3//test.txt'
#takeLongest(base_path, output_path, 0.1)


"""
2. Написати програму, яка приймає посилання на сторінку з
розкладом студентів і повертає шлях до файлу JSON, в якому збережені всі
можливі дані про розклад за отриманим посиланням. Можна використовувати
спеціалізований синтаксичний аналізатор для HTML (BeatifulSoup, lxml та
інші).
"""

def getSchedule(path) -> None:
    url = 'http://education.kpi.ua/Schedules/ViewSchedule.aspx?g=4e1262aa-fcd0-43c6-a9ec-c656bc81a3d3'
    page = requests.get(url)
    if(page.status_code != 200):
        print('Page was not loaded succesfully - ', page.status_code)
        return
    
    soup = BeautifulSoup(page.content, "html.parser")
    first_schedule_table = soup.find("table", { "id": "ctl00_MainContent_FirstScheduleTable"})
    second_schedule_table = soup.find("table", { "id": "ctl00_MainContent_SecondScheduleTable"})
    result = []

    def getDataPerTable(table: Tag):
        for row in table.find_all("tr"):
            cells: List[Tag] = row.find_all("td")
            cells = [cell.get_text(separator=' ', strip=True) 
                     for cell in cells 
                     if cell.text != '']
            if(len(cells) > 1):
                nonlocal result
                result.append(cells)    

    getDataPerTable(first_schedule_table)
    getDataPerTable(second_schedule_table)

    json_result = json.dumps(result, ensure_ascii=False, indent=4)
    with open(path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_result)
        print('Data was written to file')

base_path = 'D://Coding//code_sources//python_lab3//test.json'
#getSchedule(base_path)


"""
3. Написати програму, яка приймає шлях до двох файлів і повертає
кількість однакових позицій у файлах.
"""

def getIntersection(paths) -> set[str]:
    data = []
    for path in paths:
        with open(path, 'r', encoding='utf-8') as textFile:
            data.append([line.strip() 
                         for line in textFile 
                         if line.strip() != ''])

    result = set(data[0]).intersection(*data[1:])
    return json.dumps(list(result), ensure_ascii=False, indent=4)
    
path1 = 'D://Coding//code_sources//python_lab3//test.txt'
path2 = 'D://Coding//code_sources//python_lab3//test2.txt'
#print(getIntersection([path1, path2]))


"""
4. У файлі записані дані про результати складання екзамену. Кожен
рядок містить прізвище, ім'я та кількість балів, розділені пробілами:
<Прізвище> <Ім'я> <Кількість балів>. Написати програму, яка запише в інший
файл прізвища та імена тих студентів, які отримали понад 85 балів.
"""

def getHighGrades(path, grade, output_path) -> None:
    dict = {}
    with open(path, 'r', encoding='utf-8') as textFile:
        for line in textFile:
            key = ' '.join(line.split(' ')[:2])
            score = int(line.rstrip().split(' ')[2])
            dict[key] = score

    output_list = [key for key, value in dict.items()
                   if value >= grade]
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(output_list))
        print('Data was written to file')
    
base_path = 'D://Coding//code_sources//python_lab3//students.txt'
output_path = 'D://Coding//code_sources//python_lab3//studentsResult.txt'
#getHighGrades(base_path, 85, output_path)


"""
5. Написати програму, яка отримує інформацію з файлу, який є
базою даних про продажі інтернет-магазину. Кожен рядок вхідного файлу є
записом виду Покупець Товар Кількість, де Покупець - ім’я покупця (рядок
без пропусків), Товар - назва товару (рядок без пропусків), Кількість - кількість
придбаних одиниць товару. Створіть список всіх покупців, а для кожного
покупця підрахуйте кількість придбаних ним одиниць кожного виду товарів.
Вводяться відомості про покупки в зазначеному форматі як у вхідних даних.
Виведіть список всіх покупців в лексикографічному порядку, після імені
кожного покупця виведіть двокрапку, потім виведіть список назв всіх
придбаних даними покупцем товарів в лексикографічному порядку, після
назви кожного товару виведіть кількість одиниць товару, придбаних даними
покупцем. Інформація про кожен товар виводиться в окремому рядку.
"""

def rewriteData(path) -> str:
    dict: Dict[str, Dict[str, int]]= {}
    with open(path, 'r', encoding='utf-8') as textFile:
        for line in textFile:
           buyer, goods, amount = line.strip().split(' ')
           amount = int(amount.rstrip())

           dict.setdefault(buyer, {}).setdefault(goods, 0)
           dict[buyer][goods] += amount

    return json.dumps(dict, ensure_ascii=False, indent=4)
    
base_path = 'D://Coding//code_sources//python_lab3//sells.txt'
#print(rewriteData(base_path))