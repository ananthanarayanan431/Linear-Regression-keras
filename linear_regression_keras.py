# -*- coding: utf-8 -*-
"""linear_regression_keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l9tPfeiFooSSjuvSxqDsx9K_gv7Z0ehk
"""

!pip install keras

import pandas as pd
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

Data = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DL0101EN/labs/data/concrete_data.csv')
Data.head(5)

Data.shape

predictor = Data.iloc[:,:Data.shape[1]-1]
predictor

target = Data['Strength']
target

Data.describe

Data.isnull().sum()

predictor.head()

target.head()

predictors_norm = (predictor - predictor.mean()) / predictor.std()
predictors_norm

model = Sequential()

col = predictors_norm.shape[1]

model.add(Dense(50,activation="relu",input_shape=(col,)))

model.add(Dense(50,activation="relu"))
model.add(Dense(1))
model.compile(optimizer="adam",loss="mean_squared_error")

model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)

