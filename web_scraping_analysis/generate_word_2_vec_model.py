"""Module to generate a word 2 vec model using the doc strings generated from a csv file"""

# pylint : disable = import-error
import re
from pickle import Unpickler, Pickler
from typing import Iterator, List

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from gensim.models import Word2Vec
from gensim import downloader
from sklearn.model_selection import train_test_split
import numpy as np


# Should be a csv file that contains at least the columns 'MissionText' and 'WBText'
# filteredMissionStatements.csv is the auto filtered dataset where both the current and
# former mission statements exist, and they are sufficiently different.
CSV_FILENAME = "filteredMissionStatements.csv"

df = pd.read_csv(CSV_FILENAME)

stop_words = set(stopwords.words("english"))

PS = PorterStemmer()


def clean(word: str) -> str:
    """Function that cleans a word"""

    word = re.sub(r"\W+", "", word.lower())

    word = "" if word in stop_words else word

    # word = PS.stem(word)

    return word


def generate_clean_from_iterator(corpus: Iterator[List[str]]) -> List[List[str]]:
    """Function that transforms an iterator of an array of strings into an iteraor of cleaned words.
    Cleaning involves lowering, removing stop words, removing non alpha-numeric characters and stemming"""

    clean_sentences = []

    for words in corpus:

        cleaned_words = [clean(word) for word in words if clean(word)]

        clean_sentences.append(cleaned_words)

    return clean_sentences


# Cleans the mission texts using the clean function, and creates new columns called CleanedMissionText and CleanedWBText
df["CleanedMissionText"] = df.apply(
    lambda x: " ".join([clean(word) for word in x.MissionText if clean(word)]), axis=1
)
df["CleanedWBText"] = df.apply(
    lambda x: " ".join([clean(word) for word in x.WBText if clean(word)]), axis=1
)

# Creates an array, where each element is either a current or former mission text
specific_corpus = list(df["CleanedMissionText"]) + list(df["CleanedWBText"])

# Splits each mission text into its words, to stream to word2vec model generator
specific_corpus = [line.split(" ") for line in specific_corpus]

# Split corpus into two datasets, one for training and one for validation
train_corpus, test_corpus = train_test_split(specific_corpus, random_state=42)

# Initial train on text 8 dataset
with open("clean_wiki_2017", "rb") as wiki_file:
    wiki_corpus = Unpickler(wiki_file).load()

print("Beginning Training")

best_model = None

best_parameter = None

best_score = float("-inf")

for parameter in range(100, 200, 100):

    # Run CBOW on corpus and generate a model
    # model = Word2Vec(
    #     sentences=wiki_corpus,
    #     hs=1,
    #     vector_size=parameter,
    #     window=5,
    #     min_count=1,
    #     workers=4,
    #     epochs=5,
    #     seed=42,
    # )

    model = downloader.load("glove-wiki-gigaword-300")

    print(model.most_similar("mission"))

    # model.train(train_corpus, total_examples=len(train_corpus), epochs=100)

    score = np.mean(model.score(test_corpus))

    if score > best_score:
        best_model = model
        best_score = score
        best_parameter = parameter

        print(
            f"New best score achieved : {best_score:.2f} With Parameter : {best_parameter}"
        )


print(f"Best score achieved : {best_score:.2f} With Parameter : {best_parameter}")

print(best_model.wv.most_similar("mission"))

with open("best_model", "wb") as model_file:
    Pickler(model_file).dump(best_model)
