import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def web_scrape():
    # Generate a new link from my.saltyteemo.com to twitch for authentication
    game_info_url = "https://gameinfo.saltyteemo.com/"
    # Open chrome in incognito -> access the link
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir={}\\Google\\Chrome\\User Data".format(os.getenv("LOCALAPPDATA")))
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path=r"..\..\chromedriver_win32\chromedriver.exe", chrome_options=options)

    # Get player name a region
    driver.get(game_info_url)
    delay = 20
    try:
        # Wait until the 
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/nav/div/a')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    try:
        region, name = driver.current_url.split('/live/')[1].split('?')[0].split('/')
    except IndexError:
        print("Cannot retrieve player's name and his/her server.")
    else:
        return region, name
    finally:
        driver.close()


if __name__ == "__main__":
    web_scrape()
