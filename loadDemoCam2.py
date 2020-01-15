# URL: http://cedro3.com/ai/keras-vgg16/
# URL: https://uchidama.hatenablog.com/entry/2018/02/15/063200

from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import cv2
from PIL import Image

# 学習済みモデルの読み込み
model = load_model('mobileNetV2_16.h5')
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
    img = img.resize((120, 160))
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
    print("下接近, 下通過, 上接近, 上通過右, 上通過左, 無")
    print(results*100)
    k = cv2.waitKey(10)
    price = max(results)
    if (price == results[0]):
        print("下接近")
    if (price == results[1]):
        print("下通過")
    if (price == results[2]):
        print("上接近")
    if (price == results[3]):
        print("上通過右")
    if (price == results[4]):
        print("上通過左")
    if (price == results[5]):
       print("無")
    if k == ord('q'):
        break

cap.release()
# cv2.destroyAllWindows()
