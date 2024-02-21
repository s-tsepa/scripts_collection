

# !pip install opencv-python

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Set the path to the folder containing the fingerprint images
data_path = "assets/task2/train"

# Set the image dimensions
# IMG_WIDTH = 96
# IMG_HEIGHT = 103

RANDOM_STATE = 123
TEST_RATIO = 0.2
VERBOSITY = 1

IMG_WIDTH = 128
IMG_HEIGHT = 128

data = []
labels = []
for filename in os.listdir(data_path):
    index, label = map(int, filename.removesuffix(".bmp").split("_"))

    img = cv2.imread(os.path.join(data_path, filename))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    top_border = int(0.05 * img.shape[0])  # 5% of height
    bottom_border = int(0.05 * img.shape[0])
    left_border = int(0.05 * img.shape[1])  # 5% of width
    right_border = int(0.05 * img.shape[1])

    img = img[
          top_border:img.shape[0] - bottom_border,
          left_border:img.shape[1] - right_border
    ]

    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype('float32') / 255.0

    data.append(img)
    labels.append(label)

# Convert data and labels to numpy arrays
# data = np.array(data) / 255.0
# labels = np.array(labels)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data,
    labels,
    test_size=TEST_RATIO,
    random_state=RANDOM_STATE
)

# Create an ImageDataGenerator object for data augmentation
datagen = ImageDataGenerator(
    # rotation_range=20,
    # width_shift_range=0.2,
    # height_shift_range=0.2,
    # horizontal_flip=True,
    # vertical_flip=False,
)
# X_train = np.reshape(X_train, (*X_train.shape, 1))
datagen.fit(X_train)

print(3)



def build_model(filters: int = 32, kernel_size: tuple[int, int] = (3, 3)):
    model = Sequential()

    model.add(Conv2D(filters=filters, kernel_size=kernel_size, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=filters*2, kernel_size=kernel_size, activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(units=64, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(units=1, activation="sigmoid"))

    # model.summary()
    return model


model = build_model()
print(4)
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=[
        "accuracy"
    ]
)

print(5)
# Train the model
BATCH_SIZE = 32
EPOCHS = 50
history = model.fit(
    datagen.flow(
        X_train.reshape(-1, IMG_WIDTH, IMG_HEIGHT, 1),
        y_train,
        batch_size=BATCH_SIZE
    ),
    validation_data=(
        X_test.reshape(-1, IMG_WIDTH, IMG_HEIGHT, 1),
        y_test
    ),
    epochs=EPOCHS,
    verbose=VERBOSITY
)


print(6)
# Evaluate the model
score = model.evaluate(
    X_test.reshape(-1, IMG_WIDTH, IMG_HEIGHT, 1),
    y_test
)
print(score)