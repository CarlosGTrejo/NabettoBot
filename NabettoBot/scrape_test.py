import cfscrape
from selenium import webdriver
from getpass import getpass
from time import sleep

USERNAME = "vgfan1996"
PASSWORD = "19647328"

# Generate a new link from my.saltyteemo.com to twitch for authentication
scraper = cfscrape.CloudflareScraper()
twitch_url = scraper.get("https://my.saltyteemo.com/").url

# Open chrome in incognito -> access the link
options = webdriver.ChromeOptions()
# options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path=r"C:\Users\Minh Luu\Downloads\chromedriver_win32\chromedriver.exe", options=options)
driver.get(twitch_url)


# Authenticate
username = driver.find_element_by_id("username")
username.clear()
username.send_keys(USERNAME)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(PASSWORD)

driver.find_element_by_class_name("buttons").click()

sleep(10)

# Get the balance
balance = driver.find_element_by_id("f1").text
balance = balance.split("\n")

print(balance[1])

driver.quit()