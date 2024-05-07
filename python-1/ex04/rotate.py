from load_image import ft_load
import numpy as np
import PIL
import matplotlib.pyplot as plt


def rotate(image: np.array) -> np.array:
    if len(image.shape) == 3 and image.shape[2] == 3:
        image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    (h, w) = image.shape
    image_list = image.tolist()
    rotated_image = [[0 for x in range(h)] for y in range(w)]
    for x in range(0, w):
        for y in range(0, h):
            rotated_image[x][y] = image_list[y][x]
    transposed = np.array(rotated_image)
    rotated = PIL.Image.fromarray(transposed.astype(np.uint8))
    print("New shape after Transpose:", transposed.shape)
    plt.imshow(rotated, cmap="gray")
    plt.show()
    return transposed


if __name__ == "__main__":
    image = ft_load("animal.jpeg")
    print(image)
    print(rotate(image))
