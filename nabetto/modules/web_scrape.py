from selenium import webdriver
from time import sleep

def web_scrape():

    # Generate a new link from my.saltyteemo.com to twitch for authentication
    game_info_url = "https://gameinfo.saltyteemo.com/"

    # Open chrome in incognito -> access the link
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=C:\\Users\\Minh Luu\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path=r"C:\Users\Minh Luu\Documents\GitHub\NabettoBot\chromedriver_win32\chromedriver.exe", chrome_options=options)

    # Get player name a region
    driver.get(game_info_url)
    sleep(5)
    region, name = driver.current_url.split('/live/')[1].split('?')[0].split('/')
    driver.quit()
    return region, name


if __name__ == "__main__":
    web_scrape()