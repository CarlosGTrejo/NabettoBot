# This file contains classes and functions that use Optical Character Recognition (OCR) to detect text on a screen.
# These functions are designed to work well on a 1920 x 1080 screen
# Because this project is for educational purposes, this file might contain peculiarly designed classes and functions

from PIL import Image, ImageGrab
import pytesseract
import numpy as np
from ctypes import windll # Fix not capture full screen issue

from time import sleep # For testing purpose


class StreamPos:
    """Contains stream positions needed for capturing information."""
    def __init__(self, status_banner = (1522, 0, 1920, 40), winner_banner = (750, 500, 1170, 550)): # Res order: x1, y1, x2, y2 
        self.status_banner: "Top right corner" = status_banner # Ideal 398 x 40
        self.winner_banner: "Center, after game ended" =  winner_banner # Ideal 310 x 50

    # ---> ADD MORE RESOLUTIONS TO CAPTURE ABOVE HERE <---
    
    def __str__(self):
        return "Current capturable stream positions: status banner, winner banner" # Temporary way to display all vars from __init__

class StreamCapture(StreamPos): # inherit attributes from StreamPos
    """Uses OCR to translate text from the stream to readable strings. First parameter accepts the location of tesseract. Only works with 1080p template."""
    def __init__(self, tesseract_local = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'):
        StreamPos.__init__(self) # initialize StreamPos with default parameter
        self.pytesseract_local = tesseract_local # Tesseract location
    
    def __str__(self):
        return "This object is an instance of StreamCapture class."
    
    def capture_status_banner(self):
        """Captures the status banner on the top left corner of the stream (at full 1080p)"""
        img = ImageGrab.grab(bbox = self.status_banner)
        pytesseract.pytesseract.tesseract_cmd = self.pytesseract_local 
        text = pytesseract.image_to_string(img, lang = 'eng')
        return text

    def capture_winner_banner(self):
        """Captures the winner banner at the stream's center (at full 1080p). Only works after the game."""
        img = ImageGrab.grab(bbox = self.winner_banner)
        pytesseract.pytesseract.tesseract_cmd = self.pytesseract_local
        text = pytesseract.image_to_string(img, lang = 'eng')
        if "Red" in text:
            return "Red"
        elif "Blue" in text:
            return "Blue"
        else:
            return "Cannot detect who won."

    # ---> ADD MORE FUNCTIONS TO CAPTURE ABOVE HERE <---

# TESTING PURPOSE ONLY. COMMENT WHEN IN PRODUCTION
if __name__ == "__main__":
    user32 = windll.user32
    user32.SetProcessDPIAware()
    stream_info = StreamCapture()
    status_banner = stream_info.capture_status_banner()
    winner_banner = stream_info.capture_winner_banner()
    print(status_banner)
    print(winner_banner)
else:
    print("Capture.py has been imported!")
