import nltk
import re
from nltk.corpus import stopwords
set(stopwords.words('english'))
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

def process(example_sent):
    #example_sent = "This is a sample sentence, showing off the stop words filtration. eye, ate, apple"
#change to lower
    example_sent = example_sent.lower()
#remove special character
    example_sent = example_sent.replace(',', '')
    example_sent = example_sent.replace('.', '')
    example_sent = example_sent.replace('\n', '')
    example_sent = example_sent.strip()
    example_sent = re.sub(r'[^\w\s]', ' ', example_sent)
    stop_words = set(stopwords.words('english'))
#seperate words
    word_tokens = word_tokenize(example_sent)

#remove stop words and lenghth less than 3
    #filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words and len(w)>=3:
            filtered_sentence.append(w)
# steeming
    sentence_stemmed = []
    ps = PorterStemmer()
    for i in filtered_sentence:
        a = ps.stem(i)
        sentence_stemmed.append(a)
#print(word_tokens)
    #example_sent = sentence_stemmed
   # word = ''.join(map(str, sentence_stemmed))


    word = ' '.join(sentence_stemmed)
    return word

with open('techwords.txt','w') as f:
   for line in open('techresult.txt', 'r').readlines():
       #print(line)
       f.write(process(line))
       f.write('\n')

