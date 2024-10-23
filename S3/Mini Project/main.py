import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Dropout, Activation, Flatten, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.utils import shuffle
import cv2
import glob

# Global variables
size = 100

def kerasModel4():
    model = Sequential()
    model.add(Conv2D(16, (8, 8), strides=(4, 4), padding='valid', input_shape=(size, size, 1)))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (5, 5), padding="same"))
    model.add(Activation('relu'))
    model.add(GlobalAveragePooling2D())
    model.add(Dense(512))
    model.add(Dropout(.1))
    model.add(Activation('relu'))
    model.add(Dense(2))
    model.add(Activation('softmax'))
    return model

# Load Training data: pothole
potholeTrainImages = glob.glob("My Dataset/train/Pothole/*.jpg")
potholeTrainImages.extend(glob.glob("My Dataset/train/Pothole/*.jpeg"))
potholeTrainImages.extend(glob.glob("My Dataset/train/Pothole/*.png"))

train1 = [cv2.imread(img, 0) for img in potholeTrainImages]
train1 = [cv2.resize(img, (size, size)) for img in train1]
temp1 = np.asarray(train1)

# Load Training data: non-pothole
nonPotholeTrainImages = glob.glob("My Dataset/train/Plain/*.jpg")
train2 = [cv2.imread(img, 0) for img in nonPotholeTrainImages]
train2 = [cv2.resize(img, (size, size)) for img in train2]
temp2 = np.asarray(train2)

# Load Testing data: non-pothole
nonPotholeTestImages = glob.glob("My Dataset/test/Plain/*.jpg")
test2 = [cv2.imread(img, 0) for img in nonPotholeTestImages]
test2 = [cv2.resize(img, (size, size)) for img in test2]
temp4 = np.asarray(test2)

# Load Testing data: potholes
potholeTestImages = glob.glob("My Dataset/test/Pothole/*.jpg")
test1 = [cv2.imread(img, 0) for img in potholeTestImages]
test1 = [cv2.resize(img, (size, size)) for img in test1]
temp3 = np.asarray(test1)

X_train = np.concatenate((temp1, temp2), axis=0)
X_test = np.concatenate((temp3, temp4), axis=0)

y_train1 = np.ones([temp1.shape[0]], dtype=int)
y_train2 = np.zeros([temp2.shape[0]], dtype=int)
y_test1 = np.ones([temp3.shape[0]], dtype=int)
y_test2 = np.zeros([temp4.shape[0]], dtype=int)

y_train = np.concatenate((y_train1, y_train2), axis=0)
y_test = np.concatenate((y_test1, y_test2), axis=0)

X_train, y_train = shuffle(X_train, y_train)
X_test, y_test = shuffle(X_test, y_test)

X_train = X_train.reshape(X_train.shape[0], size, size, 1)
X_test = X_test.reshape(X_test.shape[0], size, size, 1)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("Train shape X", X_train.shape)
print("Train shape y", y_train.shape)

inputShape = (size, size, 1)
model = kerasModel4()

model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=500, validation_split=0.1)

metrics = model.evaluate(X_test, y_test)
for metric_name, metric_value in zip(model.metrics_names, metrics):
    print('{}: {}'.format(metric_name, metric_value))

print("Saving model weights and configuration file")

model.save('model/sample.h5')

model_json = model.to_json()
with open("truesample.json", "w") as json_file:
    json_file.write(model_json)

model.save("model/truesample.h5")
print("Saved model to disk")
