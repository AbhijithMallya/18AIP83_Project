#Import Modules
import pickle
from keras.models import load_model
from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Input, Dense, LSTM, Embedding, Dropout, add


def get_caption_model() :
    model = VGG16()
    # restructure the model
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
    # summarize
    # print(model.summary())

    # load features from pickle
    with open( 'features.pkl', 'rb') as f:
        features = pickle.load(f)
        
    #Model Creation
    # encoder model
    # image feature layers
    inputs1 = Input(shape=(4096,))
    fe1 = Dropout(0.4)(inputs1)
    fe2 = Dense(256, activation='relu')(fe1)
    # sequence feature layers
    inputs2 = Input(shape=(8485,))
    se1 = Embedding(8485, 256, mask_zero=True)(inputs2)
    se2 = Dropout(0.4)(se1)
    se3 = LSTM(256)(se2)

    # decoder model
    decoder1 = add([fe2, se3])
    decoder2 = Dense(256, activation='relu')(decoder1)
    outputs = Dense(8485, activation='softmax')(decoder2)

    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    # model.summary()
    model = load_model('best_model.h5')
    print('Loaded Model Successfully')
    return model 