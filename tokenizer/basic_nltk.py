import nltk
from nltk.tokenize import sent_tokenize
import nltk.data
from nltk.tokenize import word_tokenize

from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import RegexpTokenizer


#nltk.download('punkt_tab')

# Sentence Tokenization
text = "Hello everyone. This is a test sentence. Let's see how it works"
result = sent_tokenize(text)
print(result)


tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')

print(tokenizer.tokenize(text))

# Word Tokenization
text = "Hello everyone. This is a test sentence. Let's see how it works"
result = word_tokenize(text)
print(result)

result = TreebankWordTokenizer().tokenize(text)
print(result)

# Punctution based word Tokenization
result = WordPunctTokenizer().tokenize(text)
print(result)
