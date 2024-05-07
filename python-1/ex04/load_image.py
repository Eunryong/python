import numpy as np
import PIL
import os
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.array:
    '''
    Load image with path
    '''
    try:
        pwd = os.getcwd()
        file_path = path if os.path.isabs(path) else os.path.join(pwd, path)
        assert os.path.isfile(file_path), "File not found"
        file_extention = os.path.splitext(path)[1]
        assert file_extention and\
            (file_extention.lower() == '.jpg' or
             file_extention.lower() == '.jpeg'), "File extention error"
        im = PIL.Image.open(file_path)
        image_array = np.array(im)
        print("The shape of image is:", image_array.shape)
        plt.imshow(image_array)
        plt.show()
        return image_array
    except AssertionError as e:
        print("Load image error:", e)


if __name__ == "__main__":
    print(ft_load("landscape.jpeg"))
