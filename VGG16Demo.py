import cv2
import matplotlib.pyplot as plt
from IPython import display
import numpy as np

from keras_applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras_preprocessing import image

model = VGG16(weights='imagenet')

vc = cv2.VideoCapture(0)

if vc.isOpened():
    is_capturing, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    webcam_preview = plt.imshow(frame)
else:
    is_capturing = False

while is_capturing:
    try:
        is_capturing, frame = vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        webcam_preview.set_data(frame)
        plt.draw()

        display.clear_output(wait=True)
        display.display(plt.gcf())

        plt.pause(0.1)
    except KeyboardInterrupt:
        vc.release()
        is_capturing = False