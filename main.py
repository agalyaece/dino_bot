import pyautogui
import time
from PIL import ImageGrab, ImageOps
import numpy as np
pyautogui.FAILSAFE = True


class Coordinates:
    replay = (353, 388)
    tree1 = (195, 416)
    tree2 = (245, 433)
    bird = (155, 379)
    dino = (170, 391)


def image_grab():
    box = (Coordinates.dino[0]+20, Coordinates.dino[1], Coordinates.dino[0]+100, Coordinates.dino[1]+30)
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    a = np.array(gray_image.getcolors())
    return a.sum()


def jump():
    pyautogui.keyDown("space")
    time.sleep(0.05)
    pyautogui.keyUp("space")
    time.sleep(0.05)


def duck():
    pyautogui.keyDown("down")
    time.sleep(0.05)
    pyautogui.keyUp("down")
    time.sleep(0.05)


def restart():
    pyautogui.click(Coordinates.replay)


def main():
    restart()
    while True:
        image_grab()
        if image_grab() != 2646:
            jump()
            time.sleep(0.001)


if __name__ == "__main__":
    main()


