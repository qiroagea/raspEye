# Qiita: GPUを使ってVGG16をFine Tuningして、顔認識AIを作って見た

import os
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
import numpy as np
import time

# ---- 分類するクラス ---- #
classes = ["西垣前", "3F階段前", "4F階段前", "D5前", "D4前"]
nb_classes = len(classes)

# ---- 画像の大きさを設定 ---- #
img_width, img_height = 150, 150

# ---- 画像の格納先（トレーニング用とバリデーション用） ---- #
train_data_dir = './data'
validation_data_dir = './test'

# ---- 画像のデータ数 ---- #
nb_train_samples = 318
nb_validation_samples = 16

# ---- バッチサイズ ---- #
batch_size = 53

# ---- エポック数 ---- #
nb_epoch = 6

# ---- ジェネレータの作成 ---- #
train_datagen = ImageDataGenerator(rescale=1.0/255)
validation_datagen = ImageDataGenerator(rescale=1.0/255)

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

# ---- VGG16のロード（FC層は無効化） ---- #
input_tensor = Input(shape=(img_width, img_height, 3))
vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

# ---- FC層の作成 ---- #
top_model = Sequential()
top_model.add(Flatten(input_shape=vgg16.outputshape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(nb_classes, activation='softmax'))

# ---- モデルの結合 ---- #
vgg_model = Model(input=vgg16.input, output=top_model(vgg16.output))

# ---- VGG16の重みを固定 ---- #
for layer in vgg_model.layers[:15]:
    layer.trainable = False

# ---- 多クラス分類を指定 ---- #
vgg_model.compile(
    loss='categorical_crossentropy',
    optimizer=optimizers.SGD(lr=1e-3, momentum=0.9),
    metrics=['accuracy']
)

# ---- ファイン！ ---- #
history = vgg_model.fit_generator(
    train_generator,
    samples_er_epoch=nb_train_samples,
    nb_epoch=nb_epoch,
    validation_data=validation_generator,
    nb_val_samples=nb_validation_samples
)