from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from captionModel import get_caption_model
from keras.models import Model
from keras.utils import img_to_array
from keras.applications.vgg16 import VGG16,preprocess_input
from captionTokenizer import get_token_maxlen
from captionGenerator import predict_caption
from PIL import Image
import numpy as np
import io

model = get_caption_model()

vgg_model = VGG16()
#Restructuring the model
vgg_model = Model(inputs=vgg_model.inputs, outputs=vgg_model.layers[-2].output)

tokenizer , max_length = get_token_maxlen()


#Initialising FastApi Server
app = FastAPI()


#Ignore this
@app.get("/")
def welcome():
    return {"message": "Server is Up !!"}

#Ignore this 
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}



#Modify this part
#Pass the uploaded file to the model
@app.post("/generateCaption/")
async def generate_caption(file: UploadFile = File(...)):
     # Load the uploaded image
    contents = await file.read()
    img = Image.open(io.BytesIO(contents))
    
    # Resize the image
    img = img.resize((224, 224))

    # convert image pixels to numpy array
    image = img_to_array(img)
    # reshape data for model
    # image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = np.expand_dims(image, axis=0) 
    # preprocess image for vgg
    image = preprocess_input(image)
    # extract features
    feature = vgg_model.predict(image, verbose=0)
    generated_caption = predict_caption(model, feature, tokenizer, max_length)
    return {"Caption": generated_caption}

#Running Command in terminal -->  uvicorn endpoints:app --reload