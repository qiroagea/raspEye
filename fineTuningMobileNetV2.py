# Qiita: GPUを使ってVGG16をFine Tuningして、顔認識AIを作って見た

from keras.applications.mobilenetv2 import MobileNetV2
from keras.models import Sequential, Model
from keras.layers import Input, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
import matplotlib.pyplot as plt

# ---- 分類するクラス ---- #
classes = ["下接近", "下通過", "上接近", "上通過右", "上通過左", "無"]
nb_classes = len(classes)

# ---- 画像の大きさを設定 ---- #
img_width, img_height = 160, 120

# ---- 画像の格納先（トレーニング用とバリデーション用） ---- #
train_data_dir = './data'
validation_data_dir = './test'

# ---- 画像のデータ数 ---- #
nb_train_samples = 2609
nb_validation_samples = 167

# ---- バッチサイズ ---- #
batch_size = 261

# ---- エポック数 ---- #
nb_epoch = 10

# ---- ジェネレータの作成 ---- #
train_datagen = ImageDataGenerator(rescale=1.0 / 255)
validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    color_mode='rgb',
    classes=classes,
    batch_size=batch_size,
    shuffle=True
)
validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    color_mode='rgb',
    classes=classes,
    class_mode='categorical',
    batch_size=batch_size,
    shuffle=True
)

# ---- モデルのロード（FC層は無効化） ---- #
input_tensor = Input(shape=(img_width, img_height, 3))
model = MobileNetV2(include_top=False, weights='imagenet', input_tensor=input_tensor)

# ---- FC層の作成 ---- #
top_model = Sequential()
top_model.add(Flatten(input_shape=model.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(nb_classes, activation='softmax'))

# ---- モデルの結合 ---- #
modelUnion = Model(input=model.input, output=top_model(model.output))

# ---- VGG16の重みを固定 ---- #
for layer in modelUnion.layers[:15]:
    layer.trainable = False

# ---- 多クラス分類を指定 ---- #
modelUnion.compile(
    loss='categorical_crossentropy',
    optimizer=optimizers.SGD(lr=1e-3, momentum=0.9),
    metrics=['accuracy']
)

# ---- ファイン！ ---- #
history = modelUnion.fit_generator(
    train_generator,
    samples_per_epoch=nb_train_samples,
    nb_epoch=nb_epoch,
    validation_data=validation_generator,
    nb_val_samples=nb_validation_samples
)

# ---- プロット ---- #
#plt.plot(history.history["acc"], label="acc", ls="-", marker="o")
#plt.plot(history.history["val_acc"], label="val_acc", ls="-", marker="x")
#plt.ylabel("accuracy")
#plt.xlabel("epoch")
#plt.legend(loc="best")
#plt.savefig('plot/mobileNetV2.png')
#plt.show()

# ---- モデルの保存 ---- #
modelUnion.save("model/mobileNetV2.h5")
