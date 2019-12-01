from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing.image import img_to_array, load_img
import numpy as np

# 学習済みモデルの読み込み
model = VGG16(include_top=True, weights='imagenet', input_shape=None)
model.summary()

# 'data' フォルダから画像データの読み込み
x = []
img = img_to_array(load_img('./data/yosaku.png', target_size=(244, 244)))
x.append(img)
ary = np.asarray(x)
print('ary shape:', ary.shape)

# トップ5を認識
for i in range(len(ary)):
    preds = model.predict(preprocess_input(ary))
    results = decode_predictions(preds, top=5)[i]
    print(i)
    for results in results:
        print(results)