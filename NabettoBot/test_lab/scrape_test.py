from selenium import webdriver
from getpass import getpass
from time import sleep
import sys, os

def main():

    USERNAME = input("Username: ")
    PASSWORD = getpass()

    # Open chrome in incognito -> access the link
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Minh Luu\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get("https://my.saltyteemo.com/")
    sleep(10)

    # Authenticate
    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys(USERNAME)

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(PASSWORD)

    driver.find_element_by_class_name("buttons").click()

    sleep(10) # Wait to pass another CloudFlare page

    # Get the balance
    while (True):
        driver.refresh()
        balance = driver.find_element_by_id("f1").text
        balance = balance.split("\n")
        print(balance[1])
        sleep(30)

if __name__ == "__main__":
    main()