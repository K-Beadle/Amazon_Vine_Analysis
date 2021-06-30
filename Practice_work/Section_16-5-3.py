import nltk
from nltk import word_tokenize
text = word_tokenize("I have been searching for a job in Data Analytics for around six months now.")
output = nltk.pos_tag(text)
print(output)