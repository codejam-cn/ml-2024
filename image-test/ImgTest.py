import os

import requests
import random
import uuid


class ImgTest:
    def __init__(self):
        super().__init__()


if __name__ == "__main__":

    save_path = os.path.abspath("./temp/")
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for i in range(1, 100):
        imgUrl = "https://thispersondoesnotexist.com/"

        response = requests.get(imgUrl)
        print(response)

        content = response.content

        file_name = uuid.uuid4()

        str_file_name = str(file_name) + ".jpg"

        file_path = os.path.join(save_path, str_file_name)

        with open(file_path, 'wb') as f:
            f.write(content)
