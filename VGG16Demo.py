import cv2
import matplotlib.pyplot as plt
import numpy as np

from keras_applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras_preprocessing import image