import numpy as np
from tensorflow import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
split_classes = [8, 9]
mask_train_8 = np.isin(y_train, split_classes, invert=True).flatten()
mask_test_8 = np.isin(y_test, split_classes, invert=True).flatten()
