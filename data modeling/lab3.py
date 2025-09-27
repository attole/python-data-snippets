import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pymorphy3 as p3
from uk_stemmer import UkStemmer
import regex as re
import random as rnd
import string

# task 1
# path = 'cache/5_sentences.txt'
# vowels = 'aeiou'

# with open(path, 'r') as file:
#     text = file.read()
#     print('\n', text)

#     words = [word for word in tk.word_tokenize(text) if re.match(r'\w+', word)]
#     print('\nnumber of words: ', len(words))

#     vowels_starts = [word for word in words if word.lower()[0] in vowels]
#     print('\nwords, that starts with vowel: ', vowels_starts, '\namount: ', len(vowels_starts))

#     three_words = [words[rnd.randint(0, len(words) - 1)] for _ in range(3)]
#     print('\nthree words: ', three_words)
#     # positions??

#     old_word = words[rnd.randint(0, len(words) - 1)]
#     new_word = 'Kucherenko'
#     text = re.sub(r'\b' + old_word + r'\b', new_word, text)
#     print('\nthat chosen one word: ', old_word, '\nnew word: ', new_word, '\nchanged text: ', text)

# task 2
# path = 'cache/6_words.txt'

# with open(path, 'r') as file:
#     text = file.read()
#     print('\n', text)
#     words = [word for word in tk.word_tokenize(text) if re.match(r'\w+', word)]
#     letters = [letter for word in words for letter in word]
#     print('\nall letters: ', letters, '\ncount: ', len(letters))

#     print('\nfirst 2 letter of each word: ', [word[0:min(2, len(words))] for word in words])

#     with_exluded_letters = [letter for letter in letters if letter not in ('a', 'b')]
#     print("\nlist of letters without 'a' and 'b': ", with_exluded_letters, '\ncount: ', len(with_exluded_letters))

# task 3
# path = 'cache/languages.txt'
# regex = r'[A-za-z\+\#]+'

# with open(path, 'r') as file:
#     text = file.read()
#     print('\n', text)
#     languages = (re.findall(regex, text))
#     print('programming languages: ', languages)

# task 4
# path = 'cache/emails.txt'
# regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# with open(path, 'r') as file:
#     text = file.read()
#     print('\n', text)
#     emails = re.findall(regex, text)
#     print('all emails: ', emails)

# task 5
# path = 'cache/fives.txt'
# regex = r'5{2,3}'

# with open(path, 'r') as file:
#     text = file.read()
#     print('\n', text)
#     numbers = [number for number in text.split(' ') if re.search(regex, number)]
#     print('numbers with 2-3 fives in them: ', numbers)

# task 6
# path = 'cache/dates.txt'
# regex_time = r'\d{2}:\d{2}:\d{2}'
# regex_date = r'\d{4}-\d{2}-\d{2}'

# with open(path, 'r') as file:
#     text = file.read()
#     print('\n', text)
#     dates = re.findall(regex_date, text)
#     times = re.findall(regex_time, text)
#     print('time: ', times)
#     print('dates: ', dates)
#     print('\nhours: ', [time[0:2] for time in times])
#     print('years: ', [date[0:4] for date in dates])

# task 7
# path = 'cache/indexes.txt'
# regex = r'0\d{4}'

# with open(path, 'r') as file:
#     text = file.read()
#     print('\n', text)
#     indexes = re.findall(regex, text)
#     print('indexes: ', indexes)

# task 8, 9, 10
# path = 'cache/english_text.txt'
# stop_words_path = 'cache/stop_words.txt'

# with open(path, 'r')  as file, open(stop_words_path, 'r') as stop_words_file:
#     text = file.read().lower()
#     print('\n', text)

#     stop_words = stop_words_file.read().lower().split('\n')
#     print('\nstop words:', stop_words)

#     sentences = tk.sent_tokenize(text)
#     words = tk.word_tokenize(text)
#     print('\nsentences: ', sentences)
#     print('\nwords: ', words)

#     filtered_words = [word for word in words if word not in string.punctuation and word not in stop_words]
#     print('\nfiltered words: ', filtered_words)   

#     tagged_words = nltk.pos_tag(filtered_words)
#     print('\nwords and their types: ', tagged_words)

#     print('\nTASK 9:')
#     print('words count per sentence (№, count): ', [(i + 1, len(sentences[i])) for i in range(0, len(sentences))])
#     print('stop words count for all text: ', len([word for word in words if word in stop_words]))

#     longest_word = max(words, key=len)
#     print('longest word:', longest_word, '; lenght: ', len(longest_word))

#     words_with_lenght_4 = [word for word in words if len(word) == 4]
#     print('amount of words of 4 symbol lenght: ', len(words_with_lenght_4), '; words: ', words_with_lenght_4)

#     print('\nTASK10')
#     lem = WordNetLemmatizer()
#     lem_words = [lem.lemmatize(word) for word in filtered_words]
#     print('\nLemmed words:', lem_words)

#     stem = PorterStemmer()
#     stem_words = [stem.stem(word) for word in filtered_words]
#     print('\nStemmed words:', stem_words)

# task 11
# path = 'cache/45_words.txt'
# stop_words_path = 'cache/стоп_слова_українська_мова.txt'

# with open(path, 'r', encoding='utf-8')  as file, open(stop_words_path, 'r', encoding='utf-8') as stop_words_file:
#     text = file.read().lower()
#     print('\n', text)

#     stop_words = stop_words_file.read().lower().split('\n')
#     print('\nstop words:', stop_words)

#     words = tk.word_tokenize(text)
#     print('\nwords: ', words)

#     filtered_words = [word for word in words if word not in string.punctuation and word not in stop_words]
#     print('\nfiltered words: ', filtered_words)   

#     print('\nstatistics:')
#     print('words count: ', len(words))

#     punctuation_list = [word for word in words if word in string.punctuation]

#     print('punctuation count: ', len(punctuation_list))
#     print('stop words count: ', len(words) - len(filtered_words) - len(punctuation_list))
#     print('filtered words count: ', len(filtered_words))

#     lem = p3.MorphAnalyzer(lang='uk')
#     lem_words = [lem.parse(word)[0].normal_form for word in filtered_words]
#     print('\nLemmed words:', lem_words)

#     stem = UkStemmer()
#     stem_words = [stem.stem_word(word) for word in filtered_words]
#     print('\nStemmed words:', stem_words)
