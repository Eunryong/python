from numpy import array, copy
from matplotlib.pyplot import imshow, show
from load_image import ft_load


def ft_invert(array) -> array:
    '''Inverts the color of the image received.'''
    (x, y) = array.shape[:2]
    invert = copy(array)
    for i in range(x):
        for j in range(y):
            r, g, b = invert[i, j]
            r = 255 - r
            g = 255 - g
            b = 255 - b
            invert[i, j] = (r, g, b)
    imshow(invert)
    show()
    return invert


def ft_red(array) -> array:
    ''''''
    (x, y) = array.shape[:2]
    red = copy(array)
    for i in range(x):
        for j in range(y):
            r, g, b = red[i, j]
            r *= 1
            g = 0
            b = 0
            red[i, j] = (r, g, b)
    imshow(red)
    show()
    return red


def ft_green(array) -> array:
    (x, y) = array.shape[:2]
    green = copy(array)
    for i in range(x):
        for j in range(y):
            r, g, b = green[i, j]
            r -= r
            b -= b
            green[i, j] = (r, g, b)
    imshow(green)
    show()
    return green


def ft_blue(array) -> array:
    (x, y) = array.shape[:2]
    blue = copy(array)
    for i in range(x):
        for j in range(y):
            r, g, b = blue[i, j]
            r = 0
            g = 0
            blue[i, j] = (r, g, b)
    imshow(blue)
    show()
    return blue


def ft_grey(array) -> array:
    (x, y) = array.shape[:2]
    grey = copy(array)
    for i in range(x):
        for j in range(y):
            r = sum(grey[i, j]) / 3
            g = r
            b = r
            grey[i, j] = (r, g, b)
    imshow(grey)
    show()
    return grey


if __name__ == "__main__":
    image = ft_load("landscape.jpeg")
    ft_invert(image)
    ft_red(image)
    ft_green(image)
    ft_blue(image)
    ft_grey(image)
