"""File to clean a file and produce two csv files to be used in Logistic Regression Classification"""

# Imports

import re

import pandas as pd
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split

pattern = re.compile(r"[^a-zA-Z\d]+")

stop_words = stopwords.words("english")


def clean_text(text):
    """Function to clean a mission statement to help model"""

    clean_words = []

    text = str(text).lower()

    for word in text.split(" "):

        word = pattern.sub("", word)

        if word not in stop_words and len(word) > 1:

            clean_words.append(word)

    return " ".join(clean_words)


FROM_CSV_FILENAME = "insertians.csv"

TO_TRAIN_CSV_FILENAME = "train_insertians.csv"
TO_TEST_CSV_FILENAME = "test_insertians.csv"

df = pd.read_csv(FROM_CSV_FILENAME)

df["CleanedInsertians"] = df.apply(lambda x: clean_text(x.insertians), axis=1)
df["CleanedDeletians"] = df.apply(lambda x: clean_text(x.deletians), axis=1)

features = list(df["CleanedInsertians"]) + list(df["CleanedDeletians"])

labels = [0] * df.shape[0] + [1] * df.shape[0]

labeled_df = pd.DataFrame(data={"label": labels, "feature": features})

train_labeled_df, test_labeled_df = train_test_split(labeled_df)

train_labeled_df.to_csv(TO_TRAIN_CSV_FILENAME, index=False)
test_labeled_df.to_csv(TO_TEST_CSV_FILENAME, index=False)
