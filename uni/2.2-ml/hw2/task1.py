import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from keras import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
from keras.metrics import Accuracy, Recall, Precision
import keras.backend as K
from sklearn.preprocessing import OneHotEncoder

# import tensorflow as tf
# from tensorflow.keras.metrics import F1Score


def my_f1_score(y_true, y_pred):
    # precision = K.cast(Precision().update_state(y_true, y_pred), 'float32').result().numpy()
    # recall = K.cast(Recall().update_state(y_true, y_pred), 'float32').result().numpy()
    #
    # return 2*((precision*recall)/(precision+recall+K.epsilon()))

    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2 * (precision * recall) / (precision + recall + K.epsilon())
    return f1_val

RANDOM_STATE = 123
VERBOSITY = 2

df = pd.read_csv(f"task 1.csv", index_col=0).sort_index()

y = df.pop("user_id")
y = y.apply(lambda x: 1 if x == 0 else 0)
y = pd.DataFrame(y)

# TODO
cols_to_drop = ["time", "date", "sites"]
df.drop(columns=cols_to_drop)


def onehot_encode(X: pd.DataFrame) -> pd.DataFrame:
    encoder = OneHotEncoder()
    encoder.fit(X)
    np_array = encoder.transform(df).toarray()
    feat_columns = encoder.get_feature_names_out(df.columns)

    res_df = pd.DataFrame(np_array, columns=feat_columns)
    return res_df


print("get_dummies")
X = df
# X_encoded = pd.get_dummies(X)
X = onehot_encode(X)
print("after get_dummies")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)

neurons: int = 16
num_layers: int = 1
dropout_prob: float = 0.5

model = Sequential()

model.add(Dense(neurons, input_dim=X_train.shape[1], activation='relu'))
model.add(Dropout(dropout_prob))

for i in range(num_layers):
    model.add(Dense(neurons, activation='relu'))
    model.add(Dropout(dropout_prob))

model.add(Dense(1, activation='sigmoid'))

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=[
        'accuracy'
        # my_f1_score,
        # Precision(),
        # Recall(),
        # Accuracy(),
    ]
)

# early_stopping = tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
# model.fit(X_train, y_train, validation_split=0.2, epochs=50, callbacks=[early_stopping])
# loss, accuracy = model.evaluate(X_test, y_test)

VALIDATION_RATIO = 0.2
BATCH_SIZE = 128
EPOCHS = 10

early_stopping = EarlyStopping(
    patience=5,
    restore_best_weights=True
)

print("model.fit")
model.fit(
    X_train, y_train,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_split=VALIDATION_RATIO,
    verbose=VERBOSITY,
    callbacks=[early_stopping]
)

# loss, accuracy\
results = model.evaluate(
    X_test, y_test,
    verbose=VERBOSITY
)

print(results)

model.summary()

# test_loss, test_f1, test_accuracy, test_precision, test_recall, test_auc = model.evaluate(X_test, y_test)


