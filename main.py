import uvicorn
from fastapi import FastAPI, File, UploadFile
import shutil


# TODO: This path should be inside .env like file
# TODO: This directory should automatically created when program starts
storage_path = './temp/media/'

app = FastAPI()


@app.post("/get_file")
async def get(image: UploadFile = File(...), video: UploadFile = File(...)):

    image_path = storage_path + image.filename
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    video_path = storage_path + video.filename
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
