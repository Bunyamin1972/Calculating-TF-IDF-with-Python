import sys
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import html.parser
import pandas as pd
import re

def read_file():
	text = []
	for i in range(1, 6):
		file = open("text/"+ str(i)+".txt", 'r')
		text.append(file.read())
	return(text)

def lower_casing(text):
	text = html.parser.HTMLParser().unescape(text)
	tokenizer = RegexpTokenizer(r'\w+')
	text = tokenizer.tokenize(text.lower())
	number = re.compile(r'[0-9]')
	new_text = [number.sub('', new_text) for new_text in text]
	return new_text

def tokenize_words(text):
	new_text = word_tokenize(text)	
	return new_text

def filter_stopword(word):
	stopWords = set(stopwords.words('english'))
	wordsFiltered = []
	for w in word:
		if w not in stopWords:
			wordsFiltered.append(w)
	return wordsFiltered

def stemming_words(word):
	stemmer = LancasterStemmer()
	word_stem = []
	for w in word:
		word_stem.append(stemmer.stem(w))
	return word_stem

def lemmatization_words(word):
	lemmatizer = WordNetLemmatizer()
	word_lemma = []
	for w in word:
		word_lemma.append(lemmatizer.lemmatize(w))
	return word_lemma

def create_vocabulary(word):
	vocabulary = []
	for i in word:
		vocabulary += set(i)
	return vocabulary

def count_tf(docs,v):
	temp_arr = []
	for doc in docs:
		tf_arr = {}
		total = 0
		for w in v:
			total += doc.count(w)
		for wt in v:
			tf_arr[wt] = round(doc.count(wt) / float(total), 6)
		temp_arr.append(tf_arr)
	return temp_arr

def count_idf(docs,v):
	idf_arr = {}
	for w in v:
		count = 0
		for doc in docs:
			if w in doc :
				count += 1
		idf_arr[w] = count/len(docs)

	return idf_arr

def out_tf(tf_result):
	df = pd.DataFrame(tf_result)
	df.to_csv(sys.stdout)

def out_idf(idf_result):
	df = pd.DataFrame(idf_result)
	df.to_csv(sys.stdout)

def main():
	texts = read_file() 
	words = []
	for i in texts:
		word = lower_casing(i)
		word = filter_stopword(word)
		word = stemming_words(word)
		words.append(word)
	v = create_vocabulary(words)

	out_tf(count_tf(words, v))

if __name__ == '__main__':
	main()