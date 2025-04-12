import tensorflow as tf

def train_models():
    for i in range(3):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(10))
