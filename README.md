# Authentication Restful API

This is a Python application that authenticates persons identity by detecting a person's face in a video by comparing it to a photo that you sure of its authenticity.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation
1. Clone the repository to your local machine. and navigate to the project folder
```bash
    $ git clone git@github.com:ccxa/auth-ai.git
    $ cd auth-ai
```
2. Setting up environment variables<br>
To run this application, you will need to set up a `.env` file in the root directory of the project with the following environment variables:
```bash
    # application uses this directory as place to hold its generated files. (string path on your machine)
    STORAGE_PATH =
    # random string assigned to received files, helps to avoid collisions. (should be integer number)
    RANDOM_STRING_LENGTH = 
```
2. Install Docker if you haven't already.
3. Run the following command in your terminal to build the Docker image:

```bash
    $ sudo docker build -t authenticator:v1 .
```
4. Start the application
```bash
    $ sudo docker run -p <host_port>:8000 authenticator:v1
```

## Usage
1. To make sure app is started correctly, send an empty Get request to `http://localhost:<host_port>/hi`.
    > The application responds you by saying Hi !.
2. Send a POST request to `http://localhost:<host_port>/recognize` with the following binary files at the requests body:

- `photo`: the binary file of the person's photo.
- `video`: the binary file of the video captured by the webcam.

    > The application will compare the person's face in the video to the photo that you sure of its authenticity and return a response indicating whether or not a match was found.
