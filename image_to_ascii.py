import sys
from PIL import Image

CHARS = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
NEW_WIDTH = 100


def open_image(path):
    _img = Image.open(path)
    # return converted to gray scale image
    return _img.convert('L')


# new size of image
def resize_image(_img, new_width):
    width, height = _img.size
    aspect_ratio = height / width
    new_height = aspect_ratio * new_width * 0.55
    resized_image = _img.resize((new_width, int(new_height)))
    return resized_image


def pix_to_char(_img, new_width):
    pixels = _img.getdata()
    new_pixels = [CHARS[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in
                   range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    return ascii_image


def main(_img, size=NEW_WIDTH):
    try:
        _image = Image.fromarray(_img)
        _image = _image.convert('L')
    except:
        _image = _img
    _image = resize_image(_image, size)
    print(pix_to_char(_image, size))


if __name__ == '__main__':
    import sys
    try:
        filename = sys.argv[1]
    except:
        filename = "my_image.png"
    image = open_image(filename)
    main(image, size=600)
