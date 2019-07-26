# This file contains functions that use Optical Character Recognition (OCR) to detect text on a screen.
# These functions are designed to work well on a 1920 x 1080 screen 

from PIL import Image, ImageGrab
import numpy as np
import pytesseract
from time import sleep
import cv2 as cv


# class statusBoard():
#     """This class uses OCR to translate text from the status board to a string.
#        The status board contains Bet session status, current server, total amount
#        of bets and time left for the bet session."""
#     x1, y1, x2, y2 = 1522, 0, 1920, 40
#     img = ImageGrab.grab(bbox=(x1, y1, x2, y2)) # Ideal 398 x 40
#     pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract' # Tesseract location
#     text = pytesseract.image_to_string(img, lang = 'eng')
#     return text

# def victoryTeam():
#     """This function uses OCR to detect who won the game."""
#     x1, y1, x2, y2 = 750, 500, 1170, 550
#     img = ImageGrab.grab(bbox=(x1, y1, x2, y2)) # Ideal 310 x 50
#     pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract' # Tesseract location
#     text = pytesseract.image_to_string(img, lang = 'eng')
#     if "Red" in text:
#         return "Red"
#     else:
#         return "Blue"

print(statusBoard())