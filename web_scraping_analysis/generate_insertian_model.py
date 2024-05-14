"""
File to create the logistic regression model used to categorized between
insertians and deletians pre and post George Floyd
"""

# Imports

from pickle import Unpickler

from sklearn.linear_model import LogisticRegression
import pandas as pd
from gensim import downloader
import numpy as np
import matplotlib.pyplot as plt