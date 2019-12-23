# URL: http://cedro3.com/ai/keras-vgg16/
# URL: https://uchidama.hatenablog.com/entry/2018/02/15/063200

from keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import cv2
from PIL import Image

# 学習済みモデルの読み込み
model = MobileNet(include_top=True, weights='imagenet', input_shape=None)
model.summary()

# カメラから画像データの読み込み
cap = cv2.VideoCapture(0)

# トップ5を認識
while True:
    ret, frame = cap.read()
    img = Image.fromarray(np.uint8(frame))
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    ary = np.expand_dims(x, axis=0)
    preds = model.predict(preprocess_input(ary))
    results = decode_predictions(preds, top=5)[0]
    print(results)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
