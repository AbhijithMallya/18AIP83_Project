from fastapi import FastAPI, File, UploadFile
from typing import Annotated

# ----------------------------------------------------------
#-----------------------Irshad ----------------------------
# ----------------------------------------------------------

#Load the model  before app = FastAPI()


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
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    size = file.size/(1024)
    
    return {"Filename": file.filename,
            "File_content" : file.content_type, 
            "File size (Kb)": size 
            }
    
    #Actual return function as below
    #result = answer given by the model
    #return {"caption" : result}
