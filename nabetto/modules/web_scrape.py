from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os


def web_scrape():

    # Path to Chrome driver and user profile
    profile_subpath = "Google\\Chrome\\User Data"
    profile_path = os.path.join(os.getenv("LOCALAPPDATA"), profile_subpath)
    print(profile_path)
    chrome_subpath = "Documents\\GitHub\\NabettoBot\\chromedriver_win32\\chromedriver.exe"
    chrome_path = os.path.join(os.getenv("USERPROFILE"), chrome_subpath)

    # Generate a new link from my.saltyteemo.com to twitch for authentication
    game_info_url = "https://gameinfo.saltyteemo.com/"

    # Open chrome in incognito -> access the link
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument('--profile-directory=Profile 1')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path=chrome_path, options=options)

    # Get player name a region
    driver.get(game_info_url)
    delay = 10
    try:
        # Wait until the website is loaded completely
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/nav/div/a')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    try:
        region, name = driver.current_url.split(
            '/live/')[1].split('?')[0].split('/')
    except IndexError:
        print("Cannot retrieve player's name and his/her server.")
    driver.close()
    return region, name


if __name__ == "__main__":
    web_scrape()
