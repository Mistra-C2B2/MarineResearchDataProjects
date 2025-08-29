from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import num2words


def tokenize(all_text,verbose):
    stop_words = set(stopwords.words('english'))
    punctuations = {'+', ',', '?', '!', '/', '@', '#', '$','.','(',')','[',']',':', '‘','’'}
    
    stemmer = PorterStemmer()

    if(verbose):
    	nr_documents = len(all_text)

    tokens = []
    for i, text in enumerate(all_text):
        all_words = word_tokenize(text)
        all_words = [word.lower() for word in all_words]
        filtered_words = [word for word in all_words if word not in stop_words and word not in punctuations]
        stemmed_words = [stemmer.stem(word) for word in filtered_words]
        add_numbers = [num2words.num2words(int(word)) if word.isdigit() else word for word in stemmed_words]
        tokens.append(add_numbers)
        if(verbose):
        	print(f"tokenizing document:{i + 1} of {nr_documents}")

    return tokens