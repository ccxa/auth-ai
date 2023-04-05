import random
import string


def random_string(length):
    return ''.join(random.sample(string.ascii_lowercase, length))
