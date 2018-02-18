import sys
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import html.parser

def read_file():
	text_raw = ''
	for line in sys.stdin:
		text_raw += line
	return text_raw

def lower_casing(text):
	text = html.parser.HTMLParser().unescape(text)
	tokenizer = RegexpTokenizer(r'\w+')
	return tokenizer.tokenize(text.lower())

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
	word_lemma=[]
	for w in word:
		word_lemma.append(lemmatizer.lemmatize(w))
	return word_lemma

def create_vocabulary(word):
	vocabulary = set(word)
	return vocabulary

def count_tf(text):
	pass

def count_idf(text):
	pass

def main():
	text = read_file()
	word = lower_casing(text)
	#word = tokenize_words(text)
	word = filter_stopword(word)
	word = stemming_words(word)
	# print(lemmatization_words(word))
	v = create_vocabulary(word)
	i = 0
	for w in v:
		if w in word:
			i += 1
			print(i, w,word.count(w)) 


if __name__ == '__main__':
	main()