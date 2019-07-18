# This file contains functions that use Optical Character Recognition (OCR) to detect text on a screen.
# These functions are designed to work well on a 1920 x 1080 screen 

from PIL import Image, ImageGrab
import numpy as np
import pytesseract
from time import sleep
import cv2 as cv

def currentServer():
    """This function uses OCR to detect the current server."""
    # Take a screenshot and use OCR to extract the current server
    x1, y1, x2, y2 = 1522, 0, 1920, 40
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2)) # Ideal 398 x 40
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract' # Tesseract location
    text = pytesseract.image_to_string(img, lang = 'eng')
    if "Bets closed" in text:
        return text.split()[-1]
    else:
        return "Cannot detect current server due to minimized stream."

def victoryTeam():
    """This function uses OCR to detect who won the game."""
    # Take a screenshot and use OCR to extract the victory team
    x1, y1, x2, y2 = 750, 500, 1170, 550
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2)) # Ideal 310 x 50
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract' # Tesseract location
    text = pytesseract.image_to_string(img, lang = 'eng')
    if "Red" in text:
        return "Red"
    else:
        return "Blue"

# def detectLoadingScreen():
#     """This function uses OCR to detect League loading screen."""
#     # Take a screenshot and use OCR to extract the victory team
#     x1, y1, x2, y2 = 345, 1065, 385, 1080
#     img = ImageGrab.grab(bbox=(x1, y1, x2, y2)) # Ideal 310 x 50
#     pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract' # Tesseract location
#     text = pytesseract.image_to_string(img, lang = 'eng')
    

# detectLoadingScreen()

# def players():
#     Take a screenshot and use OCR to extract the victory team
#     x1, y1, x2, y2 = 300, 1000, 400, 1080
#     img = ImageGrab.grab(bbox=(x1, y1, x2, y2)) # Ideal 310 x 50
#     img.show()
#     pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract' # Tesseract location
#     text = pytesseract.image_to_string(img, lang = 'eng')
#     print(text)

def betTimer():
    pass