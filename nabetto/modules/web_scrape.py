from selenium import webdriver
import requests
from getpass import getpass
from time import sleep

def web_scrape():
    USERNAME = input()
    PASSWORD = getpass()

    # Generate a new link from my.saltyteemo.com to twitch for authentication
    twitch_url = "https://gameinfo.saltyteemo.com/"

    # Open chrome in incognito -> access the link
    options = webdriver.ChromeOptions()
    # options.add_argument("--incognito")

    driver = webdriver.Chrome(executable_path=r"C:\Users\Minh Luu\Documents\GitHub\NabettoBot\chromedriver_win32\chromedriver.exe", options=options)
    driver.get(twitch_url)

    sleep(20)

    # Authenticate
    username = driver.find_element_by_id("login-username")
    username.clear()
    username.send_keys(USERNAME)


    password = driver.find_element_by_id("password-input")
    password.clear()
    password.send_keys(PASSWORD)


    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button").click()

    sleep(15)


    # Get player name a region
    driver.get(twitch_url)
    sleep(3)
    print(driver.current_url)
    region, name = driver.current_url.split('/live/')[1].split('?')[0].split('/')
    return region, name


if __name__ == "__main__":
    web_scrape()