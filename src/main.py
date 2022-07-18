import pyautogui
import cv2 as cv
import numpy as np
import mss
from PIL import Image
import time
from operator import itemgetter

main_screen_template = cv.imread('images/main_screen.png', 0)
start_button_template = cv.imread('images/start_button.png', 0)

left_danger_template = cv.imread('images/left_danger_branch.png', 0)
right_danger_template = cv.imread('images/right_danger_branch.png', 0)

width = pyautogui.size()[0]
height = pyautogui.size()[1]

monitor = {"top": 0, "left": 0, "width": width, "height": height}

def findLowestBranch(game_image):
  res_left = cv.matchTemplate(game_image, left_danger_template, cv.TM_CCOEFF_NORMED)
  res_right = cv.matchTemplate(game_image, right_danger_template, cv.TM_CCOEFF_NORMED)

  threshold = 0.85
  locs_left = np.where(res_left >= threshold)
  locs_right = np.where(res_right >= threshold)

  locs_left = np.array([e for e in zip(*locs_left[::-1])])
  locs_right = np.array([e for e in zip(*locs_right[::-1])])

  left_branch = max(locs_left,key=itemgetter(1))
  right_branch = max(locs_right,key=itemgetter(1))

  if left_branch[1] > right_branch[1]:
    return 'left'
  return 'right'