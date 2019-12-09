# URL: http://cedro3.com/ai/keras-vgg16/
# URL: https://uchidama.hatenablog.com/entry/2018/02/15/063200

from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import cv2
from PIL import Image

# 学習済みモデルの読み込み
model = load_model('mobileNetV2.h5')
model.summary()

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
#    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#    cv2.imshow("Show FLAME Image", frame)
    img = Image.fromarray(np.uint8(frame))
    img = img.resize((150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    # ary = np.asarray(frame)
    x = x / 255.0
    #    for i in range(len(ary)):
    # preds = model.predict(preprocess_input(ary))
    # results = decode_predictions(preds, top=5)[0]
    results = model.predict(x)[0]
    #    print(i)
    # for results in results:
    print("接近1, 接近2, 通過1, 通過2, 無")
    print(results*100)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
# cv2.destroyAllWindows()
