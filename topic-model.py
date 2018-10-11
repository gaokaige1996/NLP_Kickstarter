import numpy as np
import lda
import lda.datasets
import os
import sys
import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
import pandas as pd

#X = np.genfromtxt("/Users/mia/Desktop/10risk.txt", skip_header=1, dtype=np.int)

corpus = []
for line in open('techwords.txt', 'r').readlines():
     #print(line)
     corpus.append(line.strip())

vectorizer = CountVectorizer()
print(vectorizer)

X = vectorizer.fit_transform(corpus)
analyze = vectorizer.build_analyzer()
weight = X.toarray()

print(len(weight))
print(weight[:5, :5])

print('LDA:')
model = lda.LDA(n_topics=10, n_iter=500, random_state=1)
model.fit(np.asarray(weight))     # model.fit_transform(X) is also available
topic_word = model.topic_word_    # model.components_ also works

doc_topic = model.doc_topic_
print("type(doc_topic): {}".format(type(doc_topic)))
print("shape: {}".format(doc_topic.shape))
label = []
for n in range(1890):
     topic_most_pr = doc_topic[n].argmax()
     label.append(topic_most_pr)
     #print("doc: {} topic: {}".format(n, topic_most_pr))
     #print(n,topic_most_pr)
#输出主题中的TopN关键词
word = vectorizer.get_feature_names()
#for w in word:
   # print(w)
#print(type(topic_word))
n = 20
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(word)[np.argsort(topic_dist)][:-(n+1):-1]
    print(u'*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

with open('techlabel.txt','w') as f:
    for i in label:
        f.write(str(i))
        f.write('\n')

#matrix = pd.DataFrame(doc_topic)
#matrix.to_csv('techmatrix.csv')
