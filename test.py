import pyautogui
import cv2 as cv
import numpy as np
import mss
from PIL import Image
import time
from operator import itemgetter
import argparse

main_screen_template = cv.imread('images/main_screen.png', 0)
start_button_template = cv.imread('images/start_button.png', 0)

left_danger_template = cv.imread('images/left_danger_branch.png', 0)
right_danger_template = cv.imread('images/right_danger_branch.png', 0)

width = pyautogui.size()[0]
height = pyautogui.size()[1]

monitor = {"top": 0, "left": 0, "width": width, "height": height}

with mss.mss() as sct:
    screen = sct.grab(monitor)
    screen_width = screen.size[0]
    screen_height = screen.size[1]

print(screen_width)
print(screen_height)