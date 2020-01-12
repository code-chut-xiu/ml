from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper Libraries
import numpy as np
import matplotlib as plt

print(tf.__version__)

fashion_mnist = keras.datasets.mnist

# Mac user might encounter the CERTIFICATE_VERIFY_FAILED error.  Run this line in the terminal prompt
# will most likely fix it.
# /Applications/Python\ 3.6/Install\ Certificates.command
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
