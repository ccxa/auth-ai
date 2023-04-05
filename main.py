import uvicorn
from fastapi import FastAPI, File, UploadFile
import shutil
from face import compare_faces
from utils import random_string
import os
from dotenv import load_dotenv

load_dotenv('./.env')
storage_path = os.getenv("STORAGE_PATH")
random_string_length = int(os.getenv("RANDOM_STRING_LENGTH"))

app = FastAPI()


@app.post("/get_file")
async def get(image: UploadFile = File(...), video: UploadFile = File(...)):
    prefix = random_string(random_string_length)

    image_path = storage_path + prefix + image.filename
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    video_path = storage_path + prefix + video.filename
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    comparing_result = bool(compare_faces(image_path, video_path)[0])

    os.remove(image_path)
    os.remove(video_path)

    return {"status": comparing_result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
