import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def extract_image(scale: float = 2, color_format=cv.IMREAD_GRAYSCALE) -> np.array:
    image: np.array = cv.imread("data/image.png", color_format)
    new_dims: list = [int(dim // scale) for dim in image.shape[:2]][::-1]
    resized_image: np.array = cv.resize(image, new_dims)
    return resized_image


def show_image(image: np.array) -> None:
    cv.imshow("window", image)
    cv.waitKey(0)


def apply_gaussian(image: np.array, scale: int = 5) -> np.array:
    return cv.GaussianBlur(image, (scale, scale), 0)

def apply_threshhold(image,threshhold):
    _,thresh = cv.threshold(image,threshhold)


def main():
    image_size = 1.5
    image: np.array = extract_image(image_size)
    blurred = apply_gaussian(image,3)
    show_image(blurred)


if __name__ == "__main__":
    main()
