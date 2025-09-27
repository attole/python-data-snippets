import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import gutenberg, stopwords
import string
import math
import matplotlib.pyplot as plt 

# task 1-5

def calculate_tf(unique_lems: list[str], all_lems: list[str]) -> dict[str, float]:
    tf_dict = {u_lem: round(all_lems.count(u_lem) / len(all_lems), 3) for u_lem in unique_lems}
    print('\ntf data:', tf_dict)
    return tf_dict

def get_unique(all_lems: list[str]) -> list[str]:
    unique_lems = list(set(all_lems))
    print('\nunique words (bag of words):', unique_lems, '\ncount:', len(unique_lems))
    return unique_lems

def prepare_text(text_path: str, stop_words_path: str) -> list[str]:
    with open(text_path, 'r') as file1, open(stop_words_path, 'r') as file2:
        text = file1.read().lower()
        print('text:\n', text)

        stop_words = file2.read().lower()
        words = [word for word in tk.word_tokenize(text) if 
                 word not in string.punctuation and 
                 word not in stop_words]
        
        lemmatizer = WordNetLemmatizer()
        lems = [lemmatizer.lemmatize(word) for word in words]

        print('\nfiltered words:', lems, '\ncount:', len(lems))
        return lems


text_paths = ['./cache/4_sentences_main.txt', 
         './cache/4_sentences_1.txt', 
         './cache/4_sentences_2.txt', 
         './cache/4_sentences_3.txt']

stop_words_path = './cache/stop_words.txt'

main_text_filtered = prepare_text(text_paths[0], stop_words_path)
main_text_unique = get_unique(main_text_filtered)
tf_data = calculate_tf(main_text_unique, main_text_filtered)

docs_data = [get_unique(prepare_text(path, stop_words_path)) for path in text_paths[1:]]
docs_data.append(main_text_unique)

print('\nTASK 3:')
idf_dict: dict[str, float] = {}
docs_count = len(docs_data)

for lem in tf_data:
    needed_docs_count = sum(1 for doc in docs_data if lem in doc)
    idf_dict[lem] = round(math.log10(docs_count / needed_docs_count), 3)

print('\nidf data:', idf_dict)

print('\nTASK 4:')
tf_idf_data = {key: round(idf_dict[key] * tf_data[key], 3) for key in sorted(tf_data)}
print('\ntf_idf data:', tf_idf_data)

print('\nTASK 5:')
plt.figure(figsize=(10, 5))
plt.bar(tf_idf_data.keys(), tf_idf_data.values(), color='red')

plt.subplots_adjust(bottom=0.25)

plt.title('statistical measure of importance evaluation of words', fontsize=14)
plt.xlabel('words', fontsize=12)
plt.ylabel('tf-idf', fontsize=12)
plt.xticks(rotation=90)

plt.show()
    
# task 6, 7
#nltk.download('gutenberg')
#nltk.download('stopwords')

hamlet_text = gutenberg.words('shakespeare-hamlet.txt')
filtered_hamlet_text = [word.lower() for word in hamlet_text 
                        if word.lower() not in stopwords.words('english') 
                        and word not in string.punctuation]

lemmatizer = WordNetLemmatizer()
lems = [lemmatizer.lemmatize(word) for word in filtered_hamlet_text]

nltk_hamlet_lems = nltk.Text(lems)
nltk_hamlet_lems_count = len(nltk_hamlet_lems)
print('all words count:', nltk_hamlet_lems_count)
print('first 25 words of hamlet:', nltk_hamlet_lems.tokens[0:25])

unique_hamlet_lems = list(set(nltk_hamlet_lems))
print('\nunique words count:', len(unique_hamlet_lems))
print('25 unique words:', unique_hamlet_lems[0:25])

special_words = ['Hamlet', 'Horatio', 'Ghost', 'Polonius']
special_words = [lemmatizer.lemmatize(word.lower()) for word in special_words]

tf_data = {word: round(nltk_hamlet_lems.count(word) / nltk_hamlet_lems_count, 5) for word in special_words}
print('tf data for special words:', tf_data)

nltk_hamlet_lems.dispersion_plot(special_words)
plt.show()

print('\nTASK7')
hapaxes = nltk.FreqDist(nltk_hamlet_lems).hapaxes()
print('amount of words that occur once:', len(hapaxes))
print('25 words, that occurs once:', hapaxes[0:25])

words_lenghts = [len(word) for word in filtered_hamlet_text]

freq_lenght_dict = {lenght: words_lenghts.count(lenght) for lenght in set(words_lenghts)}

most_freq_lenght = max(freq_lenght_dict, key=freq_lenght_dict.get)
print('\nmost frequent word lenght:', most_freq_lenght)

fdist_lenghts = nltk.FreqDist(words_lenghts)
fdist_lenghts = {str(key): fdist_lenghts[key] for key in sorted(fdist_lenghts)}

plt.figure(figsize=(10, 5))
plt.bar(fdist_lenghts.keys(), fdist_lenghts.values(), color='red')
plt.ylim(2, 4000)
plt.xlabel('Words', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Frequency Distribution', fontsize=14)
plt.savefig('./cache/words_lenght_ds.png')
plt.show()