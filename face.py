import face_recognition


def compare_faces(source1, source2):
    known_image = face_recognition.load_image_file(source1)
    unknown_image = face_recognition.load_image_file(source2)

    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    return face_recognition.compare_faces([known_encoding], unknown_encoding)
