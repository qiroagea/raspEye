# URL: http://cedro3.com/ai/keras-vgg16/
# URL: https://uchidama.hatenablog.com/entry/2018/02/15/063200

from keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Sequential, Model
from keras.layers import Input, Flatten, Dense, Dropout
import numpy as np
import cv2
from PIL import Image

# 同構造のモデルの定義
classes = ["西垣前", "3F階段前", "4F階段前", "D5前", "D4前"]
nb_classes = len(classes)
img_width, img_height = 150, 150
input_tensor = Input(shape=(img_width, img_height, 3))
mnet = MobileNet(include_top=False, weights='imagenet', input_tensor=input_tensor)
top_model = Sequential()
top_model.add(Flatten(input_shape=mnet.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(nb_classes, activation='softmax'))
mnet_model = Model(input=mnet.input, output=top_model(mnet.output))

# 重みと結合
mnet_model.load_weights('fineTuned.h5')
mnet_model.summary()

# カメラから画像データの読み込み
cap = cv2.VideoCapture(0)
# x = []
# img = img_to_array(load_img('./data/yosaku.jpg', target_size=(224, 224)))
# x.append(img)
# ary = np.asarray(x)
# print('ary shape:', ary.shape)

# トップ5を認識
while True:
    ret, frame = cap.read()
    cv2.imshow("Show FLAME Image", frame)
    img = Image.fromarray(np.uint8(frame))
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    ary = np.expand_dims(x, axis=0)
    preds = mnet_model.predict(preprocess_input(ary))
    results = decode_predictions(preds, top=5)[0]
    print(results)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
