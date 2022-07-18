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

def convert(x,y):
    x = (width/2880) * x
    y = (height/1800) * y
    return x,y

def findLowestBranch(game_image, threshold):
    res_left = cv.matchTemplate(game_image, left_danger_template, cv.TM_CCOEFF_NORMED)
    res_right = cv.matchTemplate(game_image, right_danger_template, cv.TM_CCOEFF_NORMED)

    locs_left = np.where(res_left >= threshold)
    locs_right = np.where(res_right >= threshold)

    if len(locs_left[0]) > 0:
        locs_left = np.array([e for e in zip(*locs_left[::-1])])
        left_branch = max(locs_left,key=itemgetter(1))
        
    if len(locs_right[0]) > 0:
        locs_right = np.array([e for e in zip(*locs_right[::-1])])
        right_branch = max(locs_right,key=itemgetter(1))

    if len(locs_left[0]) > 0 and len(locs_right[0]) > 0:
        if left_branch[1] > right_branch[1]:
            return 'left'
        return 'right'
    
    if len(locs_left[0]) > 0:
        return 'left'
    return 'right'

def detect_start_screen():
    with mss.mss() as sct:
        while True:
            screen = sct.grab(monitor)
            img = Image.frombytes("RGB", screen.size, screen.bgra, "raw", "BGRX")
            img = np.array(img)
            img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
            res = cv.matchTemplate(img, main_screen_template, cv.TM_CCOEFF_NORMED)
            _,score,_,top_left = cv.minMaxLoc(res)
            if score > 0.95:
                break
    bot_right = (top_left[0]+main_screen_template.shape[0], top_left[1]+main_screen_template.shape[1])
    return [top_left, bot_right]

def start_game():
    with mss.mss() as sct:
        screen = sct.grab(monitor)
        img = Image.frombytes("RGB", screen.size, screen.bgra, "raw", "BGRX")
        img = np.array(img)
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        res = cv.matchTemplate(img,start_button_template,cv.TM_CCOEFF_NORMED)
        _,_,_,max = cv.minMaxLoc(res)
        x = (width/2880) * max[0]
        y = (height/1800) * max[1]
        pyautogui.moveTo(x+10, y+10)
        pyautogui.click()

def play_game(region, count):
    left = region[0][0]
    right = region[1][0]
    bot = region[1][1]
    top = region[0][1]

    left, top = convert(left, top)
    right, bot = convert(right, bot)
    
    game_space = {"top": top, "left": left, "width": right-left, "height": bot-top}

    with mss.mss() as sct:
        for _ in range(count):
            screen = sct.grab(game_space)
            img = Image.frombytes("RGB", screen.size, screen.bgra, "raw", "BGRX")
            img = np.array(img)
            img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
            branchSide = findLowestBranch(game_image=img, threshold=0.90)

            if branchSide == 'right':
                x, y = left, bot
                pyautogui.moveTo(x, y-50)
                pyautogui.click()
            else:
                x, y = right, bot
                pyautogui.moveTo(x, y-50)
                pyautogui.click()
            time.sleep(0.2) #delay required for game screen to clear so screenshot can be correctly analysed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=10, help="Set number of kicks to run program for.")
    args = parser.parse_args()

    region = detect_start_screen()
    start_game()
    play_game(region=region, count=args.runs)

if __name__ == '__main__':
    main()