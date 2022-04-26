import random
import string


class Uploader:

    @staticmethod
    def get_random_dir_name():
        s = string.ascii_lowercase + string.digits
        return ''.join(random.sample(s, 4))
