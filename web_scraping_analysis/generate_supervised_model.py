"""
File to create the logistic regression model used to categorized between
pre and post George Floyd Mission Statements
"""

# Imports

from pickle import Unpickler

from tensorflow import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV files to pull from, must contain columns labeled 'feature' and 'label'
TRAIN_CSV_FILENAME = "train_insertians.csv"
TEST_CSV_FILENAME = "test_insertians.csv"

print("Pulling CSV Data")

train_df = pd.read_csv(TRAIN_CSV_FILENAME)
test_df = pd.read_csv(TEST_CSV_FILENAME)

print("Downloading Word Embedder")

with open("glove-wiki-gigaword-300", "rb") as model_file:
    word2vec_model = Unpickler(model_file).load()
# word2vec_model = downloader.load('glove-twitter-25')


def vector_from_text(text):
    """Function to convert a document to a vector using a pretrained word2vec model"""

    text = str(text)

    embeddings = [
        word2vec_model[word] for word in text.split(" ") if word in word2vec_model
    ]
    if len(embeddings) > 1:
        return np.mean(embeddings, axis=0)
    else:
        return None


print("Embedding Features")

train_features = []
train_labels = []

for feature, label in zip(train_df["feature"], train_df["label"]):

    vector = vector_from_text(feature)

    if vector is not None:

        train_features.append(vector)

        train_labels.append(label)

test_features = []
test_labels = []

for feature, label in zip(test_df["feature"], test_df["label"]):

    vector = vector_from_text(feature)

    if vector is not None:

        test_features.append(vector)

        test_labels.append(label)

print("Building Model")

model = keras.Sequential()
model.add(keras.Input(shape=(300,)))
model.add(keras.layers.Dense(150))
model.add(keras.layers.ReLU(negative_slope = 0.05))
model.add(keras.layers.Dense(75))
model.add(keras.layers.ReLU(negative_slope = 0.05))
model.add(keras.layers.Dense(40))
model.add(keras.layers.ReLU(negative_slope = 0.05))
model.add(keras.layers.Dense(20))
model.add(keras.layers.ReLU(negative_slope = 0.05))
model.add(keras.layers.Dense(10))
model.add(keras.layers.ReLU(negative_slope = 0.05))
model.add(keras.layers.Dense(5))
model.add(keras.layers.ReLU(negative_slope = 0.05))
model.add(keras.layers.Dense(1))

print("Compiling Model")

model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=['accuracy', 'mse']
)

print("Fitting Model")

history = model.fit(
    np.array(train_features),
    np.array(train_labels),
    batch_size=4,
    epochs=100,
    shuffle = True,
    validation_data = (np.array(test_features), np.array(test_labels)),
    validation_freq = 1,
)

print("Evaluating Model")

print(history.history.keys())
print(f"loss = {history.history['loss']}")
print(f"accuracy = {history.history['accuracy']}")
print(f"val_loss = {history.history['val_loss']}")
print(f"val_accuracy = {history.history['val_accuracy']}")

plt.plot(range(100), history.history['accuracy'], label="train")
plt.plot(range(100), history.history['val_accuracy'], label="test")
plt.xlabel("eopch")
plt.ylabel("accuracy")
plt.legend()
plt.savefig("NN_accuracy_insertians.png")

# train_scores = []
# test_scores = []

# parameters = np.linspace(0.01, 1, num=50)

# for parameter in parameters:



#     train_scores.append(logistic_model.score(train_features, train_labels))
#     test_scores.append(logistic_model.score(test_features, test_labels))

#     print(f"Parameter = {parameter} | test_score = {test_scores[-1]}")

# plt.plot(parameters, train_scores, label="train")
# plt.plot(parameters, test_scores, label="test")
# plt.xlabel("C")
# plt.ylabel("accuracy")
# plt.legend()
# plt.savefig("C_accuracy_insertians.png")
