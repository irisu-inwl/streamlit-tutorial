from keras.applications.xception import Xception, preprocess_input, decode_predictions

model = Xception(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)