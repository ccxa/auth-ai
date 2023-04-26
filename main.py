import os
from fastapi import FastAPI, File, UploadFile
from dotenv import load_dotenv
import shutil
import uvicorn
from face import compare_faces
from utils import random_string

load_dotenv('./.env')
storage_path = os.getenv("STORAGE_PATH")
random_string_length = int(os.getenv("RANDOM_STRING_LENGTH"))

app = FastAPI()


@app.post("/get_file")
async def post(image: UploadFile = File(...), video: UploadFile = File(...)):
    """
        Receives an image and a video file by incoming post request,
        compares the faces in both binary files,
        and returns a boolean indicating whether they match.

        Args:
            image (UploadFile): The image file to be uploaded.
            video (UploadFile): The video file to be uploaded.

        Returns:
            A dictionary containing the result of the face comparison
            as a boolean value under the key 'status'.
    """
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


@app.get("/hi")
async def get() -> dict:
    """
    Just returns a JSON response with the message "Hi !".
    Use this endpoint to check if the app is running and accessible.

    Returns:
        dict: A JSON object with the message "Hi !".
    """
    return {"msg": 'Hi !'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
