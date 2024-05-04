from load_image import ft_load
from numpy import array, resize
from PIL import Image

def zoom(image: array) -> array:
    '''hi
    '''
    try:
        pil_image= Image.fromarray(image)
        w, h = pil_image.size
        assert w >= 400 and h >= 400, "hi"
        # (left, upper, right, lower) = (w * 1 / 4, h * 1 / 4, w * 3 / 4, h * 3 / 4)
        (left, upper, right, lower) = (w / 2 - 200, h / 2 - 200, w / 2 + 200, h / 2 + 200)
        zoom_image = pil_image.crop((left, upper, right, lower))
        # zoom_image = pil_image.resize((400, 400), 1)
        zoom_array = array(zoom_image)
        zoom_image.show()
        print("New shape after slicing:", zoom_array.shape)
        return zoom_array
    except AssertionError as e:
        print("Image error:", e)

if __name__ == "__main__":
    image = ft_load("animal.jpeg")
    print(image)
    print(zoom(image))
    