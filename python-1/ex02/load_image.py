from numpy import array
from PIL import Image
from os import path as os_path, getcwd
def ft_load(path: str) -> array:
    '''
    Load image with path
    '''
    try:
        pwd = getcwd()
        file_path = path if os_path.isabs(path) else os_path.join(pwd, path)
        assert os_path.isfile(file_path), "File not found"
        file_extention = os_path.splitext(path)[1]
        assert file_extention and\
            (file_extention.lower() == '.jpg' or\
              file_extention.lower() == '.jpeg'), "File extention error"
        im = Image.open(file_path)
        print("The shape of image is:", array(im).shape)
        return array(im)
    except AssertionError as e:
        print("Load image error:", e)

