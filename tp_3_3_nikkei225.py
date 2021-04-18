# -*- coding: utf-8 -*-
"""TP 3.2 Nikkei225.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ulzTgZCZoA_Nb6BhT3mg4mwKv0GRZzS9
"""

from sklearn.model_selection import train_test_split
import pandas as pd
import tensorflow
from tensorflow import keras
from tensorflow.keras import layers
from keras.utils.vis_utils import plot_model
import random, numpy
from numpy.random import seed

SEED = 12345

df = pd.read_excel('Data for NN Nikkei225.xlsx')
df.index = pd.to_datetime(df.Date)
df.drop(['Date'], axis='columns', inplace=True)
df.head()

X = df.copy()
Y = X.pop('Y')
X_train, X_valid, y_train, y_valid = train_test_split(X, Y, train_size=0.75, random_state=42, shuffle=False)

X_train.tail()

X_valid.head()

y_train

y_valid

input_shape = [X_train.shape[1]]
input_shape

def neural_network(nodes_first, nodes_second, batch, dropout_include, SEED, X_train, y_train, X_valid, y_valid, count, rate_=None):
  from tensorflow.python.framework import ops
  ops.reset_default_graph()

  seed(SEED)
  tensorflow.random.set_seed(SEED)
  random.seed(SEED)
  numpy.random.seed(SEED)

  if dropout_include==False:
      model = keras.Sequential([
          layers.Dense(nodes_first, activation='relu'),
          layers.Dense(nodes_second, activation='relu'),  
          layers.Dense(1, activation='sigmoid')
      ])
  else:
      model = keras.Sequential([
          layers.Dense(nodes_first, activation='relu'),
          layers.Dropout(rate=rate_),
          layers.Dense(nodes_second, activation='relu'),
          layers.Dropout(rate=rate_),    
          layers.Dense(1, activation='sigmoid')
      ])

  model.compile(
      optimizer='adam',
      loss='binary_crossentropy',
      metrics=['binary_accuracy'])

  early_stopping = keras.callbacks.EarlyStopping(
      patience=4,
      min_delta=0.001,
      restore_best_weights=False,
  )

  history = model.fit(
      X_train, y_train,
      validation_data=(X_valid, y_valid),
      batch_size=batch,
      epochs=40,
      verbose=0,
      callbacks=[early_stopping]
  )

  print("model "+str(count) + ":"+
        " nodes_first= "+str(nodes_first)+
        ", nodes_second=" + str(nodes_second) +
        ", batch=" + str(batch) +
        ", dropout_include=" + str(dropout_include) +
        ", rate=" + str(rate_) +
        ". Binary accuracy: " + str(history.history['binary_accuracy'][-1]))
  
  return (history.history['binary_accuracy'][-1])

i = 0
accuracy_list = []
for dropout_include in [True, False]:
  for batch in [64, 128, 256, 512, 1024]:
    for nodes_first in [4, 8, 16, 32]:
      for nodes_second in [4, 8, 16, 32]:
        if dropout_include == True:
          for rate__ in [0.2, 0.3, 0.4, 0.5]:
            acc = neural_network(nodes_first, nodes_second, batch, dropout_include, SEED, X_train, y_train, X_valid, y_valid, i, rate_=rate__)
            i=i+1
            accuracy_list.append(acc)
        else:
          acc = neural_network(nodes_first, nodes_second, batch, dropout_include, SEED, X_train, y_train, X_valid, y_valid, i)
          i=i+1
          accuracy_list.append(acc)

sorted(range(len(accuracy_list)), key=lambda x: accuracy_list[x])[-5:]

"""# Top-5 models

model 360: nodes_first= 16, nodes_second=4, batch=256, dropout_include=False, rate=None. Binary accuracy: 0.5480209589004517

model 252: nodes_first= 32, nodes_second=32, batch=512, dropout_include=True, rate=0.2. Binary accuracy: 0.543364405632019

model 383: nodes_first= 32, nodes_second=32, batch=512, dropout_include=False, rate=None. Binary accuracy: 0.5430733561515808

model 332: nodes_first= 32, nodes_second=4, batch=64, dropout_include=False, rate=None. Binary accuracy: 0.5419092178344727

model 339: nodes_first= 4, nodes_second=32, batch=128, dropout_include=False, rate=None. Binary accuracy: 0.521536648273468
"""

def neural_network_analysis(nodes_first, nodes_second, batch, dropout_include, SEED, X_train, y_train, X_valid, y_valid, count, rate_=None):
  from tensorflow.python.framework import ops
  ops.reset_default_graph()

  seed(SEED)
  tensorflow.random.set_seed(SEED)
  random.seed(SEED)
  numpy.random.seed(SEED)

  if dropout_include==False:
      model = keras.Sequential([
          layers.Dense(nodes_first, activation='relu'),
          layers.Dense(nodes_second, activation='relu'),  
          layers.Dense(1, activation='sigmoid')
      ])
  else:
      model = keras.Sequential([
          layers.Dense(nodes_first, activation='relu'),
          layers.Dropout(rate=rate_),
          layers.Dense(nodes_second, activation='relu'),
          layers.Dropout(rate=rate_),    
          layers.Dense(1, activation='sigmoid')
      ])

  model.compile(
      optimizer='adam',
      loss='binary_crossentropy',
      metrics=['binary_accuracy'])

  early_stopping = keras.callbacks.EarlyStopping(
      patience=4,
      min_delta=0.001,
      restore_best_weights=False,
  )

  history = model.fit(
      X_train, y_train,
      validation_data=(X_valid, y_valid),
      batch_size=batch,
      epochs=40,
      verbose=0,
      callbacks=[early_stopping]
  )

  print("model "+str(count) + ":"+
        " nodes_first= "+str(nodes_first)+
        ", nodes_second=" + str(nodes_second) +
        ", batch=" + str(batch) +
        ", dropout_include=" + str(dropout_include) +
        ", rate=" + str(rate_) +
        ". Binary accuracy: " + str(history.history['binary_accuracy'][-1]))
  
  history_df = pd.DataFrame(history.history)
  # history_df.loc[:, ['loss', 'val_loss']].plot(title="Cross-entropy", colormap='bwr')

  # print(history_df.loc[:, ['loss', 'val_loss']].head())

  # history_df.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot(title="Accuracy", colormap='bwr')

  # plot_model(model, to_file="model.png", show_shapes=True, show_layer_names=True)
  return model.predict(X_valid)

# model 360: nodes_first= 16, nodes_second=4, batch=256, dropout_include=False, rate=None. Binary accuracy: 0.5480209589004517

# model 252: nodes_first= 32, nodes_second=32, batch=512, dropout_include=True, rate=0.2. Binary accuracy: 0.543364405632019

# model 383: nodes_first= 32, nodes_second=32, batch=512, dropout_include=False, rate=None. Binary accuracy: 0.5430733561515808

predictions = neural_network_analysis(16, 4, 256, False, SEED, X_train, y_train, X_valid, y_valid, 360)
# predictions
output_data = pd.DataFrame(y_valid)
# output_data.columns = ["Predictions"]
output_data['Prediction 1'] = predictions
output_data

predictions = neural_network_analysis(32, 32, 512, True, SEED, X_train, y_train, X_valid, y_valid, 252, rate_=0.2)
# predictions
output_data['Prediction 2'] = predictions
output_data

predictions = neural_network_analysis(32, 32, 512, False, SEED, X_train, y_train, X_valid, y_valid, 383)
# predictions
output_data['Prediction 3'] = predictions
output_data

print(len(predictions))
print(len(X_valid))

output_data.to_excel('Nikkei225 output 1.xlsx')

