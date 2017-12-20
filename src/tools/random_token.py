import random
import string


def generate_random_token(n_char=32):
    """Randomly generate a token of size N of letters or digits"""
    return ''.join(
        random
        .SystemRandom()
        .choice(string.ascii_letters + string.digits)
        for _ in range(n_char)
    )
