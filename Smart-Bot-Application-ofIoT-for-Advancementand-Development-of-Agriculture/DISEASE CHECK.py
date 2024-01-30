from keras import preprocessing
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import keras.models
import matplotlib.pyplot as plt
import numpy as np
import cv2
import keras.preprocessing

class_names = ["healthy", "non healthy;"]

classifier=Sequential()

classifier.add(Conv2D(32, 3, 3, input_shape=(150, 150, 3), activation="relu"))

classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Conv2D(32, 3, 3, activation="relu"))

classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Flatten())

classifier.add(Dense(output_dim=128, activation="relu"))
classifier.add(Dense(output_dim=1, activation="sigmoid"))

classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=['acc'])

train_datagen = keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

print(train_datagen)

test_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        '/root/flower/',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        '/root/flower/',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        train_generator,
        steps_per_epoch=20,
        epochs=2,
        validation_data=validation_generator,
        validation_steps=80)



ip = preprocessing.image.load_img("/root/plants34/", target_size=(150, 150))
print(ip)
f=plt.imshow(ip)
plt.show()
predct = np.expand_dims(ip, axis=0)
print(predct)
prediction = classifier.predict(predct)
print(prediction)
a = np.argmax(prediction)
print(a)
r = class_names[np.argmax(a)]
print(r)
