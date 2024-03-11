from fastapi import FastAPI, File, UploadFile
from typing import Annotated





app = FastAPI()


@app.get("/")
def welcome():
    return {"message": "Server is Up !!"}


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    size = file.size/(1024)
    
    return {"Filename": file.filename,
            "File_content" : file.content_type, 
            "File size (Kb)": size 
            }
