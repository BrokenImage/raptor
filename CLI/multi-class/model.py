import numpy as np
import keras as k
import json
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

def load_images_labels(path_to_metadata_json):
    file = open(path_to_metadata_json) # Open meta-data
    data = json.load(file) # load meta-data
    file.close() # close file :)
    images , category = [], [] # make lists to append images and categories to
    for i in range(20000): # 20,000 is the amount of images we have to work with 
        images.append(np.array(k.preprocessing.image.load_img(
            'InfraredSolarModules/' + data[str(i)]['image_filepath'], color_mode = "grayscale"))) # load the image and append to list
        category.append(data[str(i)]['anomaly_class']) # load its class
    return np.array(images), np.array(category) # return np arrays for ease of use later

def preprocess_images_labels(images, category):
    images = images.reshape(20000, 40, 24, 1) # reshape to show color channels
    images = images / 255 # scale data
    X_train, X_test, y_train, y_test = train_test_split(images, category, test_size=0.2)
    labelencoder = LabelEncoder() # Make a label encoder 
    y_train = labelencoder.fit_transform(y_train) # encode labels to numbers
    y_test = labelencoder.transform(y_test)
    y_train = k.utils.to_categorical(y_train) # encode nubers to catagorical labels
    y_test = k.utils.to_categorical(y_test)
    return X_train, X_test, y_train, y_test

def define_model():
    """
    This model is a little less accurate than the best one I found.
    But it also has onlya quarter the paramenters so its a lot smaller.
    """
    model = k.Sequential()
    model.add(k.layers.Conv2D(filters=15, kernel_size=(3,3), strides=(1, 1), padding="valid", input_shape=(40, 24, 1)))
    model.add(k.layers.MaxPooling2D(pool_size=(2, 2), strides=(2,2), padding="same"))
    model.add(k.layers.Conv2D(filters=15, kernel_size=(3,3), strides=(1, 1), padding="valid"))
    model.add(k.layers.MaxPooling2D(pool_size=(2, 2), strides=(2,2), padding="same"))
    model.add(k.layers.Flatten())
    model.add(k.layers.Dense(675))
    model.add(k.layers.Activation('relu'))
    model.add(k.layers.Dense(12))
    model.add(k.layers.Activation('softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
    model.summary()
    return model

if __name__ == '__main__':
    # load
    images, categories = load_images_labels('InfraredSolarModules/module_metadata.json')
    # prrocess and train test split
    X_train, X_test, y_train, y_test = preprocess_images_labels(images, categories)
    # define model
    model = define_model()
    # fit
    model.fit(X_train, y_train, epochs=20, batch_size=20, verbose=1, shuffle=True)
    # evaluate
    model.evaluate(X_test, y_test, verbose=1)
    # save model as model.h5
    model.save("model.h5")



