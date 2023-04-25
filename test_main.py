from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_hello():
    response = client.get('/hi')
    assert response.status_code == 200
    assert response.json() == {"msg": "Hi !"}


def test_authorized_by_video():
    with open("./test_files/person1-main.png", "rb") as image_file:
        image_bytes = image_file.read()
    with open("./test_files/person1-v1.gif", "rb") as video_file:
        video_bytes = video_file.read()

    response = client.post(
        "/get_file",
        files={
            "image": ("billies_image.jpg", image_bytes),
            "video": ("billies_video.mp4", video_bytes)
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": True}


def test_authorized_by_image():
    with open("./test_files/person1-main.png", "rb") as image_file:
        image_bytes = image_file.read()
    with open("./test_files/person1-p1.jpg", "rb") as video_file:
        video_bytes = video_file.read()

    response = client.post(
        "/get_file",
        files={
            "image": ("billies_image.jpg", image_bytes),
            "video": ("billies_video.mp4", video_bytes)
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": True}


def test_unauthorized_by_video():
    with open("./test_files/person1-main.png", "rb") as image_file:
        image_bytes = image_file.read()
    with open("./test_files/person2-v1.gif", "rb") as video_file:
        video_bytes = video_file.read()

    response = client.post(
        "/get_file",
        files={
            "image": ("billies_image.jpg", image_bytes),
            "video": ("billies_video.mp4", video_bytes)
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": False}


def test_unauthorized_by_image():
    with open("./test_files/person1-main.png", "rb") as image_file:
        image_bytes = image_file.read()
    with open("./test_files/person2-p1.jpg", "rb") as video_file:
        video_bytes = video_file.read()

    response = client.post(
        "/get_file",
        files={
            "image": ("billies_image.jpg", image_bytes),
            "video": ("billies_video.mp4", video_bytes)
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": False}

