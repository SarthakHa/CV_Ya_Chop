import pytest
import cv2 as cv
from src.main import findLowestBranch

def test_lowest_branch():
    test_img_0 = cv.imread('tests/resources/test_0.png')
    test_img_0 = cv.cvtColor(test_img_0, cv.COLOR_RGB2GRAY)

    test_img_1 = cv.imread('tests/resources/test_1.png')
    test_img_1 = cv.cvtColor(test_img_1, cv.COLOR_RGB2GRAY)

    test_img_2 = cv.imread('tests/resources/test_2.png')
    test_img_2 = cv.cvtColor(test_img_2, cv.COLOR_RGB2GRAY)

    assert findLowestBranch(test_img_0, 0.9) == 'left'
    assert findLowestBranch(test_img_1, 0.9) == 'right'
    assert findLowestBranch(test_img_2, 0.9) == 'right'