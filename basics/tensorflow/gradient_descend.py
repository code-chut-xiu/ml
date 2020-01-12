import tensorflow as tf
import numpy as np
from tensorflow import keras
from constants.loss_function import MEAN_SQUARED_ERROR_LOSS_FUNC
from constants.optimizers import STOICHAIC_GRADIENT_DESCENT_OPTIMIZER

print(tf.__version__)
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer=STOICHAIC_GRADIENT_DESCENT_OPTIMIZER, loss=MEAN_SQUARED_ERROR_LOSS_FUNC)

xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))
