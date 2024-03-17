from captionModel import get_caption_model
from keras.models import Model
from keras.utils import load_img, img_to_array
from keras.applications.vgg16 import VGG16,preprocess_input
from captionTokenizer import get_token_maxlen
from captionGenerator import predict_caption

model = get_caption_model()

vgg_model = VGG16()
# restructure the model
vgg_model = Model(inputs=vgg_model.inputs, outputs=vgg_model.layers[-2].output)

tokenizer , max_length = get_token_maxlen()
#Test With Real Image
image_path = 'sample6.jpg'
# load image
image = load_img(image_path, target_size=(224, 224))
# convert image pixels to numpy array
image = img_to_array(image)
# reshape data for model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# preprocess image for vgg
image = preprocess_input(image)
# extract features
feature = vgg_model.predict(image, verbose=0)
# predict from the trained model
generated_caption = predict_caption(model, feature, tokenizer, max_length)

print("Generated Caption : ",generated_caption)

print("Everything good as of now")