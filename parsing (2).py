import requests
from bs4 import BeautifulSoup
import pymorphy2
import nltk
from nltk.corpus import stopwords
from gensim import corpora, models
import scipy
nltk.download('stopwords')
def parse_site(url, tag, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(tag, class_=class_name)
    return [element.text for element in elements]
def normalize_text(texts):
    morph = pymorphy2.MorphAnalyzer()
    russian_stopwords = set(stopwords.words("russian"))
    normalized_texts = []
    for text in texts:
        words = [word.lower() for word in nltk.word_tokenize(text) if word.isalpha()]
        words = [morph.parse(word)[0].normal_form for word in words]
        words = [word for word in words if word not in russian_stopwords]
        normalized_texts.append(words)
    return normalized_texts
def lda_model(texts, num_topics=5):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)
    return lda
def remove_non_breaking_spaces(text):
    for i in range(len(text)):
        text[i] = text[i].replace('\xa0', ' ')
    return text
url = "https://news.mail.ru/incident/60760659/"
tag = "div"
class_name = "d4d7f9cef4 df068f8f97"

texts = parse_site(url, tag, class_name)
normalized_texts = normalize_text(texts)
print(lda_model(texts))