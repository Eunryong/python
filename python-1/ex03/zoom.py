from load_image import ft_load
import numpy as np
import PIL
import matplotlib.pyplot as plt


def zoom(image: np.array, x, y) -> np.array:
    '''hi
    '''
    try:
        pil_image = PIL.Image.fromarray(image)
        w, h = pil_image.size
        assert w >= x and h >= y, "hi"
        (left, upper, right, lower) = ((w - x) / 2, (h - y) / 2,
                                       (w + x) / 2, (h + y) / 2)
        zoom_image = pil_image.crop((left, upper, right, lower))
        # zoom_image.save("zoom_image.jpeg", "jpeg")
        zoom_array = np.asarray(zoom_image)
        zoom_array = np.dot(zoom_array[..., :3], [0.2989,
                                               0.5870, 0.1140]).astype(np.uint8)
        print("New shape after slicing:", zoom_array.shape)
        plt.imshow(zoom_array, cmap="gray")
        plt.show()
        return zoom_array
    except AssertionError as e:
        print("Image error:", e)


if __name__ == "__main__":
    image = ft_load("animal.jpeg")
    print(image)
    print(zoom(image, 400, 400))
