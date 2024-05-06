from load_image import ft_load
from numpy import array, dot, uint8
from PIL import Image
from matplotlib.pyplot import show, imshow

def rotate(image: array) -> array:
    if len(image.shape) == 3 and image.shape[2] == 3:
        image = dot(image[...,:3], [0.2989, 0.5870, 0.1140]).astype(uint8)
    (h, w) = image.shape
    image_list = image.tolist()
    rotated_image = [[0 for x in range(h)] for y in range(w)]
    for x in range(0, w):
        for y in range(0, h):
            rotated_image[x][y] = image_list[y][x]
    transposed = array(rotated_image)
    rotated = Image.fromarray(transposed.astype(uint8))
    print("New shape after Transpose:", transposed.shape)
    imshow(rotated, cmap="gray")
    show()
    return transposed

if __name__ == "__main__":
    image = ft_load("animal.jpeg")
    print(image)
    print(rotate(image))