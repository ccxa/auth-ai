import face_recognition as fr


def compare_faces(source1: str, source2: str) -> bool:
    """
    Compares the faces in two binary files and
    returns a boolean value indicating whether they match.

    Args:
        source1 (str): The filename or path to the first binary file.
        source2 (str): The filename or path to the second binary file.

    Returns:
        A bool value indicating whether the faces in the two files match.
    """

    # loading binary files from local
    known_face = fr.load_image_file(source1)
    unknown_face = fr.load_image_file(source2)
    
    # encoding loaded binary files
    known_face_encoding = fr.face_encodings(known_face)[0]
    unknown_face_encoding = fr.face_encodings(unknown_face)[0]

    # Comparing faces in encoded binary files, then returning its result
    return fr.compare_faces([known_face_encoding], unknown_face_encoding)
